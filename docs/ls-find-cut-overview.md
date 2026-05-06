# `ls`, `find`, and `cut` Command Overview

These three commands are useful for different kinds of shell work:

- `ls` lists files and directories
- `find` searches for files and directories by name, type, age, size, and more
- `cut` extracts selected parts of each line, usually by character position or delimiter-separated field

Together, they cover a lot of day-to-day command-line inspection and data extraction.

## `ls`

`ls` shows directory contents.

### Basic Syntax

```sh
ls [options] [path]
```

### Common Forms

#### List the current directory

```sh
ls
```

#### Long listing format

```sh
ls -l
```

This shows details like:

- permissions
- owner
- group
- size
- modification time
- filename

#### Show hidden files

```sh
ls -a
```

#### Long format plus hidden files

```sh
ls -la
```

#### Human-readable sizes

```sh
ls -lh
```

#### Sort by modification time

```sh
ls -lt
```

#### Reverse sort order

```sh
ls -ltr
```

### Useful Options

| Option | Meaning |
| --- | --- |
| `-l` | Long format |
| `-a` | Include hidden files |
| `-h` | Human-readable sizes |
| `-t` | Sort by modified time |
| `-r` | Reverse sort |
| `-R` | Recursive listing |

### Practical Examples

#### Show all files in long format

```sh
ls -la
```

#### Show the newest files first

```sh
ls -lt
```

#### Show files under another directory

```sh
ls -lah /var/log
```

### When to Use `ls`

Use `ls` when you already know roughly where you are and just want to inspect a directory quickly.

## `find`

`find` searches directory trees recursively.

### Basic Syntax

```sh
find [path] [tests] [actions]
```

A very common mental model is:

1. choose where to search
2. add match conditions
3. decide what to do with matches

### Common Forms

#### Find everything under the current directory

```sh
find .
```

#### Find by exact name

```sh
find . -name "config.yaml"
```

#### Case-insensitive name search

```sh
find . -iname "readme*"
```

#### Find only directories

```sh
find . -type d
```

#### Find only files

```sh
find . -type f
```

#### Find by extension

```sh
find . -type f -name "*.log"
```

### Common Tests

| Test | Meaning |
| --- | --- |
| `-name "pattern"` | Match filename |
| `-iname "pattern"` | Case-insensitive filename match |
| `-type f` | Regular files only |
| `-type d` | Directories only |
| `-mtime -7` | Modified within the last 7 days |
| `-size +100M` | Larger than 100 MB |
| `-maxdepth N` | Limit recursion depth |

### Common Actions

#### Print matches

```sh
find . -name "*.txt" -print
```

#### Delete matches

```sh
find . -type f -name "*.tmp" -delete
```

Use `-delete` carefully.

#### Execute a command on matches

```sh
find . -type f -name "*.log" -exec ls -lh {} \;
```

`{}` is replaced by the current match.

### Practical Examples

#### Find shell scripts

```sh
find . -type f -name "*.sh"
```

#### Find large files

```sh
find . -type f -size +500M
```

#### Find files changed in the last day

```sh
find . -type f -mtime -1
```

#### Limit search depth

```sh
find . -maxdepth 2 -type f
```

### When to Use `find`

Use `find` when you need recursive searching or filtering by file attributes.

## `cut`

`cut` extracts columns or character ranges from each input line.

It works best with predictable, delimiter-based text.

### Basic Syntax

```sh
cut [options] [file]
```

The two most common modes are:

- **field mode** with `-d` and `-f`
- **character mode** with `-c`

### Field Mode

Use `-d` to define a delimiter and `-f` to choose fields.

#### Extract the first field from a colon-separated file

```sh
cut -d: -f1 /etc/passwd
```

#### Extract multiple fields

```sh
cut -d, -f1,3 file.csv
```

#### Extract a field range

```sh
cut -d, -f2-4 file.csv
```

### Character Mode

Use `-c` for character positions.

#### Extract the first 5 characters

```sh
cut -c1-5 file.txt
```

#### Extract specific character positions

```sh
cut -c1,3,8 file.txt
```

### Useful Options

| Option | Meaning |
| --- | --- |
| `-d` | Delimiter character |
| `-f` | Field list |
| `-c` | Character positions |
| `--complement` | Select everything except the chosen fields/chars |

### Practical Examples

#### Show usernames from `/etc/passwd`

```sh
cut -d: -f1 /etc/passwd
```

#### Show the first and third CSV columns

```sh
cut -d, -f1,3 data.csv
```

#### Extract a fixed-width code

```sh
cut -c1-8 codes.txt
```

### Limitations of `cut`

`cut` is simple and fast, but it has limits:

- it does not understand quoted CSV the way dedicated CSV tools do
- it is best for simple delimiters
- for more complex logic, `awk` is often a better fit

## Common Pipelines

These commands are often used together with pipes.

### List files and inspect output

```sh
ls -l | cut -c1-20
```

### Find files and pass them to another command

```sh
find . -type f -name "*.log"
```

### Extract usernames from `/etc/passwd`

```sh
cut -d: -f1 /etc/passwd
```

### Find matching files and show their names only

```sh
find . -type f -name "*.sh" | cut -d/ -f2-
```

## Tips

- Use `ls` for quick directory inspection.
- Use `find` when you need recursive search or attribute filtering.
- Use `cut` when the input structure is simple and delimiter-based.
- If you need richer text processing or conditions, move up to `awk`.

## Summary

The quickest way to think about them is:

- `ls` = what is in this directory?
- `find` = where are the files I want?
- `cut` = which part of each line do I want?

If you remember `ls -la`, `find . -type f -name "*.ext"`, and `cut -d: -f1`, you can handle many common shell tasks right away.
