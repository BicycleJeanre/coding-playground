# Downtime Tracker Bug Tracker

## 1. Purpose

This document tracks known bugs in the current app.

## 2. Entry Format

Each bug entry should use the following numbered structure:

1. **ID**
2. **Title**
3. **Status**
4. **Severity**
5. **Summary**
6. **Reproduction**
7. **Expected**
8. **Actual**
9. **Files**
10. **Notes**

Bug IDs must use stable legal-style numbering in the form `BUG-001`, `BUG-002`, and so on.

## 3. Active Bugs

### 3.1. BUG-001 - Downtime submissions fail from the browser

1. **ID:** BUG-001
2. **Title:** Downtime submissions fail from the browser
3. **Status:** Open
4. **Severity:** High
5. **Summary:** The downtime form posts an invalid record type to the backend, so new downtime entries cannot be created from the UI.
6. **Reproduction:** Open the app, select a plant, go to the Downtime tab, fill in the form, and click Save.
7. **Expected:** The app should create a downtime record and show it in the downtime list.
8. **Actual:** The frontend sends `type: "downtim"` and the backend rejects it with `400 Invalid record type`.
9. **Files:** `public/app.js`, `server.js`
10. **Notes:** The issue comes from deriving the API type with `type.slice(0, -1)`, which works for plural tab names like `breakdowns` and `spares` but not for `downtime`.
