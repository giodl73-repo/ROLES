# `.roles` Conformity Report

This report records the local public-repo audit used to shape v0.1 of the `.roles` convention.

## Summary

All audited repos already use `.roles/ROLE.md`, so v0.1 preserves that as the only hard layout requirement. Existing repos differ in how rich their role files are, so the spec treats frontmatter and tier folders as recommended rather than mandatory.

| Repo | `.roles/ROLE.md` | Markdown files | Files with frontmatter | Notes |
| --- | ---: | ---: | ---: | --- |
| BISECT | yes | 17 | 16 | Mostly direct role files below `.roles`. |
| CERES | yes | 13 | 9 | Mixed metadata coverage. |
| CROP | yes | 14 | 13 | Uses recommended tier folders. |
| FLETCH | yes | 22 | 21 | Uses recommended tier folders. |
| ICELINES | yes | 13 | 11 | Rich direct role files below `.roles`. |
| LUCIA | yes | 210 | 203 | Large role set with broad metadata coverage. |
| PROOF | yes | 14 | 13 | Uses recommended tier folders. |
| ROUTE | yes | 33 | 32 | Uses recommended tier folders. |
| SIGNALS | yes | 206 | 206 | Large role set with complete frontmatter coverage. |
| TRACKER | yes | 13 | 12 | Uses recommended tier folders. |

## Conformity decision

v0.1 defines four levels:

1. Minimal: `.roles/ROLE.md` exists.
2. Indexed: the index links to role files.
3. Metadata: role files include `name`, `slug`, and `tier`.
4. Panel: role files are grouped and documented for review use.

This allows existing public repos to conform immediately at the Minimal level while giving maintainers a clear path toward richer metadata.
