# Downtime Tracker Changelog

## 1. Rules

1. This document is append-only in practice for project history, but new entries should be inserted at the top of the log section.
2. Do not delete prior entries unless the user explicitly asks for that cleanup.
3. Each entry must have a stable change ID in the form `CHG-001`, `CHG-002`, and so on.
4. Each entry should include a timestamp, author, and concise summary.

## 2. Entry Format

1. **Change ID**
2. **Timestamp**
3. **Author**
4. **Summary**

Recommended line format:

`1. CHG-001 | 2026-04-12T11:31:17.455Z | Copilot | bootstrapped DESIGN.md with the current architecture, data model, API, UI flow, limitations, and the known downtime submission bug.`

## 3. Entries

1. CHG-004 | 2026-04-12T11:33:05.460Z | Copilot | bootstrapped `.github/copilot-instructions.md` and reformatted `DESIGN.md`, `BUGTRACKER.md`, and `CHANGELOG.md` into legal-style numbered structures.
2. CHG-003 | 2026-04-12T11:31:17.455Z | Copilot | bootstrapped `BUGTRACKER.md` with the initial bug tracking structure and `BUG-001` for the broken downtime form submission flow.
3. CHG-002 | 2026-04-12T11:31:17.455Z | Copilot | bootstrapped `DESIGN.md` with the current app architecture, data model, API, UI flow, limitations, and the known downtime submission bug.
4. CHG-001 | 2026-04-12T13:23:00Z | Jay | added the changelog and initial AI instructions for changelog updates.
