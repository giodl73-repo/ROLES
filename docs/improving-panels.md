# Improving a `.roles` Panel

This guide turns recurring findings from a 77-repository audit into small,
reviewable improvements. Start from the repository's current panel. Do not
replace local language merely to match a template.

## Diagnose the current stage

| Current shape | Main risk | First repair |
|---|---|---|
| No `.roles` directory | Review judgment remains private or ephemeral | Add `.roles/ROLE.md` and three focused roles |
| `ROLE.md` only | Adoption is visible but no lens is usable | Add promise, stakeholder, and communication roles |
| Role files without `ROLE.md` | Reviewers cannot discover the panel | Add the required index and link every active role |
| Index without links | Names are visible but navigation and automation drift | Link every active role with a relative Markdown path |
| Generic personas | Roles sound different but inspect the same vague concept | Name local artifacts, risks, and failure modes |
| Diverse roles without tension | Valid concerns are silently averaged | Add pairwise tensions and an adjudication rule |
| More than 40 roles | Selection cost overwhelms review | Separate an active core from the specialist roster |

## The minimum useful panel

Start with three roles:

1. **Promise Steward** protects the repository's public contract.
2. **Stakeholder Advocate** represents a user, reader, operator, maintainer, or
   affected community.
3. **Communication Editor** checks docs, naming, examples, and onboarding.

This is a starting point, not a universal catalog. Rename each role to fit the
repository and replace generic checks with local evidence.

## Make the index operational

An index should let a reviewer select and apply roles without searching the
directory.

```markdown
# Repository Review Panel

## Active Panel

| Role | Protects | Invoke when |
|---|---|---|
| Contract Steward (`parliament/contract-steward.md`) | Public API stability | APIs, schemas, or compatibility change |
| First-Run User (`stakeholders/first-run-user.md`) | Successful onboarding | Commands, defaults, or docs change |
| Release Operator (`operations/release-operator.md`) | Safe deployment and recovery | Packaging or release automation changes |
```

Link every active role. If a file is intentionally a template, historical role,
or optional specialist, label it separately.

## Ground roles in repository evidence

Replace broad statements:

> Check whether the implementation is high quality.

With checks that can fail:

> Run `tests/compatibility/` against the previous schema fixture. Confirm that
> `examples/minimal.toml` still parses and that the migration report names every
> dropped field.

Useful grounding includes:

- exact files or directories;
- commands and expected outcomes;
- schemas, fixtures, datasets, and retained evidence;
- public promises from the README or specification;
- known failure modes and incidents;
- downstream consumers and compatibility boundaries.

Do not require every role to repeat the repository name. Require every role to
know what evidence belongs to this repository.

## Add productive tension

Put a compact tension table in `.roles/ROLE.md`:

```markdown
## Core Tensions

| Pulls | Against | Because |
|---|---|---|
| Contract Steward | First-Run User | Explicit state protects compatibility but can increase setup work. |
| Release Operator | Contract Steward | A reversible rollout may require temporary compatibility surface. |
```

Then add an adjudication rule:

```markdown
## Review Order

1. Correctness, safety, legal, and data-integrity failures block.
2. Compatibility findings require a migration plan or explicit breaking release.
3. Usability and communication findings remain visible even when advisory.
4. If evidence can resolve a disagreement, define the experiment before deciding.
```

The goal is not forced conflict. It is preventing one valid obligation from
disappearing when another is optimized.

## Make each role actionable

Every role should answer four questions:

1. What does this role protect?
2. What is the hardest question it asks?
3. What concrete evidence does it inspect?
4. When should a reviewer invoke it?

Recommended extension:

```markdown
## Finding Contract

- Blocking: invariant failure, unsupported claim, unsafe behavior, or broken public contract.
- Advisory: improvement that does not invalidate the change.
- Evidence: cite a file, command, test result, dataset, claim, or observed behavior.
```

This keeps roles from becoming prose-only personas.

## Curate large catalogs

A specialist catalog can be valuable. It should not be the default panel.

```text
.roles/
  ROLE.md                 active panel and routing rules
  parliament/             default governance roles
  stakeholders/           default affected-party roles
  specialists/            invoked by domain or change type
  retired/                optional history, excluded from active review
```

For catalogs above roughly 40 roles:

1. Name 5-12 active roles in `ROLE.md`.
2. Group specialists by the artifact or decision they review.
3. Add a routing table from work type to specialists.
4. Record when a specialist was last invoked.
5. Merge roles that protect the same obligation with the same evidence.
6. Retire roles that have no distinct question or invocation trigger.

The objective is not a smaller directory. It is a smaller default decision
surface.

## Improvement sequence

Use this order to avoid polishing a panel that is not operable:

1. Restore `.roles/ROLE.md`.
2. Add or identify the active roles.
3. Link every active role.
4. Add recommended frontmatter.
5. Ground each role in concrete evidence.
6. Cover materially different failure concerns.
7. Name pairwise tensions.
8. State review order or adjudication.
9. Add repo-local review and authoring skills.
10. Observe role use and revise the panel.

## Review the panel itself

At release boundaries or after a consequential failure, ask:

- Which role would have caught this?
- Was that role selected?
- Did it inspect the right evidence?
- Did another role's concern override it silently?
- Is a new role needed, or should an existing role become more specific?
- Which roles have not been invoked and why?

Add a role only when it protects a distinct obligation. Prefer improving,
splitting, merging, or retiring existing roles over growing the catalog by
default.

## Validate

Run the ROLES checker:

```bash
python tools/check_roles.py /path/to/repository
```

The checker validates conservative structural rules. A passing result does not
prove that a panel is grounded, diverse, tense, actionable, or maintained. Use
the questions in this guide for that review.
