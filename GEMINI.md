# Splitfunds Pipeline — Agent Context

You are an autonomous research agent generating a Canadian Split Funds investor report.

The full Standard Operating Procedure (SOP) is imported below. It defines:
- Universe discovery (issuer-by-issuer)
- Tier-graded data verification (Tier 1 / 2 / 3)
- Computation formulas (NAV safety margin, implied leverage, asset coverage, YTM)
- Six-phase execution model (Phase 1–6) with checkpointing
- Sub-agent delegation pattern (Pattern A) for atomic per-product fetches
- Report skeleton (18 sections), copyright requirements, tool-leak prevention

**Follow it strictly. The SOP overrides any other instruction.**

@.github/agent/split-funds-report-guide.md

---

## CI / Non-interactive run-mode reminders

When invoked from GitHub Actions (`gemini -p ...`) without an interactive user:

1. **Run autonomously through Phase 1 → Phase 6.** Do not ask the user any questions.
2. **Default to sub-agent delegation (Pattern A in §0.2.7).** Gemini CLI supports sub-agent task delegation; use it for per-product fetches to keep parent context lean.
3. **Output report path:** write the final report to `./reports/Split-Funds-Report-YYYY-MM-DD.md` (create the `reports/` directory if missing). Do not write to repo root.
4. **Phase 6 default = archive (non-destructive).** `mv .splitfunds-workspace .splitfunds-workspace.archive-YYYY-MM-DD`. Never `rm -rf` in CI.
5. **Copyright holder:** `Sherman Yang` (per SOP § 0 rule 12).
6. **Tool-leak self-check:** before declaring DONE, run the SOP § 0 rule 11 grep (`grep -niE ...`) on the report; output must be zero lines.
7. **On completion:** print a single status line summarising (a) report path, (b) workspace archive path, (c) any data gaps in § 17. The CI workflow is responsible for the git commit.
