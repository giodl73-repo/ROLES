#!/usr/bin/env python3
"""Scaffold a .roles panel with no third-party dependencies."""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Role:
    path: str
    name: str
    slug: str
    tier: str
    applies_to: tuple[str, ...]
    tension: str
    disposition: str
    question: str
    checks: tuple[str, ...]


TEMPLATES: dict[str, tuple[str, tuple[Role, ...]]] = {
    "starter": (
        "General-purpose repository review panel.",
        (
            Role(
                "parliament/promise-steward.md",
                "Promise Steward",
                "promise-steward",
                "parliament",
                ("scope", "architecture", "release"),
                "Ambition vs. the repo's actual public contract",
                "This role protects the repo's public promise from drift.",
                "Does this change make the repo more true to what it says it is?",
                (
                    "The README promise still matches the implementation.",
                    "New scope is intentional, not accidental.",
                    "Tradeoffs are named where users or maintainers will feel them.",
                ),
            ),
            Role(
                "editorial/public-guide-editor.md",
                "Public Guide Editor",
                "public-guide-editor",
                "editorial",
                ("readme", "docs", "examples", "onboarding"),
                "Complete explanation vs. usable onboarding",
                "This role protects first-contact clarity.",
                "Can a new reader understand what this repo is, why it matters, and how to begin?",
                (
                    "The README names the audience and purpose quickly.",
                    "Examples show the safe path before advanced options.",
                    "Public docs do not rely on private session context.",
                ),
            ),
            Role(
                "stakeholders/user-advocate.md",
                "User Advocate",
                "user-advocate",
                "stakeholders",
                ("users", "operators", "maintainers"),
                "Builder intent vs. user experience",
                "This role represents people who rely on the repo.",
                "What will a real user misunderstand, trip over, or need next?",
                (
                    "User-visible behavior is documented.",
                    "Errors and edge cases are actionable.",
                    "The change improves user trust rather than only internal elegance.",
                ),
            ),
        ),
    ),
    "software-library": (
        "Library or reusable package panel.",
        (
            Role(
                "parliament/api-boundary-steward.md",
                "API Boundary Steward",
                "api-boundary-steward",
                "parliament",
                ("api", "interfaces", "compatibility"),
                "Expressive API vs. stable downstream contract",
                "This role protects public interfaces from accidental churn.",
                "What can downstream users depend on, and is that dependency intentional?",
                (
                    "Public names, types, and errors remain coherent.",
                    "Breaking changes are explicit.",
                    "Implementation details do not leak into the contract.",
                ),
            ),
            Role(
                "parliament/correctness-auditor.md",
                "Correctness Auditor",
                "correctness-auditor",
                "parliament",
                ("algorithms", "tests", "edge-cases"),
                "Fast implementation vs. correct behavior",
                "This role looks for logic bugs and missing invariants.",
                "What input would make this code lie?",
                (
                    "Boundary cases are covered.",
                    "Tests exercise behavior, not only mocks.",
                    "Error paths are explicit and observable.",
                ),
            ),
            Role(
                "stakeholders/downstream-maintainer.md",
                "Downstream Maintainer",
                "downstream-maintainer",
                "stakeholders",
                ("migration", "docs", "release"),
                "Internal refactor vs. downstream adoption",
                "This role represents users who upgrade the library later.",
                "Can a maintainer adopt this change without reading the source?",
                (
                    "Migration notes exist for changed behavior.",
                    "Examples compile against the public API.",
                    "Versioning and compatibility expectations are clear.",
                ),
            ),
        ),
    ),
    "research": (
        "Research, paper, or analysis repo panel.",
        (
            Role(
                "parliament/claim-auditor.md",
                "Claim Auditor",
                "claim-auditor",
                "parliament",
                ("claims", "evidence", "abstract"),
                "Strong conclusions vs. supported evidence",
                "This role protects the boundary between evidence and assertion.",
                "Which claims would a hostile reviewer challenge first?",
                (
                    "Quantitative claims cite reproducible evidence.",
                    "Abstract and conclusions do not outrun results.",
                    "Limitations are visible where they affect interpretation.",
                ),
            ),
            Role(
                "parliament/methodology-reviewer.md",
                "Methodology Reviewer",
                "methodology-reviewer",
                "parliament",
                ("methods", "experiments", "replication"),
                "Elegant method vs. reproducible method",
                "This role checks whether the research procedure can be trusted.",
                "Could another researcher reproduce the result from the record?",
                (
                    "Inputs, parameters, and exclusions are documented.",
                    "Methods match the claims being made.",
                    "Negative or ambiguous results are not hidden.",
                ),
            ),
            Role(
                "editorial/referee-editor.md",
                "Referee Editor",
                "referee-editor",
                "editorial",
                ("paper", "review", "framing"),
                "Author intent vs. referee interpretation",
                "This role reads like a skeptical but fair reviewer.",
                "What would make a reviewer lose confidence?",
                (
                    "The contribution is stated plainly.",
                    "Terminology is consistent.",
                    "The paper answers the question it sets up.",
                ),
            ),
        ),
    ),
    "creative": (
        "Game, story, design, or creative studio panel.",
        (
            Role(
                "parliament/promise-steward.md",
                "Promise Steward",
                "promise-steward",
                "parliament",
                ("theme", "scope", "release"),
                "Creative ambition vs. deliverable promise",
                "This role protects the experience the project says it will deliver.",
                "What experience is being promised, and does the artifact create it?",
                (
                    "The design promise is specific.",
                    "New ideas support the core experience.",
                    "Risks to safety, trust, or feasibility are named.",
                ),
            ),
            Role(
                "craft/core-loop-editor.md",
                "Core Loop Editor",
                "core-loop-editor",
                "craft",
                ("mechanics", "flow", "iteration"),
                "Novel idea vs. repeatable fun",
                "This role protects the thing people actually do again and again.",
                "Where does the fun break?",
                (
                    "The core loop is visible.",
                    "Friction, boredom, and confusion are treated as design evidence.",
                    "Iteration notes improve the experience, not just the theme.",
                ),
            ),
            Role(
                "playtest/player-experience-reviewer.md",
                "Player Experience Reviewer",
                "player-experience-reviewer",
                "playtest",
                ("players", "audience", "feedback"),
                "Designer intent vs. player experience",
                "This role represents the player at the table, page, screen, or room.",
                "What does the participant actually feel, understand, and remember?",
                (
                    "Playtest evidence is concrete.",
                    "Audience assumptions are explicit.",
                    "Feedback changes the design when patterns repeat.",
                ),
            ),
        ),
    ),
    "data-pipeline": (
        "Data, evidence, or ETL pipeline panel.",
        (
            Role(
                "parliament/provenance-auditor.md",
                "Provenance Auditor",
                "provenance-auditor",
                "parliament",
                ("inputs", "outputs", "lineage"),
                "Useful output vs. traceable output",
                "This role protects source lineage.",
                "Can every output be traced back to its inputs and transformations?",
                (
                    "Input versions and sources are recorded.",
                    "Generated artifacts name their derivation path.",
                    "Manual edits and exclusions are visible.",
                ),
            ),
            Role(
                "parliament/reproducibility-steward.md",
                "Reproducibility Steward",
                "reproducibility-steward",
                "parliament",
                ("builds", "hashes", "runs"),
                "Convenience vs. repeatable evidence",
                "This role protects deterministic reruns.",
                "Could a future operator recreate this output?",
                (
                    "Parameters, hashes, and environment assumptions are recorded.",
                    "Failure modes are explicit.",
                    "Outputs distinguish source data from generated data.",
                ),
            ),
            Role(
                "operations/failure-mode-reviewer.md",
                "Failure Mode Reviewer",
                "failure-mode-reviewer",
                "operations",
                ("errors", "retries", "fallbacks"),
                "Happy path vs. operational reality",
                "This role looks at missing, stale, partial, and corrupt data.",
                "What happens when the source is wrong or unavailable?",
                (
                    "Retries and partial failures are observable.",
                    "Bad data does not become success-shaped output.",
                    "Operators know what to fix next.",
                ),
            ),
        ),
    ),
    "ai-agent": (
        "AI-agent workflow or assistant-driven repo panel.",
        (
            Role(
                "parliament/task-boundary-steward.md",
                "Task Boundary Steward",
                "task-boundary-steward",
                "parliament",
                ("scope", "tools", "autonomy"),
                "Agent initiative vs. task boundary",
                "This role protects the line between helpful autonomy and unsafe drift.",
                "Does the agent know when to act, ask, verify, or stop?",
                (
                    "Tool use is bounded by the task.",
                    "Ambiguous decisions have an ask path.",
                    "The workflow avoids hidden session-only knowledge.",
                ),
            ),
            Role(
                "parliament/verification-auditor.md",
                "Verification Auditor",
                "verification-auditor",
                "parliament",
                ("tests", "claims", "completion"),
                "Plausible answer vs. verified result",
                "This role checks whether the agent proved the outcome.",
                "What evidence shows the task is actually done?",
                (
                    "Claims cite files, commands, or artifacts.",
                    "Known failures are surfaced.",
                    "Completion criteria match the user's request.",
                ),
            ),
            Role(
                "editorial/prompt-contract-editor.md",
                "Prompt Contract Editor",
                "prompt-contract-editor",
                "editorial",
                ("prompts", "skills", "instructions"),
                "Rich instruction vs. executable contract",
                "This role makes prompts usable by future agents.",
                "Can a different agent follow this without private context?",
                (
                    "Instructions are ordered and testable.",
                    "Inputs and outputs are explicit.",
                    "Failure and escalation paths are named.",
                ),
            ),
        ),
    ),
}


def role_index(template_name: str, description: str, roles: tuple[Role, ...]) -> str:
    tiers: dict[str, list[Role]] = {}
    for role in roles:
        tiers.setdefault(role.tier, []).append(role)

    lines = [
        "# Repository Role Index",
        "",
        f"This repository uses `.roles` for {description.lower()}",
        "",
    ]
    for tier, tier_roles in tiers.items():
        lines.extend(
            [
                f"## {tier.replace('-', ' ').title()}",
                "",
                "| File | Role | Primary tension |",
                "|---|---|---|",
            ]
        )
        for role in tier_roles:
            lines.append(f"| `{role.path}` | {role.name} | {role.tension} |")
        lines.append("")

    lines.extend(
        [
            "## Review order",
            "",
            "1. Read this index before selecting roles.",
            "2. Use only the roles relevant to the change unless the user asks for a full-panel review.",
            "3. Report findings by role and cite concrete evidence.",
            "",
            f"Template: `{template_name}`.",
        ]
    )
    return "\n".join(lines) + "\n"


def role_markdown(role: Role) -> str:
    applies_to = ", ".join(role.applies_to)
    checks = "\n".join(f"- {check}" for check in role.checks)
    return f"""---
name: {role.name}
slug: {role.slug}
tier: {role.tier}
applies_to: [{applies_to}]
---

# {role.name}

## Intellectual Disposition

{role.disposition}

## Key Question

*"{role.question}"*

## Lens - What to Verify

{checks}
"""


def write_file(path: Path, content: str, force: bool) -> str:
    if path.exists() and not force:
        return f"SKIP {path}"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")
    return f"WRITE {path}"


def scaffold(root: Path, template_name: str, force: bool) -> list[str]:
    if template_name not in TEMPLATES:
        choices = ", ".join(sorted(TEMPLATES))
        raise ValueError(f"unknown template '{template_name}'. Choices: {choices}")

    description, roles = TEMPLATES[template_name]
    roles_dir = root / ".roles"
    actions = [
        write_file(roles_dir / "ROLE.md", role_index(template_name, description, roles), force)
    ]
    for role in roles:
        actions.append(write_file(roles_dir / role.path, role_markdown(role), force))
    return actions


def main() -> int:
    parser = argparse.ArgumentParser(description="Scaffold a .roles panel")
    parser.add_argument("repo_root", type=Path, help="repository root to update")
    parser.add_argument(
        "--template",
        choices=sorted(TEMPLATES),
        default="starter",
        help="starter panel to create",
    )
    parser.add_argument("--force", action="store_true", help="overwrite existing role files")
    args = parser.parse_args()

    root = args.repo_root.resolve()
    if not root.exists():
        print(f"ERROR {root} does not exist", file=sys.stderr)
        return 1
    if not root.is_dir():
        print(f"ERROR {root} is not a directory", file=sys.stderr)
        return 1

    for action in scaffold(root, args.template, args.force):
        print(action)
    return 0


if __name__ == "__main__":
    sys.exit(main())
