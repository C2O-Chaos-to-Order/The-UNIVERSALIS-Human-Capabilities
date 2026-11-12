# Human Capabilities Architecture

**Status:** First portable evidence contract and deterministic validator implemented in this branch. All named products and standards below remain owner-supplied candidates or reference patterns pending source, license, security, maintenance, and compatibility review.

## 1. Architectural split

UNIVERSALIS provides open, evidence-producing instruments that humans and agents can independently operate and verify. C2O provides private, governed, audited, authority-bounded instruments. Shared protocols carry portable capability evidence and consent—not private policy, authority tokens, or personal source material.

A capability claim is not a permission grant. Evidence that a person or agent can perform a task does not authorize that subject to perform it in a protected environment or on behalf of another party.

## 2. UNIVERSALIS candidate inventory

| Sub-layer | Owner-supplied tools | Role in the supplied document |
|---|---|---|
| Sensory/accessibility | human-mcp; a11y-toolkit | Eyes/Hands/Mouth/Brain sensory MCP surface; accessibility audit/fix/document/watch/handoff and human-signable evidence |
| Skill/capability attestation | Kredo; Gaia; ToolGym; SkillSeal | Peer-signed competence evidence; public evidence ledger; workout/simulation/qualification/mastery ladder; isolated execution and signed skill-quality evidence |
| Human-in-the-loop / teaming | Everstaff; SecTrust; Magentic-UI; Enju; MOSAIC | Human checkpoints, async approval queues, auditable DAGs, human-agent co-planning, peer task workflow, and cross-paradigm evaluation |
| Ethics / maturity | WIA-AUG-012; HCQM | Augmentation ethics and a human/synthetic capability taxonomy with constructs and behavioral indicators |

The source describes human-mcp Ears as planned, not complete. The source's 29-tool, 32-tool, WCAG coverage, and other product statements are user-supplied claims, not independently verified here.

## 3. C2O candidate inventory

| Sub-layer | Owner-supplied tools | Role in the supplied document |
|---|---|---|
| Private audited knowledge/capability | CueCrux; Pythia; C2Cognitive; C2 Companion; JADE Decision Governance | Cited encrypted corpus, correction-propagating atomic claims, L0–L3 bounded cognition, repository-as-audit-trail, and human-held execution permits |
| Enterprise reference patterns | Cloudflare OS; CoWork OS; Kerdos OS | Zero-trust per-resource authorization, approval gates, guardrail budgets, audit sidecars, and review trails |

Cloudflare OS, CoWork OS, and Kerdos OS are recorded as reference patterns in the supplied material, not directly deployable C2O components.

## 4. Shared portable trust substrates

PACT Passport; Open Agent Passport (OAP); Cognitive Skill Passport (CSP-0.1); Agent Passport System (APS); Cupel; MortarCAPS Human Capability Record; Enju; MOSAIC.

Their shared purpose is portability of identity-bound capability evidence, competence provenance, consent-gated verification, peer workflow, and cross-paradigm interaction. They do not collapse C2O and UNIVERSALIS authority models.

## 5. Minimum capability evidence contract

The first executable increment is the JSON Schema in schemas/human-capabilities/capability-record.v1.schema.json, with a synthetic example in examples/human_capabilities/capability-record.json and dependency-free checks in .github/scripts/human_capability_contract.py.

The record contains:
- subject reference and subject type (human, agent, organization);
- capability identifier, domain, taxonomy reference, and description;
- proficiency label and rubric/indicator references;
- assessment method, assessor, date, and assessment reference;
- evidence artifact references with SHA-256 hashes, timestamps, result, and test-suite hash;
- provenance and submitter attribution;
- purpose-bound consent record;
- independent review/proctor status;
- attestation status and algorithm metadata;
- Evidence/Advisory/Controlled governance classification.

Mastery is not inferred from a workout alone. A mastery_credentialed record requires a passed review from a distinct, authorized proctor and an Ed25519 attestation structure. The validator checks structure and reviewer independence; it does not cryptographically verify signature bytes.

## 6. Boundary rules

- A human subject requires an explicit granted consent record. Withdrawal suspends/revokes/expires the active capability claim and prevents further use pending handling.
- Assessment, evidence, and independent review are separate roles; submitter/assessor cannot serve as the independent mastery proctor.
- Evidence and Advisory are descriptions of demonstrated capability, not authorization to act.
- C2O Controlled records require private policy and approval references; these fields must not cross into public UNIVERSALIS.
- The same v1 evidence structure can be exchanged, but each ecosystem applies its own privacy, authorization, reviewer, and revocation rules.
- Human capability evidence must be minimized, purpose-scoped, revocable, and exportable by the relevant rights-holder.

## 7. Evidence status and limits

| Item | Status |
|---|---|
| Supplied candidate inventories recorded | Documented |
| Portable capability evidence schema and synthetic fixture | Implemented in this branch |
| Dependency-free semantic validator and negative cases | Implemented in this branch |
| Human-capability product integrations | Not implemented |
| Live identity, consent, credential signing/verification, revocation service | Not implemented |
| Full JSON Schema 2020-12 validation | Pending |
| Candidate source/license/security verification | Pending |
| Real human assessment or mastery evaluation | Not performed |
