# Recommended `.roles` Skills

Each repo that adopts `.roles` should provide two local assistant skills or equivalent commands: one for reviews and one for authoring. The skills should read the repo's own `.roles/ROLE.md` first and avoid importing roles from other repos unless the user explicitly asks.

## `roles-review`

**Purpose**: Review a change, plan, document, or release through the relevant `.roles` lenses.

Recommended contract:

```yaml
name: roles-review
description: Review work using this repository's .roles panel.
```

Recommended instructions:

1. Read `.roles/ROLE.md`.
2. Identify the role files relevant to the user's target, changed files, or review topic.
3. Read only those role files unless the index says the whole panel is required.
4. Produce findings grouped by role.
5. For every finding, cite the role lens and the concrete file, command, claim, or artifact being reviewed.
6. Do not invent missing roles. If the right role does not exist, note the gap separately.
7. Separate blocking issues from advisory suggestions.

Suggested output:

```text
Blocking findings
- [Role Name] Finding with evidence and required fix.

Advisory findings
- [Role Name] Improvement or risk.

Role coverage
- Used: role-a, role-b
- Missing: role-c, if any
```

## `roles-author`

**Purpose**: Create, split, rename, or update role files in the repo's `.roles` directory.

Recommended contract:

```yaml
name: roles-author
description: Author and maintain this repository's .roles files.
```

Recommended instructions:

1. Read `.roles/ROLE.md` and nearby role files to learn the local style.
2. Preserve the existing tier layout unless the user asks to reorganize it.
3. Use Markdown with frontmatter when the repo already uses frontmatter.
4. Prefer `name`, `slug`, `tier`, and `applies_to` frontmatter fields for new role files.
5. Include a clear disposition, key question, and verification lens.
6. Update `.roles/ROLE.md` whenever adding, removing, or renaming a role.
7. Keep roles actionable: each role should tell a reviewer what evidence to inspect.

Suggested role skeleton:

```markdown
---
name: Role Name
slug: role-name
tier: parliament
applies_to: [surface]
---

# Role Name

## Intellectual Disposition

Short statement of what this role protects.

## Key Question

*"The hardest question this role asks."*

## Lens - What to Verify

- Concrete check.
- Concrete check.
```

## Repo adoption checklist

For each repo:

1. Confirm `.roles/ROLE.md` is the panel index.
2. Add or update `roles-review` so reviews begin from `.roles/ROLE.md`.
3. Add or update `roles-author` so new roles follow local layout.
4. Run `python tools/check_roles.py <repo-root>` from this repository or an equivalent local check.
5. Document any repo-specific review order in `.roles/ROLE.md`.
