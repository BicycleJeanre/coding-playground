# `awk` Command Overview

`awk` is a text-processing tool for scanning input line by line, splitting each line into fields, and running actions when patterns match. It is especially useful for:

- extracting columns from structured text
- filtering rows
- reformatting output
- calculating sums, counts, and reports

## Basic Idea

`awk` reads input one record at a time. By default:

- each input line is one **record**
- whitespace separates **fields**
- `$1`, `$2`, `$3`, etc. refer to fields
- `$0` refers to the full current line

## Basic Syntax

```sh
awk 'pattern { action }' file
```

You can use:

- **pattern only**: print lines that match
- **action only**: run the action on every line
- **pattern + action**: run the action only for matching lines

## Common Forms

### Print every line

```sh
awk '{ print }' file
```

### Print the first column

```sh
awk '{ print $1 }' file
```

### Print lines matching a word

```sh
awk '/error/' logfile
```

### Print the first and third columns

```sh
awk '{ print $1, $3 }' file
```

### Use a custom field separator

For CSV-like input:

```sh
awk -F',' '{ print $1, $2 }' file.csv
```

## Patterns

Patterns decide **when** an action runs.

### Regex pattern

```sh
awk '/admin/ { print $1 }' users.txt
```

### Comparison pattern

```sh
awk '$3 > 100 { print $1, $3 }' sales.txt
```

### Equality check

```sh
awk '$2 == "ERROR" { print $0 }' app.log
```

### Line number conditions

```sh
awk 'NR == 1 { print }' file
```

`NR` is the current record number.

## Actions

Actions are blocks of code inside `{ ... }`.

Common action statements:

- `print` — output text or fields
- variable assignment — store values
- `if`, `else` — conditional logic
- `for`, `while` — loops

Example:

```sh
awk '{ total += $2 } END { print total }' prices.txt
```

This adds the second field from each line and prints the total at the end.

## Special Blocks

### `BEGIN`

Runs before input is read:

```sh
awk 'BEGIN { print "Report" } { print $1 }' file
```

### `END`

Runs after all input is processed:

```sh
awk '{ count++ } END { print count }' file
```

## Built-in Variables

Some commonly used built-ins:

| Variable | Meaning |
| --- | --- |
| `FS` | Input field separator |
| `OFS` | Output field separator |
| `NR` | Current line number across all input |
| `FNR` | Current line number in the current file |
| `NF` | Number of fields in the current line |
| `RS` | Input record separator |
| `ORS` | Output record separator |

Example:

```sh
awk 'BEGIN { OFS=" | " } { print $1, $2 }' file
```

## Common Usage Patterns

### 1. Filter rows

```sh
awk '$5 == "active"' users.txt
```

### 2. Extract columns

```sh
awk '{ print $2, $4 }' data.txt
```

### 3. Sum a column

```sh
awk '{ sum += $3 } END { print sum }' numbers.txt
```

### 4. Count matching rows

```sh
awk '/failed/ { count++ } END { print count }' test.log
```

### 5. Skip header row

```sh
awk 'NR > 1 { print $1, $2 }' file.csv
```

### 6. Print the last field

```sh
awk '{ print $NF }' file
```

## Passing Shell Variables into `awk`

Use `-v`:

```sh
name="alice"
awk -v user="$name" '$1 == user { print $0 }' users.txt
```

## Quoting Notes

The `awk` program is usually wrapped in single quotes:

```sh
awk '{ print $1 }' file
```

This prevents the shell from expanding `$1` before `awk` sees it.

## Running `awk` Without a File

You can pipe data into it:

```sh
ps aux | awk '/ssh/ { print $1, $2, $11 }'
```

Or:

```sh
echo "a b c" | awk '{ print $2 }'
```

## One-Liner vs Script File

For short commands, one-liners are common:

```sh
awk '$2 > 50 { print $1 }' scores.txt
```

For more complex logic, store the program in a file:

```awk
BEGIN { total = 0 }
{ total += $2 }
END { print total }
```

Run it with:

```sh
awk -f script.awk data.txt
```

## Practical Examples

### Show usernames from `/etc/passwd`

```sh
awk -F: '{ print $1 }' /etc/passwd
```

### Show processes using more than 10% CPU

```sh
ps aux | awk '$3 > 10 { print $1, $3, $11 }'
```

### Count non-empty lines

```sh
awk 'NF > 0 { count++ } END { print count }' file.txt
```

## Tips

- Start with `print` and a few fields to inspect data.
- Use `-F` when your input is not whitespace-separated.
- Use `NR`, `NF`, and `$NF` often; they are extremely handy.
- If the logic gets long, move it into a `.awk` script file.

## Summary

`awk` is best when you need lightweight, line-oriented data processing in the shell. The core mental model is:

1. read one line
2. split it into fields
3. match a pattern
4. run an action

If you remember `awk 'pattern { action }'`, `$1`, `$0`, `NF`, `NR`, `BEGIN`, and `END`, you can handle most common command-line text processing tasks.
