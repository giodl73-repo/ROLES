# `.roles` Specification

**Status**: v0.1

`.roles` is a repository-root directory for human-readable review roles. A role is a repeatable lens used during design, implementation, documentation, release, or audit work.

## Required layout

```text
.roles/
  ROLE.md
```

`ROLE.md` is the index for the role system in that repository. It should explain:

- what the panel is for;
- when to use it;
- which role files are active;
- any local invocation or review order.

## Recommended layout

```text
.roles/
  ROLE.md
  parliament/
  editorial/
  stakeholders/
```

The three recommended tiers are:

| Tier | Purpose |
| --- | --- |
| `parliament` | Technical, architectural, data, safety, and verification lenses. |
| `editorial` | Writing, docs, pedagogy, naming, and public communication lenses. |
| `stakeholders` | User, operator, maintainer, policy, and adoption lenses. |

Repos may add other tiers when local names are clearer. A conforming `.roles` directory does not need to use the recommended tiers.

## Role files

Role files should be Markdown files below `.roles/`. `ROLE.md` is reserved for the panel index.

Recommended frontmatter:

```yaml
---
name: Boundary Reviewer
slug: boundary-reviewer
tier: parliament
applies_to: [architecture, interfaces]
---
```

Fields:

| Field | Required | Description |
| --- | --- | --- |
| `name` | Recommended | Human-readable role name. |
| `slug` | Recommended | Stable lowercase identifier, usually matching the file stem. |
| `tier` | Recommended | Local grouping such as `parliament`, `editorial`, or `stakeholders`. |
| `applies_to` | Optional | Short list of surfaces, tasks, or artifacts the role reviews. |
| `version` | Optional | Local role schema or role revision. |
| `scope` | Optional | Intended scope such as `project`, `repo`, `package`, or `docs`. |

Structured sections are intentionally flexible. Recommended headings:

- `Intellectual Disposition`
- `Key Question`
- `Lens - What to Verify`
- `Expertise`
- `Pulls Against` or `Tensions`

## Conformance levels

| Level | Requirements |
| --- | --- |
| Minimal | `.roles/ROLE.md` exists. |
| Indexed | Minimal plus links from `ROLE.md` to role files. |
| Metadata | Indexed plus frontmatter with `name`, `slug`, and `tier` on role files. |
| Panel | Metadata plus meaningful tier grouping and review instructions. |
| Assisted | Panel plus repo-local review and authoring skills that know how to use `.roles`. |

## Recommended skills

Repos that use automation assistants should add two local skills or equivalent commands:

| Skill | Purpose |
| --- | --- |
| `roles-review` | Read `.roles/ROLE.md`, select relevant role files, and review a change through those lenses. |
| `roles-author` | Create or update role files while preserving the repo's tier layout, naming, and frontmatter style. |

The skills should be local to each repo because the active panel, review order, and evidence requirements are repo-specific. See `docs/recommended-skills.md` for copyable skill contracts.

## Non-goals

`.roles` is not a package manager, workflow runner, or mandatory global role catalog. It is a portable repository convention. Tools may validate it, but the source of truth remains the Markdown in each repo.

## Compatibility rule

Existing repos with role files directly under `.roles/` are conforming when they include `.roles/ROLE.md`. Repos can migrate to tiers gradually.
