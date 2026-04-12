# Downtime Tracker Design

## 1. Overview

Downtime Tracker is a lightweight multi-plant tracking app for recording operational issues at industrial sites. It currently supports four categories of records per plant:

1. downtime events
2. breakdown incidents
3. critical spare part needs
4. observations

The current implementation is a simple prototype intended to be easy to run locally and easy to extend. It uses an Express server, a static browser UI, and a JSON file for persistence.

## 2. Goals

1. Keep setup simple for local use and demos.
2. Support multiple plants in one app.
3. Let users add records quickly with minimal UI.
4. Preserve data between restarts without requiring a database.

## 3. Current Architecture

### 3.1. Runtime

1. **Backend:** Node.js with Express
2. **Frontend:** static HTML, CSS, and vanilla JavaScript
3. **Persistence:** file-based JSON storage in `data/sample-data.json`

### 3.2. High-Level Flow

1. The Express server serves the static files from `public/`.
2. The browser loads the UI and requests plant data from `/api/plants`.
3. The user selects a plant or creates a new one.
4. The user submits a record form inside one of the four tabs.
5. The server appends the record to the selected plant in the JSON file.
6. The client reloads plant data and re-renders the view.

## 4. User Experience

### 4.1. Main Screen

The main page has three primary areas:

1. **Plant panel**
   1. plant selector dropdown
   2. add plant button
   3. selected plant summary showing name and location
   4. machinery management panel for adding/removing machinery items, with a predefined dropdown for common machinery types
2. **Tabbed records panel**
   1. Downtime
   2. Breakdowns
   3. Critical Spares
   4. Observations

### 4.2. User Actions

1. Add a plant by entering a name and location via browser prompts.
2. Switch between plants with the dropdown.
3. Add machinery items to the selected plant via the machinery panel or directly from the breakdowns form.
4. Remove machinery items from the plant.
5. View existing records for the selected plant.
6. Add a new record from the active tab.
7. When adding a breakdown, select the affected machinery from the plant's machinery list or add a new machinery item on the fly.

## 5. Data Model

### 5.1. Root Structure

```json
{
  "plants": []
}
```

### 5.2. Plant Structure

Each plant contains:

```json
{
  "id": "string",
  "name": "string",
  "location": "string",
  "machinery": ["string"],
  "downtime": [],
  "breakdowns": [],
  "spares": [],
  "observations": []
}
```

The `machinery` array stores user-defined machinery items for the plant.

### 5.3. Shared Record Fields

All records currently include:

1. `id`
2. `createdAt`
3. `note`
4. `details`

### 5.4. Record-Specific Fields

| Record type | Collection | Extra fi, `machinery`elds |
| --- | --- | --- |
| Downtime | `downtime` | `duration` |
| Breakdown | `breakdowns` | `system` |
| Spare | `spares` | `partNumber`, `priority` |
| Observation | `observations` | `severity` |

## 6. API Design

### 6.1. `GET /api/plants`

Returns the full list of plants, including all nested record arrays and machinery list.

### 6.2. `POST /api/plants`

Creates a new plant with:

1. generated `id`
2. provided `name`
3. provided `location`
4. empty `machinery` array
5. empty record collections

### 6.3. `POST /api/plants/:plantId/records`

Creates a record for a plant based on `type`.

Expected `type` values:

1. `downtime`
2. `breakdown`
3. `spare`
4. `observation`

The server rejects unknown types with `400 Invalid record type` and rejects unknown plants with `404 Plant not found`.

### 6.4. `POST /api/plants/:plantId/machinery`

Adds a new machinery item to a plant's machinery list.

Request body:
```json
{
  "name": "the machinery panel for the selected plant
4. renders each tab's list and form

### 7.2. Form Generation

Forms are built dynamically per tab. Each form always asks for a note and may ask for one or more type-specific field sets:

1. downtime: duration
2. breakdowns: system and machinery (dropdown populated from plant's machinery list)
Removes a machinery item from a plant's machinery list.

Returns the updated machinery array.

## 7. Frontend Behavior

### 7.1. Rendering

The client fetches all plants on load and after each successful write. It then:

1. repopulates the plant selector
2. chooses the current plant
3. renders each tab's list and form

### 7.2. Form Generation

Forms are built dynamically per tab. Each form always asks for a note and may ask for one extra type-specific field set:

1. downtime: duration
2. breakdowns: system
3. spares: part number and priority
4. observations: severity

### 7.3. Record Display

Each saved record is shown as:

1. note
2. created timestamp
3. one line of type-specific metadata

## 8. Persistence Strategy

The app uses synchronous file reads and writes against `data/sample-data.json`.

### 8.1. Benefits

1. very low setup overhead
2. easy to inspect and edit manually
3. convenient for prototyping and demos

### 8.2. Tradeoffs

1. no concurrency protection
2. no history or audit model
3. no filtering, pagination, or indexing
4. unsuitable for multi-user production use

## 9. Known Limitations

1. No authentication or authorization.
2. No edit or delete operations.
3. No server-side validation beyond basic record type checks.
4. No database or migration layer.
5. No distinction between demo data and user-created data.
6. Record IDs are timestamp-based and not guaranteed to be collision-safe in all environments.

## 10. Known Implementation Issues

### 10.1. Downtime Form Type Mismatch

The current frontend derives record `type` values with `type.slice(0, -1)`. This works for:

1. `breakdowns` -> `breakdown`
2. `spares` -> `spare`
3. `observations` -> `observation`

But it breaks for:

1. `downtime` -> `downtim`

As a result, downtime form submissions currently do not match the backend API contract and are rejected.

## 11. Extension Directions

1. Replace JSON file storage with a database.
2. Add edit and delete flows.
3. Add structured validation for plant and record inputs.
4. Improve plant creation UX beyond browser prompts.
5. Add search, filters, and reporting views.
