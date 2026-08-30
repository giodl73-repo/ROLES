# ROLES Invariants

## ROLES-I-01: ROLE.md Is The Required Entry Point

**Status:** VERIFIED

**Invariant:** A conforming `.roles` directory has `.roles/ROLE.md`.

**Why it matters:** Reviewers and assistants need one discoverable start point.

**Evidence:** `SPEC.md`, `tools/check_roles.py`, `tools/check-roles.ps1`, and `examples/minimal/.roles/ROLE.md`.

**Test:** `pwsh -NoProfile -File tests\check-proof.ps1`.

## ROLES-I-02: Slugs Are Stable Lowercase Kebab-Case Identifiers

**Status:** VERIFIED

**Invariant:** When a role file declares `slug`, the slug is lowercase kebab-case.

**Why it matters:** Stable IDs are the minimum structure needed for automation without prescribing role prose.

**Evidence:** `SPEC.md`, `schemas/role.schema.json`, `tools/check_roles.py`, `tools/check-roles.ps1`, and `tests/fixtures/invalid-slug/`.

**Test:** `pwsh -NoProfile -File tests\check-proof.ps1`.

## ROLES-I-03: Python And PowerShell Checkers Agree On Retained Proof

**Status:** VERIFIED

**Invariant:** Both checker entry points accept the minimal fixture and reject the invalid-slug fixture.

**Why it matters:** README advertises the Python checker while Windows users may run the PowerShell wrapper.

**Evidence:** `tests/check-proof.ps1`, `tools/check_roles.py`, `tools/check-roles.ps1`, `examples/minimal/`, and `tests/fixtures/invalid-slug/`.

**Test:** `pwsh -NoProfile -File tests\check-proof.ps1`.

## ROLES-I-04: Metadata Is Recommended, Not Required

**Status:** VERIFIED

**Invariant:** Missing role-file frontmatter is a warning in the Python checker, not a conformance failure.

**Why it matters:** Existing repos can adopt ROLES gradually without rewriting useful local panels.

**Evidence:** `SPEC.md`, `docs/conformity.md`, and `tools/check_roles.py`.

**Test:** `python tools\check_roles.py examples\minimal`.

## ROLES-I-05: Research Claims Stay Portfolio-Bounded

**Status:** VERIFIED

**Invariant:** ROLES research describes the managed portfolio dataset without claiming the same distributions hold across independent ecosystems.

**Why it matters:** ROLES is a public convention; research claims need bounded evidence.

**Evidence:** `research/README.md`, `research/portfolio-role-quality-study.md`, and `research/productive-tension-study.md`.

**Test:** `git diff --check`.
