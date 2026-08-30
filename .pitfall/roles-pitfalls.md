# ROLES Pitfalls

## ROLES-PF-01: Retained Proof Covers Only One Checker Path

**Status:** MITIGATED

**Pattern:** The retained proof validates the PowerShell checker while README and most cross-platform users rely on the Python checker.

**Domain:** `tests/check-proof.ps1`, `tools/check_roles.py`, `tools/check-roles.ps1`, README proof claims, and validator compatibility.

**Detection difficulty:** Both checkers can work individually while the advertised retained proof silently covers only one path.

**Structural solution:** Make the retained proof exercise both checkers on the accepted minimal fixture and invalid-slug fixture.

**Evidence:** PITFALL adoption updated `tests/check-proof.ps1`; `pwsh -NoProfile -File tests\check-proof.ps1` passes.

## ROLES-PF-02: Roles Absorb PITFALL Doctrine

**Status:** MITIGATED

**Pattern:** Role files copy repository principles, invariants, or recurring failure-pattern text and become a second doctrine ledger.

**Domain:** `SPEC.md`, `docs/adoption-guide.md`, README doctrine/traceability guidance, repo-local role authoring, and PITFALL adopters.

**Detection difficulty:** Copying doctrine into a role can feel helpful because it puts everything near the reviewer.

**Structural solution:** Roles may cite PITFALL IDs as evidence or rationale, but PITFALL remains the durable doctrine owner.

**Evidence:** PITFALL adoption added doctrine/trace hooks to `SPEC.md` and `docs/adoption-guide.md`; `README.md` already named the boundary.

## ROLES-PF-03: Roles Replace VTRACE Traceability

**Status:** MITIGATED

**Pattern:** Role files become requirement, verification, validation, or release-trace tables because roles are present during review.

**Domain:** `SPEC.md`, `docs/adoption-guide.md`, VTRACE adopters, release reviews, and repo-local assistant skills.

**Detection difficulty:** A role acting as a review gate can look like the natural place to store the full trace.

**Structural solution:** Roles may serve as VTRACE review owners or gates, but VTRACE owns mission-to-evidence trace records.

**Evidence:** PITFALL adoption added doctrine/trace hooks to `SPEC.md` and `docs/adoption-guide.md`; `README.md` already named the boundary.

## ROLES-PF-04: Template Panels Become Universal Governance

**Status:** OPEN

**Pattern:** Starter templates or recommended tiers are treated as mandatory global governance instead of a local starting point.

**Domain:** `tools/init_roles.py`, `docs/adoption-guide.md`, `SPEC.md`, public examples, and assistant-authored panels.

**Detection difficulty:** Templates are easy to copy and can look official even when local evidence needs different tiers or roles.

**Structural solution:** Keep template language explicitly optional, preserve local tier names, and require adopters to replace generic checks with repository evidence.

**Evidence:** `SPEC.md`, `docs/adoption-guide.md`, `docs/improving-panels.md`, and `tools/init_roles.py`.

## ROLES-PF-05: Research Portfolio Becomes External Proof

**Status:** OPEN

**Pattern:** ROLES research based on one managed portfolio is presented as proof of independent open-source or organizational role-panel behavior.

**Domain:** `research/README.md`, `research/portfolio-role-quality-study.md`, `research/productive-tension-study.md`, README claims, and future public papers.

**Detection difficulty:** The dataset is large enough to sound general even though it is still portfolio-bounded and correlated.

**Structural solution:** Keep research claims scoped to the managed portfolio unless independent datasets are collected.

**Evidence:** `research/README.md`, `research/portfolio-role-quality-study.md`, and `research/productive-tension-study.md`.
