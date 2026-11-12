#!/usr/bin/env python3
"""Dependency-free semantic checks for portable human capability evidence records."""
from __future__ import annotations
import argparse, copy, json, sys
from datetime import datetime
from pathlib import Path

FIXTURE=Path("examples/human_capabilities/capability-record.json")

def timestamp(value,label):
    if not isinstance(value,str): raise ValueError(f"{label} must be an ISO-8601 timestamp")
    try: parsed=datetime.fromisoformat(value.replace("Z","+00:00"))
    except ValueError as exc: raise ValueError(f"{label} must be an ISO-8601 timestamp") from exc
    if parsed.tzinfo is None: raise ValueError(f"{label} must include a timezone")
    return parsed

def validate(record,profile):
    if record.get("schema_version")!="1.0.0": raise ValueError("unsupported schema version")
    subject=record["subject"]; status=record["status"]; provenance=record["provenance"]
    if not record.get("evidence"): raise ValueError("capability claim requires evidence")
    for item in record["evidence"]:
        if len(item.get("artifact_sha256",""))!=64: raise ValueError("evidence artifact requires SHA-256")
        timestamp(item["occurred_at"],"evidence.occurred_at")
    timestamp(record["assessment"]["assessed_at"],"assessment.assessed_at")
    timestamp(provenance["recorded_at"],"provenance.recorded_at")
    consent=record["consent"]
    timestamp(consent["recorded_at"],"consent.recorded_at")
    if subject["subject_type"]=="human" and consent["status"]!="granted":
        raise ValueError("human capability records require recorded granted consent")
    if consent["status"]=="withdrawn" and status not in {"suspended","revoked","expired"}:
        raise ValueError("withdrawn consent cannot leave a capability claim active")
    review=record["independent_review"]
    if status=="mastery_credentialed":
        if review["status"]!="passed" or not review.get("reviewer_id") or not review.get("review_ref"):
            raise ValueError("mastery credential requires passed independent review")
        if review["reviewer_id"] in {provenance["submitted_by"],record["assessment"]["assessed_by"]}:
            raise ValueError("submitter or assessor cannot independently proctor their own mastery")
        if review.get("proctor_authorized") is not True:
            raise ValueError("mastery credential requires an authorized independent proctor")
        if record["attestation"]["status"]!="signed" or record["attestation"]["algorithm"]!="Ed25519" or not record["attestation"].get("signature"):
            raise ValueError("mastery credential requires an Ed25519 attestation structure")
    if record["attestation"]["status"]=="revoked" and status!="revoked":
        raise ValueError("revoked attestation must revoke or suspend the capability claim")
    if profile=="c2o" and record["governance"]["authority_class"]=="Controlled":
        if not record["governance"].get("policy_ref") or not record["governance"].get("approval_ref"):
            raise ValueError("C2O Controlled capability requires policy and approval references")
    if profile=="universalis" and record["governance"]["authority_class"]=="Controlled":
        raise ValueError("public UNIVERSALIS profile cannot import C2O Controlled authority")
    if consent["status"]=="granted" and not consent.get("record_ref"):
        raise ValueError("granted human consent requires a record reference")
    return True

def self_test(root):
    record=json.loads((root/FIXTURE).read_text(encoding="utf-8"))
    validate(record,"universalis"); validate(record,"c2o")
    cases=[]
    bad=copy.deepcopy(record); bad["subject"]["subject_type"]="human"; bad["consent"]["status"]="not_required"; cases.append((bad,"human consent"))
    bad=copy.deepcopy(record); bad["independent_review"]["reviewer_id"]=bad["provenance"]["submitted_by"]; cases.append((bad,"self-review"))
    bad=copy.deepcopy(record); bad["independent_review"]["proctor_authorized"]=False; cases.append((bad,"unauthorized proctor"))
    bad=copy.deepcopy(record); bad["evidence"]=[]; cases.append((bad,"missing evidence"))
    bad=copy.deepcopy(record); bad["governance"]["authority_class"]="Controlled"; cases.append((bad,"public controlled authority"))
    bad=copy.deepcopy(record); bad["consent"]["status"]="withdrawn"; cases.append((bad,"withdrawn consent"))
    for bad,label in cases:
        try: validate(bad,"universalis")
        except (ValueError,KeyError,TypeError): continue
        raise AssertionError("negative test unexpectedly passed: "+label)
    controlled=copy.deepcopy(record); controlled["governance"].update({"authority_class":"Controlled","policy_ref":"policy:fixture","approval_ref":"approval:fixture"}); validate(controlled,"c2o")
    print("Human capability contract self-test: PASS (2 profiles, 7 negative/positive boundary cases)")

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--profile",choices=("c2o","universalis"),default="universalis")
    p.add_argument("--self-test",action="store_true"); p.add_argument("--check",action="store_true")
    p.add_argument("--root",type=Path,default=Path(__file__).resolve().parents[2]); a=p.parse_args(); root=a.root.resolve()
    if a.self_test: self_test(root)
    if a.check:
        try: validate(json.loads((root/FIXTURE).read_text(encoding="utf-8")),a.profile); print(f"Human capability validation: PASS (profile={a.profile})")
        except (OSError,UnicodeError,json.JSONDecodeError,ValueError,KeyError,TypeError) as exc: print("Human capability validation: FAIL: "+str(exc)); return 1
    if not a.self_test and not a.check: p.error("choose --self-test and/or --check")
    return 0
if __name__=="__main__": sys.exit(main())
