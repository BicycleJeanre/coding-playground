# Downtime Tracker Copilot Instructions

## 1. Purpose

These instructions apply to all changes made in this repository.

## 2. Documentation Maintenance Requirements

1. Update `CHANGELOG.md` for every material repository change.
2. Update `BUGTRACKER.md` when:
   1. a new bug is discovered
   2. a bug is fixed
   3. bug status, severity, scope, or reproduction changes
3. Update `DESIGN.md` when:
   1. architecture changes
   2. API contracts change
   3. data structures change
   4. user flows or UI structure change
   5. notable limitations or extension directions change
4. Keep these documents aligned with the actual current implementation, not an aspirational future state unless explicitly labeled as planned work.

## 3. Numbering Requirements

1. Use legal-style numbered headings in project documentation where practical, for example `1.`, `1.1.`, and `1.1.1.`.
2. Use stable IDs for tracked records:
   1. bugs: `BUG-001`, `BUG-002`, ...
   2. changelog entries: `CHG-001`, `CHG-002`, ...
3. When adding a new bug or changelog entry, increment the highest existing ID instead of renumbering old entries.

## 4. Changelog Rules

1. Add new changelog entries at the top of the entries section.
2. Each changelog entry must include:
   1. change ID
   2. timestamp
   3. author
   4. concise summary
3. Do not remove old changelog entries unless explicitly instructed.

## 5. Bug Tracker Rules

1. Each bug entry must include the fields defined in `BUGTRACKER.md`.
2. If a fix is shipped, update the matching bug entry status instead of creating a duplicate replacement entry unless the user asks for a historical split.
3. If behavior changes reveal a new defect, add a new bug entry and cross-reference related files or earlier bug IDs in notes where useful.

## 6. Design Document Rules

1. Keep `DESIGN.md` focused on the implemented system.
2. Keep known limitations and known implementation issues current.
3. When a bug materially affects system behavior, make sure `DESIGN.md` and `BUGTRACKER.md` do not contradict each other.

## 7. Scope and Editing Discipline

1. Make precise updates instead of rewriting history unnecessarily.
2. Preserve existing IDs once created.
3. If a request changes code, check whether the documentation files above also need corresponding updates.
