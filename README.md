# ROLES

**ROLES defines `.roles`: a portable, human-readable convention for putting a
repository's review panel inside the repository.**

This is a specification for a world where serious work is increasingly produced
by teams of humans and AI agents. The question is no longer just "what changed?"
It is "which durable judgment systems were present while the change was made?"
`.roles` gives that judgment system a place in version control.

Modern projects are reviewed through many lenses: architecture, security,
documentation, user experience, operations, safety, pedagogy, policy, creative
direction, and release readiness. Those lenses are often scattered across
private memory, issue comments, prompts, checklists, and reviewer habits.
`.roles` gives them a simple home.

A repo that adopts `.roles` keeps its review roles next to the work they govern.
Each role explains what it checks, when to invoke it, and what evidence it
expects. Humans can read it. AI assistants can follow it. Tooling can validate
it. The format is intentionally small enough to start with one Markdown file and
grow into a full review parliament over time.

ROLES is meant to be copied, forked, debated, and improved. Any public project
can adopt the convention without asking permission, installing a service, or
accepting a central authority.

## Official specification

The canonical `.roles` specification is [`SPEC.md`](SPEC.md). It defines the
required layout, recommended tiers, role-file metadata, conformance levels,
assistant-skill guidance, non-goals, and compatibility rule.

If you link to only one thing, link to the spec:
[`https://github.com/giodl73-repo/ROLES/blob/main/SPEC.md`](https://github.com/giodl73-repo/ROLES/blob/main/SPEC.md).

If you want to adopt `.roles` in a repo today, use
[`docs/adoption-guide.md`](docs/adoption-guide.md). It includes copyable
templates, scenario recipes, role prompts, and validation steps.

## Why `.roles` exists

`.roles` helps a repository answer:

- Who should review this kind of change?
- What question is each reviewer responsible for asking?
- What does good evidence look like?
- Which tradeoffs should be argued instead of silently averaged away?
- How can humans and AI assistants use the same local review contract?

The convention is not a global role catalog. It is repo-local by design: each
project writes the roles that match its own promises, risks, users, and style.

## Quick start

Create a `.roles` directory at the repository root:

```text
.roles/
  ROLE.md
  parliament/
    boundary-reviewer.md
  editorial/
    docs-editor.md
  stakeholders/
    user-advocate.md
```

`ROLE.md` is the entry point. It should explain what the local panel is for,
which roles exist, and when to use them.

Each role file is Markdown. Frontmatter is recommended for tooling, but the
human-readable role is the source of truth:

```markdown
---
name: Boundary Reviewer
slug: boundary-reviewer
tier: parliament
applies_to: [architecture, interfaces]
---

# Boundary Reviewer

## Intellectual Disposition

This role protects clean ownership boundaries.

## Key Question

*"Does this change make the boundary clearer or blur it?"*

## Lens - What to Verify

- Interfaces remain explicit.
- Consumers do not rely on hidden implementation details.
```

That is enough to start. A stronger panel usually adds:

- one governance role in `parliament/`;
- one communication role in `editorial/`;
- one user, operator, maintainer, or audience role in `stakeholders/`;
- any repo-native tiers the work actually needs.

See the [adoption guide](docs/adoption-guide.md) for ready-made starting panels
for software libraries, research repos, creative studios, games, civic systems,
data pipelines, infrastructure tools, documentation sites, and AI-agent
workflows.

## Recommended shape

ROLES recommends `parliament` as the governance tier: the place for roles that
decide whether a change is safe, coherent, shippable, or aligned with the repo's
public promise.

```text
.roles/
  ROLE.md
  parliament/    technical, safety, verification, release, boundary roles
  editorial/     writing, docs, naming, pedagogy, public communication roles
  stakeholders/  user, maintainer, operator, policy, adoption roles
```

These names are not a straitjacket. Creative and domain-heavy repos can add peer
tiers such as `studio`, `playtest`, `craft`, `voices`, `operations`, `research`,
or any local grouping that makes review clearer.

## Conformance levels

| Level | Meaning |
|---|---|
| Minimal | `.roles/ROLE.md` exists. |
| Indexed | `ROLE.md` links to role files. |
| Metadata | Role files include recommended frontmatter. |
| Panel | Roles are meaningfully grouped with review instructions. |
| Assisted | Repo-local assistant skills know how to author and review with `.roles`. |

A project can adopt the first level in minutes and improve over time.

## Tooling

Validate a repo's `.roles` directory with the dependency-free checker:

```bash
python tools/check_roles.py /path/to/repo
```

The checker is intentionally conservative. It catches missing entry points and
obvious drift, but it does not prescribe a single writing style.

## What belongs in this repo

- [`SPEC.md`](SPEC.md) defines the `.roles` convention.
- [`schemas/`](schemas/) contains optional JSON Schemas for tooling.
- [`tools/check_roles.py`](tools/check_roles.py) validates `.roles` directories.
- [`examples/`](examples/) shows minimal and panel-style layouts.
- [`docs/recommended-skills.md`](docs/recommended-skills.md) recommends
  repo-local assistant skills for review and authoring workflows.
- [`docs/conformity.md`](docs/conformity.md) records the current public-repo
  shape audit.

## Design principles

1. `.roles` is repository-local.
2. Markdown is the source format.
3. `ROLE.md` is the entry point.
4. Roles should be useful to humans first and automatable second.
5. Validators should report drift without flattening local voice.
6. Governance belongs somewhere explicit; `parliament` is the recommended name.
7. Creative and domain-specific review can use local tier names that fit the work.

## License

MIT. See [LICENSE](LICENSE).
