# Soya Personal Board

**Use AI to compare a personal choice from several perspectives and clarify benefits, risks and next steps.**

## Start without coding

A **Skill** is a package of instructions that helps an AI follow repeatable steps. A **prompt** is a message you can copy into an AI chat. Try the message below before installing anything.

1. Open the AI chat you normally use and start a new conversation.
2. Copy the complete message below and replace the bracketed example with information you are allowed to share.
3. Compare the reply with the expected result. Missing information should lead to questions, not invented facts.

```text
Compare this personal choice from three useful perspectives: [read one book this weekend or finish an introductory course]. List known facts and questions first, then benefits, costs and risks, followed by at most three next steps. Do not impersonate real people.
```

**Expected result:** Expect a comparison, missing information and up to three next steps. You make the decision.

Your AI service may charge fees and handles the text under its own policies. Do not paste work secrets, private contact details or passwords. If a reply is incomplete, name the missing part and add non-sensitive context. You can stop at any time.

The installation and developer sections below are optional for this first try. For questions, use the repository’s **Issues** tab, the public question area, and remove private/work information before posting.



Examine a personal question through complementary intellectual perspectives and produce a decision memo containing disagreements, risks and next actions. You make the decision.

[中文](README.md)

## Start without installation

```text
Use Soya Personal Board to examine this question: [a non-sensitive personal question].
Separate facts, preferences and unknowns. Choose three complementary perspectives;
give each view and its strongest objection. Summarize agreement, disagreement,
blind spots and up to three next actions. These are AI interpretations of public
ideas, not statements by real people. Invent no quotations or facts. I decide.
```

## Background and users

A single perspective can hide trade-offs. This project provides decision discussion, morning focus and reusable reflection-card Skills for people seeking structured reflection. It does not replace professional advice or guarantee faithful simulation of historical or living people.

## Install and use

Download the source. Choose a complete directory under `skills/`: `personal-board`, `soya-morning-meeting` or `soya-card-vault`. Give it to a Skills-capable host and use that host's current official installation mechanism. Back up any namesake directory, reopen a session and verify discovery. Do not run the old `install.sh`. The DSH preset is retained as compatibility material and has not been tested in the current host.

Say `Use $personal-board to examine: [question]`. Expect facts/unknowns, complementary views, disagreements and next actions. With Python 3, run `python3 skills/personal-board/scripts/decision_template.py --list` for the offline member/template utility; this does not call a model.

## Privacy, cost, recovery and status

Use only authorized material without work secrets, personal sensitive data or credentials. Model processing and retention follow the host/provider; local Markdown does not imply no external processing. Model credits are not included. Back up Skill directories and personal outputs before updating. Restore the old directory and reopen a session if needed; preserve private knowledge files. If discovery fails, check host support, directory nesting and SKILL.md, or use the prompt above.

This proposal restores source from commit `33cb83599a93724fb5ebc10dca9242b8c7b5ae99` after template overwrites. The offline member-list command was run; host installation, real workflows and publication remain unverified. See [review](OPEN_SOURCE_REVIEW.md) and [LICENSE](LICENSE).


[Maintenance and recovery](MAINTENANCE.md) · Public release acceptance remains pending.
