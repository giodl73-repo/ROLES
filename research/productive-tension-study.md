# Productive Tension in Repository Review Panels

## From a List of Perspectives to a Decision System

This paper analyzes the 2026-08-21 pre-intervention baseline. ROLES then applied
the findings to its own panel by adding pairwise tensions, review order, and an
Adopter Advocate.

## Abstract

A diverse role catalog does not automatically produce a useful review. Roles
become a panel when their obligations differ, their disagreements are named,
and the repository explains how those disagreements affect a decision.

This paper develops a practical model of productive tension from a structural
audit of 77 repository panels. Only three panels in the sample have a strong
explicit tension contract. Tension is the weakest scoring dimension, averaging
4.6 of 20 available points. The strongest examples use pairwise conflict
statements, hard-stop rules, review routing, and evidence-specific questions.

Productive tension is not performative argument. It is a durable record of
which valid concern must not disappear when another valid concern is optimized.

## The problem with parallel personas

Consider three plausible roles:

- an architecture reviewer;
- a user advocate;
- a release operator.

All three can produce thoughtful comments while still failing as a panel. If
the repository never states how architectural purity trades against migration
cost, or how release urgency trades against recoverability, reviewers can
silently average the concerns into a vague approval.

A role list answers "who might review?" A tension contract also answers:

- Which obligations can conflict?
- What evidence does each side bring?
- Is either concern a hard stop?
- Who decides when both claims are valid?
- Must the disagreement remain visible in the final finding?

## A five-part tension contract

### 1. Distinct obligation

Each role protects something another role can rationally sacrifice. Two roles
that ask the same question with different persona names do not create useful
tension.

Examples of distinct obligations:

- correctness versus usability;
- evidence completeness versus delivery speed;
- transparency versus privacy;
- backward compatibility versus simplification;
- local optimization versus portfolio interoperability.

### 2. Pairwise edge

Name the relationship directly:

| Pulls | Against | Because |
|---|---|---|
| Correctness Auditor | Performance Steward | Extra optimization can weaken invariants or observability. |
| User Advocate | Boundary Steward | A simpler workflow can tempt the API to hide consequential state. |

The `Because` column matters. It distinguishes a real tradeoff from decorative
opposition.

### 3. Evidence boundary

Each side should identify evidence that can change its judgment. A useful
disagreement might compare:

- a failing invariant test with a latency benchmark;
- a migration fixture with a proposed schema simplification;
- a threat model with an observability requirement;
- a reader task test with a completeness checklist.

Without evidence boundaries, a conflict becomes preference against preference.

### 4. Adjudication rule

Not every panel needs a strict hierarchy, but it needs a decision protocol.
Common patterns include:

- **hard stop:** legal invalidity, data corruption, or safety failure blocks;
- **ordered review:** establish evidence before evaluating usability;
- **scope split:** one role governs the public contract, another implementation
  freedom inside it;
- **documented dissent:** both findings remain visible for the owner to decide;
- **experiment:** specify the measurement that resolves an empirical conflict.

### 5. Invocation trigger

Tension is useful only when the relevant pair is selected. The index should map
change types to roles:

| Change | Invoke |
|---|---|
| Public API or schema | Boundary Steward + Downstream Maintainer |
| Performance optimization | Correctness Auditor + Performance Steward |
| New telemetry | Operator Advocate + Privacy Steward |
| Documentation redesign | Subject Expert + First-Run Reader |

This keeps a large roster from becoming an all-reviewers-on-every-change tax.

## Patterns observed in strong panels

### Tension matrix

BISECT, PROOF, and ICELINES make pairwise pulls visible in their panel indexes.
The matrix is compact, searchable, and difficult to misread. It also exposes
missing edges: a role with no relationship to any other role may be ornamental
or insufficiently integrated.

### Tiebreaker ranking

Some panels state that legal validity, data integrity, safety, or correctness
precedes advisory concerns. Rankings are useful when they express repository
policy rather than status among personas.

### Core panel plus specialists

ICELINES distinguishes core perspectives from specialists for a surface or
delivery channel. This model is particularly important for catalogs with
dozens or hundreds of roles. The active panel makes default review tractable;
the specialist roster preserves depth.

### Work-type routing

PROOF maps classes of work to relevant role combinations. Routing connects the
panel to actual repository operations and avoids invoking every role.

## Common failure modes

### Diversity without conflict

The index lists architecture, documentation, security, and user roles, but no
role says what it pulls against. Reviews become additive checklists.

### Conflict words without role relationships

A role may discuss "speed versus safety" internally. That is not yet inter-role
tension. The panel should name which role owns each concern and how both
findings are handled.

### Universal reviewers

A role that owns correctness, security, usability, maintainability, and release
readiness has no useful boundary. Split it until each role can ask one hard
question another role might answer differently.

### Hierarchy without rationale

A numbered list of roles is not an adjudication policy unless the order says
what blocks, what advises, and why.

### Catalog without selection

Large catalogs make expertise discoverable but can make review impossible to
start. Define the active panel, routing rules, and a specialist retirement
policy.

### Synthetic agreement

Do not ask roles to produce one consensus paragraph. Report findings by role,
retain material dissent, and let the repository's adjudication rule govern the
decision.

## A tension maturity model

| Stage | Capability |
|---|---|
| 0. Presence | Multiple role names exist. |
| 1. Differentiation | Roles protect distinct obligations. |
| 2. Pairing | The index names pairwise tensions and explains why. |
| 3. Evidence | Each side identifies concrete evidence it inspects. |
| 4. Adjudication | Hard stops, review order, dissent, or experiments resolve decisions. |
| 5. Learning | Review outcomes change role boundaries, triggers, or evidence requirements. |

The 77-repository audit measures stages 0-4 structurally. Stage 5 requires
longitudinal usage evidence.

## Future research

A causal study should observe reviews rather than files alone. Useful measures
include:

- roles selected per change type;
- findings produced per selected role;
- findings that change a decision;
- disagreements preserved versus silently merged;
- escaped defects mapped to missing or unused roles;
- time required to select and apply a panel;
- roles never invoked during a release interval;
- role additions, merges, and retirements after incidents.

The central hypothesis is falsifiable: panels with explicit tension and
evidence contracts should identify more consequential tradeoffs per unit of
review effort than equally large catalogs of parallel personas.
