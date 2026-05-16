# ROLES

ROLES defines `.roles`: a small, portable directory convention for repository review panels.

A repository that uses `.roles` keeps its review lenses next to the code they govern. Each role explains what it checks, when to invoke it, and what kind of evidence it expects. The convention is intentionally lightweight so a repo can start with a few Markdown files and grow into richer panels over time.

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

`ROLE.md` is the index. Each role file is Markdown with optional frontmatter:

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

## What belongs here

- `SPEC.md` defines the `.roles` convention.
- `schemas/` contains optional JSON Schemas for tooling.
- `tools/check_roles.py` validates `.roles` directories without external dependencies.
- `examples/` shows minimal and panel-style layouts.
- `docs/recommended-skills.md` recommends repo-local skills for review and authoring workflows.
- `docs/conformity.md` records the current public-repo shape audit.

## Design principles

1. `.roles` is repository-local. Roles should name the checks that matter for that repo.
2. Markdown is the source format. Frontmatter is for tooling, not required for humans.
3. `ROLE.md` is the entry point. A reader should understand the panel without hunting.
4. The spec accepts both concise and richly structured roles.
5. Validators should report drift; they should not prescribe a single writing style.
