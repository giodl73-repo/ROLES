# ROLES Principles

## ROLES-P-01: Repository Local Judgment

**Status:** ACTIVE

**Statement:** `.roles` panels belong inside the repository whose work they review.

**Decision rule:** ROLES should provide a portable convention and tooling, not a central role catalog that overrides local review language.

**Evidence:** `README.md`, `SPEC.md`, `docs/adoption-guide.md`, and `tools/init_roles.py`.

## ROLES-P-02: Markdown Is The Source Of Truth

**Status:** ACTIVE

**Statement:** Human-readable Markdown role files are the canonical review contract.

**Decision rule:** Schemas, checkers, and assistant skills may validate or scaffold role files, but they must not replace the local Markdown panel.

**Evidence:** `README.md`, `SPEC.md`, `schemas/`, `tools/check_roles.py`, and `tools/check-roles.ps1`.

## ROLES-P-03: Roles Ask Questions, They Do Not Own Doctrine

**Status:** ACTIVE

**Statement:** ROLES defines who reviews and what evidence they inspect; PITFALL owns durable principles, invariants, and recurring failure patterns.

**Decision rule:** A role may cite PITFALL IDs, but should not copy PITFALL doctrine into the role file.

**Evidence:** `README.md`, `SPEC.md`, `docs/adoption-guide.md`, and `.pitfall/roles-pitfalls.md`.

## ROLES-P-04: Roles Can Own Review Gates, Not The Trace

**Status:** ACTIVE

**Statement:** Roles may act as VTRACE review owners or gates while VTRACE remains the mission-to-evidence trace.

**Decision rule:** Role files should not become a parallel requirement table, validation ledger, or release trace.

**Evidence:** `README.md`, `SPEC.md`, `docs/recommended-skills.md`, and `research/README.md`.

## ROLES-P-05: Validators Report Drift Conservatively

**Status:** ACTIVE

**Statement:** ROLES validators catch structural drift without flattening local voice or creative tier names.

**Decision rule:** Hard failures should stay limited to missing required entry points and invalid stable identifiers; richer panel quality remains a review question.

**Evidence:** `SPEC.md`, `tools/check_roles.py`, `tools/check-roles.ps1`, `tests/check-proof.ps1`, and `docs/improving-panels.md`.
