# Downtime Tracker Bug Tracker

## 1. Purpose

This document tracks known bugs in the current app.

## 2. Entry Format

Each bug entry should use the following Markdown table columns:

| ID | Title | Status | Severity | Summary | Reproduction | Expected | Actual | Files | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Bug IDs must use stable legal-style numbering in the form `BUG-001`, `BUG-002`, and so on.

## 3. Active Bugs

| ID | Title | Status | Severity | Summary | Reproduction | Expected | Actual | Files | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BUG-001 | Downtime submissions fail from the browser | Open | High | The downtime form posts an invalid record type to the backend, so new downtime entries cannot be created from the UI. | Open the app, select a plant, go to the Downtime tab, fill in the form, and click Save. | The app should create a downtime record and show it in the downtime list. | The frontend sends `type: "downtim"` and the backend rejects it with `400 Invalid record type`. | `public/app.js`, `server.js` | The issue comes from deriving the API type with `type.slice(0, -1)`, which works for plural tab names like `breakdowns` and `spares` but not for `downtime`. |
