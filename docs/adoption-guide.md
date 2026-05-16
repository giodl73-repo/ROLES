# `.roles` Adoption Guide

This guide helps you create `.roles` for any repository: software, research,
documentation, games, data, civic systems, art, operations, or AI-agent work.

The goal is not to copy a universal panel. The goal is to name the judgment
system your repo already needs and make it durable.

## The ten-minute path

1. Scaffold a starter panel:

   ```bash
   python tools/init_roles.py /path/to/repo --template starter
   ```

   Or create `.roles/ROLE.md` by hand.
2. Add one role that protects the repo's main promise.
3. Add one role that represents the user, reader, operator, or maintainer.
4. Add one role that checks communication: docs, naming, examples, onboarding.
5. Link those role files from `.roles/ROLE.md`.
6. Run the checker:

   ```bash
   python tools/check_roles.py /path/to/repo
   ```

You can stop there. That is a useful `.roles` panel.

## One-command templates

`tools/init_roles.py` can create starter panels for common repo shapes:

| Template | Use for |
|---|---|
| `starter` | any repo that wants a small general panel |
| `software-library` | reusable packages, APIs, crates, SDKs |
| `research` | papers, analyses, experiments, evidence repos |
| `creative` | games, stories, design labs, studios |
| `data-pipeline` | ETL, evidence packages, reproducible data workflows |
| `ai-agent` | agent workflows, skills, prompt contracts, assistant repos |

Example:

```bash
python tools/init_roles.py ../my-repo --template software-library
python tools/check_roles.py ../my-repo
```

The scaffolder will not overwrite existing files unless you pass `--force`.

## Copyable starter layout

```text
.roles/
  ROLE.md
  parliament/
    promise-steward.md
  editorial/
    public-guide-editor.md
  stakeholders/
    user-advocate.md
```

## Copyable `ROLE.md`

```markdown
# Repository Role Index

This repository uses `.roles` to make review expectations explicit.

## Parliament

| File | Role | Primary tension |
|---|---|---|
| `parliament/promise-steward.md` | Promise Steward | Ambition vs. the repo's actual public contract |

## Editorial

| File | Role | Primary tension |
|---|---|---|
| `editorial/public-guide-editor.md` | Public Guide Editor | Complete explanation vs. usable onboarding |

## Stakeholders

| File | Role | Primary tension |
|---|---|---|
| `stakeholders/user-advocate.md` | User Advocate | Builder intent vs. user experience |

## Review order

1. Use the Promise Steward when behavior, scope, or architecture changes.
2. Use the Public Guide Editor when README, docs, examples, or names change.
3. Use the User Advocate before releases or public-facing changes.
```

## Copyable role file

```markdown
---
name: Promise Steward
slug: promise-steward
tier: parliament
applies_to: [scope, architecture, release]
---

# Promise Steward

## Intellectual Disposition

This role protects the repo's public promise from drift.

## Key Question

*"Does this change make the repo more true to what it says it is?"*

## Lens - What to Verify

- The README promise still matches the implementation.
- New scope is intentional, not accidental.
- Tradeoffs are named where users or maintainers will feel them.
- Release notes and examples do not overclaim.
```

## Scenario recipes

Use these as starting points. Rename tiers when local language is clearer.

### Software library

```text
.roles/
  ROLE.md
  parliament/api-boundary-steward.md
  parliament/correctness-auditor.md
  stakeholders/downstream-maintainer.md
  editorial/examples-editor.md
```

Good questions:

- Is the public API stable and coherent?
- What can downstream users accidentally depend on?
- Do examples teach the safe path?

### CLI or developer tool

```text
.roles/
  ROLE.md
  parliament/contract-steward.md
  operations/release-operator.md
  stakeholders/first-run-user.md
  editorial/help-text-editor.md
```

Good questions:

- Does the command do what help text says?
- Are errors actionable?
- Can a new user succeed without private context?

### Data pipeline or evidence system

```text
.roles/
  ROLE.md
  parliament/provenance-auditor.md
  parliament/reproducibility-steward.md
  stakeholders/data-consumer.md
  operations/failure-mode-reviewer.md
```

Good questions:

- Can every output be traced to inputs?
- Are hashes, versions, and assumptions visible?
- What happens when a source is missing or stale?

### Research repo

```text
.roles/
  ROLE.md
  parliament/claim-auditor.md
  parliament/methodology-reviewer.md
  editorial/referee-editor.md
  stakeholders/reader-advocate.md
```

Good questions:

- Which claims are actually supported?
- Can a hostile reviewer reproduce the reasoning?
- Does the paper deliver what the abstract promises?

### Documentation or knowledge base

```text
.roles/
  ROLE.md
  parliament/reference-integrity-auditor.md
  editorial/learning-path-editor.md
  stakeholders/new-reader-advocate.md
```

Good questions:

- Is this accurate enough to rely on?
- Can a new reader find the right entry point?
- Are examples concrete enough to teach transfer?

### Game, story, or creative design repo

```text
.roles/
  ROLE.md
  parliament/safety-or-promise-steward.md
  craft/core-loop-editor.md
  playtest/player-experience-reviewer.md
  operations/runbook-reviewer.md
```

Good questions:

- What experience is the design promising?
- Where does the fun break?
- Can operators, facilitators, or playtesters run it repeatedly?

### Civic, legal, or public-interest system

```text
.roles/
  ROLE.md
  parliament/legal-boundary-reviewer.md
  parliament/evidence-auditor.md
  stakeholders/public-trust-reviewer.md
  editorial/plain-language-editor.md
```

Good questions:

- Does the system separate evidence from advocacy?
- Are legal or policy claims bounded?
- Can a public reader understand what is and is not being asserted?

### AI-agent workflow repo

```text
.roles/
  ROLE.md
  parliament/task-boundary-steward.md
  parliament/verification-auditor.md
  stakeholders/future-agent-operator.md
  editorial/prompt-contract-editor.md
```

Good questions:

- Does the agent know when to stop, ask, or verify?
- Are tool permissions and failure modes explicit?
- Can a future agent use the repo without hidden session memory?

## Naming roles

Good role names are specific enough to act:

| Weak | Stronger |
|---|---|
| Reviewer | API Boundary Steward |
| User | First-Run User Advocate |
| Docs | Public Guide Editor |
| Quality | Reproducibility Auditor |
| Safety | Egress and Override Steward |

Prefer a role that asks one hard question over a role that owns everything.

## What every role should contain

At minimum:

1. what it protects;
2. the hardest question it asks;
3. concrete evidence to inspect;
4. when to invoke it.

Optional but useful:

- frontmatter with `name`, `slug`, `tier`, and `applies_to`;
- tensions with other roles;
- examples of blocking vs. advisory findings;
- known failure modes.

## How to use `.roles` in reviews

1. Read `.roles/ROLE.md`.
2. Pick only the roles relevant to the change.
3. Review through each selected role separately.
4. Preserve disagreement. Do not average roles into one vague verdict.
5. Report findings with evidence and severity.
6. If the right role is missing, add that as a panel gap.

## Adoption checklist

| Check | Done |
|---|---|
| `.roles/ROLE.md` exists |  |
| At least one governance role exists |  |
| At least one stakeholder/audience role exists |  |
| At least one communication/docs role exists |  |
| Role files say what evidence to inspect |  |
| README links to ROLES or the local `.roles` index |  |
| Checker passes: `python tools/check_roles.py /path/to/repo` |  |

## When to grow the panel

Add a role when:

- a bug would have been caught by a distinct lens;
- reviews keep repeating the same concern;
- a stakeholder is being represented only from memory;
- an AI assistant needs a durable instruction that should live with the repo;
- a repo's public promise becomes more specific.

Do not add roles just to look complete. A small panel that gets used is better
than a large panel nobody invokes.
