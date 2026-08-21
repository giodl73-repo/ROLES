# Role Panels in Practice

## A Structural Study of 77 Repository-Local Review Systems

**Study date:** 2026-08-21  
**Dataset:** 77 managed repositories, 1,120 committed role files  
**Authority:** ROLES v0.1

**Snapshot note:** Results describe the baseline captured before the ROLES
self-improvement published with this paper. That intervention adds an Adopter
Advocate and an explicit tension contract, increasing tension-ready panels from
three to four. The subsequent SCENARIUM pilot raises the count to five.

## Abstract

This study examines how 77 repositories implement the `.roles` convention.
It asks whether repository-local review panels are present, grounded in their
work, diverse in viewpoint, explicit about disagreement, actionable during
review, and maintainable over time.

Adoption is broad: 70 repositories have `.roles/ROLE.md`, and 62 have at least
one role file. Operational completeness is much rarer. Only 10 non-empty panels
link every role from their index, and only three panels have a strong explicit
tension contract. Fifteen repositories have no active role files. Three
repositories contain more than 40 roles and need an active-core model rather
than further catalog growth.

The central finding is that role count is not a useful quality proxy. The
strongest panels in this sample are bounded systems whose roles name concrete
artifacts, ask different hard questions, and explain how disagreements are
handled.

## Research questions

1. How widely has the required `.roles/ROLE.md` entry point been adopted?
2. Do indexes identify the active panel rather than merely announce it?
3. Are roles specific to repository promises, artifacts, and failure modes?
4. Do panels represent materially different review concerns?
5. Is disagreement between roles explicit and usable?
6. Can maintainers tell when to invoke a role and what evidence to inspect?
7. Does panel size create maintenance or selection pressure?

## Dataset and selection

The sample contains every repository classified `managed` in the TRACKER
portfolio inventory on the study date. Each repository is evaluated at the
commit pinned by TRACKER, not at an uncommitted working tree or a newly fetched
branch tip. This makes the study reproducible and prevents concurrent repository
updates from changing results during a run.

The unit of analysis is a repository panel. Role files within one repository
are not treated as independent observations because they share authorship,
vocabulary, and governance.

## Method

The audit generates a 100-point structural score:

| Dimension | Points | Observable question |
|---|---:|---|
| Conformance | 20 | Is there an indexed, metadata-bearing panel consistent with ROLES? |
| Repository grounding | 20 | Do roles name local artifacts, domain obligations, promises, and risks? |
| Viewpoint diversity | 15 | Are materially different failure concerns represented? |
| Productive tension | 20 | Are disagreements between roles explicit rather than averaged away? |
| Actionability | 15 | Do roles say what to inspect, when to invoke them, and what evidence matters? |
| Maintainability | 10 | Is the active panel bounded, indexed, unique, and consistently described? |

Safeguards prevent count from dominating:

- missing `.roles/ROLE.md` caps the total at 20;
- an index with no role files caps the total at 15;
- more than 80 role files caps the total at 79;
- role count alone earns no grounding, diversity, tension, or actionability
  points.

The generator uses index links, recommended frontmatter, tier structure,
repository terms, concrete artifact references, review-lens sections,
evidence instructions, and explicit tension declarations. It emits both JSON
and Markdown and includes a check mode for stale outputs.

## Results

### Portfolio summary

| Measure | Result |
|---|---:|
| Managed repositories | 77 |
| Committed role files | 1,120 |
| Repositories with `.roles/ROLE.md` | 70 |
| Repositories with at least one role file | 62 |
| Fully indexed non-empty panels | 10 |
| Panels with a strong explicit tension contract | 3 |
| Catalogs with more than 40 roles | 3 |
| Average score | 50.8 / 100 |

### Score bands

| Band | Range | Repositories |
|---|---:|---:|
| Exemplary | 85-100 | 0 |
| Strong | 70-84 | 11 |
| Developing | 50-69 | 46 |
| Thin | 0-49 | 20 |

No repository reached the exemplary band. This is useful: the rubric leaves
room for every panel, including ROLES itself, to improve.

### Panel size

| Active role files | Repositories |
|---|---:|
| 0 | 15 |
| 1-5 | 17 |
| 6-15 | 21 |
| 16-40 | 21 |
| More than 40 | 3 |

The sample includes both placeholder adoption and very large specialist
catalogs. Neither extreme is sufficient by itself. A useful panel needs enough
distinct lenses to create coverage, but few enough active roles that a reviewer
can select and apply them intentionally.

### Dimension averages

| Dimension | Raw average | Share of available points |
|---|---:|---:|
| Conformance | 12.1 / 20 | 60.5% |
| Repository grounding | 13.1 / 20 | 65.5% |
| Viewpoint diversity | 9.4 / 15 | 62.7% |
| Productive tension | 4.6 / 20 | 23.0% |
| Actionability | 6.9 / 15 | 46.0% |
| Maintainability | 5.8 / 10 | 58.0% |

Productive tension is the largest portfolio gap. Grounding and diversity are
more common than an explicit account of what happens when grounded, diverse
roles disagree.

## Findings

### 1. Entry-point adoption exceeds usable indexing

Seventy repositories have the required index, but only 10 non-empty panels link
every active role. In this sample, indexes often describe a panel without
providing navigable links to its role files. The distinction between "an index
exists" and "the active panel is operable from the index" should remain visible
in tooling and guidance.

### 2. Empty adoption is a real maturity stage

Fifteen repositories have no active role files. Eleven of them have an index
but no roles; four have no `.roles` surface. This is not a reason to reject
incremental conformance. It is a reason to give maintainers a small next step:
one role for the public promise, one stakeholder role, and one communication
role.

### 3. Productive tension is uncommon

Only three panels reach the study's threshold for an explicit tension contract.
Many repositories have multiple credible reviewers but do not state where
their obligations conflict. Without that connection, diversity remains a list
of perspectives rather than a decision system.

### 4. Bounded panels are easier to operate

The leading panels use focused sets of roughly 8-16 roles. Three catalogs have
more than 40 roles, including two with more than 150. Large catalogs can carry
valuable domain expertise, but they need:

- a small active panel;
- selection rules for specialists;
- an explicit review order;
- complete index coverage;
- retirement or archival rules.

The recommendation is not to delete specialist knowledge. It is to separate
the default decision group from the roster that can be called when needed.

### 5. Concrete evidence turns personas into reviewers

High-scoring role files name repository artifacts, tests, schemas, commands,
datasets, claims, or failure modes. Weak role files describe a disposition
without telling the reviewer what to inspect. The difference is operational:
a persona says how to sound; a role says what evidence could change its
judgment.

## Implications for ROLES

1. Preserve Minimal conformance, but teach the difference between presence and
   an operable panel.
2. Make complete index links a prominent improvement step.
3. Add productive-tension examples to starter guidance.
4. Recommend active-core plus specialist-roster designs for large catalogs.
5. Keep scores diagnostic. Every score should produce a concrete next action.
6. Encourage repositories to measure role use, not only role-file structure.

## Threats to validity

- **Single portfolio:** the repositories share maintainers and conventions.
- **Structural measures:** the audit does not observe whether roles were
  invoked or whether they prevented defects.
- **Heuristic classification:** textual signals can miss unusual but valid
  local writing styles.
- **Unequal maturity:** repositories range from placeholders to long-running
  systems.
- **Correlated role files:** 1,120 files do not represent 1,120 independent
  review systems.
- **Snapshot timing:** results describe pinned commits on one date.

The appropriate interpretation is comparative and diagnostic, not causal.

## Reproduction

From a TRACKER checkout with its pinned submodules available:

```powershell
.\scripts\refresh-portfolio-role-quality.ps1
.\scripts\refresh-portfolio-role-quality.ps1 -Check
```

Inspect:

- `portfolio-role-quality.json` for machine-readable scores and inputs;
- `PORTFOLIO_ROLE_QUALITY.md` for the ranking and improvement queue;
- `scripts/refresh-portfolio-role-quality.ps1` for the complete scoring rules.

Future studies should retain the generated JSON for each dated snapshot so
panel changes can be compared longitudinally.
