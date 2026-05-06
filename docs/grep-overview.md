# `grep` Command Overview

`grep` searches text for lines that match a pattern. It is one of the fastest ways to answer questions like:

- which files mention this word?
- where is this function used?
- which log lines contain an error?
- does this output include a specific value?

`grep` works with regular expressions by default, but it can also search for plain fixed strings.

## Basic Syntax

```sh
grep [options] pattern [file...]
```

The basic mental model is:

1. choose the pattern
2. choose where to search
3. add options for case, recursion, line numbers, or match style

## Common Forms

### Search one file

```sh
grep "error" app.log
```

### Search multiple files

```sh
grep "TODO" *.py
```

### Search recursively

```sh
grep -r "function_name" .
```

### Show line numbers

```sh
grep -n "error" app.log
```

### Case-insensitive search

```sh
grep -i "warning" app.log
```

### Show only matching filenames

```sh
grep -l "database" *.md
```

### Count matching lines

```sh
grep -c "failed" test.log
```

### Invert the match

```sh
grep -v "debug" app.log
```

`-v` prints lines that do not match the pattern.

## Useful Options

| Option | Meaning |
| --- | --- |
| `-n` | Show line numbers |
| `-i` | Ignore case |
| `-r` | Search recursively |
| `-l` | Print filenames with matches |
| `-L` | Print filenames without matches |
| `-c` | Count matching lines |
| `-v` | Invert match |
| `-w` | Match whole words |
| `-x` | Match the whole line |
| `-F` | Treat the pattern as a fixed string, not a regex |
| `-E` | Use extended regular expressions |
| `-A N` | Show N lines after each match |
| `-B N` | Show N lines before each match |
| `-C N` | Show N lines before and after each match |

## Regular Expressions

By default, `grep` uses basic regular expressions.

### Match any line containing a word

```sh
grep "admin" users.txt
```

### Match lines starting with text

```sh
grep "^ERROR" app.log
```

`^` means start of line.

### Match lines ending with text

```sh
grep "\.csv$" files.txt
```

`$` means end of line.

### Match one of several words

Use extended regex mode:

```sh
grep -E "error|failed|timeout" app.log
```

### Match digits

```sh
grep -E "[0-9]+" access.log
```

## Fixed-String Search

Use `-F` when you want the pattern treated literally:

```sh
grep -F "user.name" config.txt
```

This avoids regex interpretation of characters like `.`, `[`, `]`, `*`, and `?`.

`-F` is often the right choice when searching for exact snippets from config files, code, or logs.

## Recursive Code Search

### Search from the current directory

```sh
grep -rn "handleSubmit" .
```

### Search only matching filenames

```sh
grep -rl "handleSubmit" .
```

### Search one file type with shell globs

```sh
grep -rn "handleSubmit" --include="*.js" .
```

### Exclude a directory

```sh
grep -rn "handleSubmit" --exclude-dir=node_modules .
```

On macOS, the system `grep` is BSD `grep`; some GNU examples from Linux may not behave exactly the same.

## Searching Piped Output

`grep` is commonly used after another command:

```sh
ps aux | grep "python"
```

```sh
history | grep "git commit"
```

```sh
cat app.log | grep "ERROR"
```

The last example works, but this is cleaner:

```sh
grep "ERROR" app.log
```

## Context Around Matches

### Show lines after each match

```sh
grep -A 3 "Traceback" app.log
```

### Show lines before each match

```sh
grep -B 3 "Traceback" app.log
```

### Show lines before and after each match

```sh
grep -C 3 "Traceback" app.log
```

Context flags are useful when searching logs, stack traces, and config blocks.

## Whole Word and Whole Line Matching

### Match a whole word

```sh
grep -w "cat" words.txt
```

This matches `cat`, but not `concatenate`.

### Match a whole line

```sh
grep -x "enabled=true" config.txt
```

This only matches lines where the entire line is exactly `enabled=true`.

## Exit Status

`grep` sets an exit status:

| Status | Meaning |
| --- | --- |
| `0` | At least one match found |
| `1` | No matches found |
| `2` | Error |

This makes `grep` useful in scripts:

```sh
if grep -q "ready" status.txt; then
  echo "System is ready"
fi
```

`-q` means quiet mode: do not print matches, only return the status.

## Practical Examples

### Find TODOs in a project

```sh
grep -rn "TODO" .
```

### Find errors in a log

```sh
grep -i "error" app.log
```

### Find lines that are not comments

```sh
grep -v "^#" config.txt
```

### Find blank lines

```sh
grep "^$" file.txt
```

### Find non-blank lines

```sh
grep -v "^$" file.txt
```

### Search for an exact string containing regex characters

```sh
grep -F "db.host=localhost" app.properties
```

### Search logs with nearby context

```sh
grep -C 5 "connection refused" app.log
```

## `grep` vs `find` vs `awk`

| Tool | Best For |
| --- | --- |
| `grep` | Finding lines that match text or regex patterns |
| `find` | Finding files by name, type, size, age, or location |
| `awk` | Extracting fields, filtering rows, and building small reports |

Common combinations:

```sh
find . -type f -name "*.log" -exec grep -n "ERROR" {} \;
```

```sh
grep "ERROR" app.log | awk '{ print $1, $2 }'
```

## `grep` vs `rg`

`rg` means `ripgrep`. It is a modern search tool that is usually faster and more convenient for codebases:

```sh
rg "handleSubmit"
```

Useful differences:

| Tool | Notes |
| --- | --- |
| `grep` | Standard, available almost everywhere |
| `rg` | Faster for projects, respects `.gitignore`, good defaults |

Use `grep` when you need a portable command that works on most Unix-like systems. Use `rg` when searching source code in a local project.

## Common Mistakes

### Forgetting quotes

Use quotes around patterns:

```sh
grep "hello world" file.txt
```

Without quotes, the shell splits the pattern into separate arguments.

### Regex characters matching too much

This pattern treats `.` as any character:

```sh
grep "app.log" files.txt
```

For a literal dot, either escape it:

```sh
grep "app\.log" files.txt
```

Or use fixed-string mode:

```sh
grep -F "app.log" files.txt
```

### Searching binary or huge generated folders

Recursive `grep` can be noisy in generated directories. Exclude them:

```sh
grep -rn "token" --exclude-dir=node_modules --exclude-dir=.git .
```

## Summary

`grep` is best when you need to quickly find matching lines in files or command output. The core commands to remember are:

```sh
grep "pattern" file
grep -n "pattern" file
grep -i "pattern" file
grep -rn "pattern" .
grep -F "literal.string" file
grep -E "one|two" file
```

If you remember `grep -n`, `grep -i`, `grep -r`, `grep -v`, `grep -F`, and `grep -E`, you can handle most everyday text-search tasks.
