# Developer Quick Reference

---

## VSCode

### Shortcuts

#### Copilot

| Shortcut         | Description               |
| ---------------- | ------------------------- |
| `ctrl + cmd + i` | Move to chat and activate |
| `cmd + enter`    | Allow chat                |

#### Terminal

| Shortcut                  | Description                |
| ------------------------- | -------------------------- |
| `ctrl + \``               | Toggle terminal            |
| `ctrl + shift + \``       | New terminal               |
| `ctrl + 1`                | Focus editor               |
| `ctrl + tab`              | Cycle focus                |
| `ctrl + pagedown`         | Next terminal instance     |
| `ctrl + pageup`           | Previous terminal instance |
| `ctrl + shift + w`        | Kill terminal              |
| `ctrl + shift + 5`        | Split terminal             |
| `ctrl + alt + right/left` | Focus next/prev split pane |
| `ctrl + alt + up/down`    | Focus up/down split pane   |
| `ctrl + k`                | Clear terminal             |
| `ctrl + c`                | Interrupt (SIGINT)         |
| `shift + pageup/pagedown` | Scroll terminal            |
| `ctrl + f`                | Find in terminal           |
| `ctrl + shift + c`        | Copy in terminal           |
| `ctrl + shift + v`        | Paste in terminal          |

#### Copilot & Shell (zsh/bash)

| Shortcut         | Description               |     | Shortcut    | Description             |
| ---------------- | ------------------------- | --- | ----------- | ----------------------- |
| `ctrl + cmd + i` | Move to chat and activate |     | `↑` / `↓`   | Previous / next command |
| `cmd + enter`    | Allow chat                |     | `ctrl + r`  | Reverse history search  |
|                  |                           |     | `alt + b/f` | Move by word            |
|                  |                           |     | `ctrl + w`  | Delete word             |

---

## Neovim

### Vim Motions Reference

#### Modes

| Mode         | Enter           | Description                          |
| ------------ | --------------- | ------------------------------------ |
| Normal       | `Esc`           | Default mode — navigation & commands |
| Insert       | `i` / `a` / `o` | Type text                            |
| Visual       | `v`             | Character selection                  |
| Visual Line  | `V`             | Line selection                       |
| Visual Block | `<C-v>`         | Column/block selection               |
| Command      | `:`             | Ex commands                          |
| Replace      | `R`             | Overwrite text                       |

#### Horizontal Movement

| Key       | Description                         |
| --------- | ----------------------------------- |
| `h` / `l` | Left / right one character          |
| `w`       | Next word start                     |
| `W`       | Next WORD start (space-delimited)   |
| `b`       | Previous word start                 |
| `B`       | Previous WORD start                 |
| `e`       | Next word end                       |
| `E`       | Next WORD end                       |
| `0`       | Start of line                       |
| `^`       | First non-blank character           |
| `$`       | End of line                         |
| `g_`      | Last non-blank character            |
| `f{c}`    | Jump to next occurrence of char `c` |
| `F{c}`    | Jump to prev occurrence of char `c` |
| `t{c}`    | Jump to just before next char `c`   |
| `T{c}`    | Jump to just after prev char `c`    |
| `;`       | Repeat last `f/F/t/T` forward       |
| `,`       | Repeat last `f/F/t/T` backward      |

#### Vertical Movement & Jump List

| Key       | Description              |     | Key     | Description               |
| --------- | ------------------------ | --- | ------- | ------------------------- |
| `j` / `k` | Down / up one line       |     | `<C-o>` | Jump back in jump list    |
| `{N}j`    | Down N lines (e.g. `5j`) |     | `<C-i>` | Jump forward in jump list |
| `gg`      | Go to top of file        |     | `H`     | Top of screen             |
| `G`       | Go to bottom of file     |     | `M`     | Middle of screen          |
| `{N}G`    | Go to line N             |     | `L`     | Bottom of screen          |
| `{` / `}` | Prev / next blank line   |     | `zz`    | Center screen on cursor   |
| `<C-d>`   | Half page down           |     | `zt`    | Scroll cursor to top      |
| `<C-u>`   | Half page up             |     | `zb`    | Scroll cursor to bottom   |
| `<C-f>`   | Full page down           |     |         |                           |
| `<C-b>`   | Full page up             |     |         |                           |

#### Operators

Operators follow the pattern: `{operator}{motion}` or `{operator}{text-object}`

| Operator | Description                     |
| -------- | ------------------------------- |
| `d`      | Delete                          |
| `c`      | Change (delete + enter insert)  |
| `y`      | Yank (copy)                     |
| `p`      | Paste after                     |
| `P`      | Paste before                    |
| `=`      | Auto-indent                     |
| `>`      | Indent right                    |
| `<`      | Indent left                     |
| `gU`     | Uppercase                       |
| `gu`     | Lowercase                       |
| `g~`     | Toggle case                     |
| `!`      | Filter through external command |

Examples: `dw` → delete word · `ciw` → change word · `yip` → yank paragraph · `>ap` → indent paragraph

#### Insert Mode Entry & Normal Mode Editing

| Key  | Description                   |     | Key     | Description                    |
| ---- | ----------------------------- | --- | ------- | ------------------------------ |
| `i`  | Insert before cursor          |     | `x`     | Delete character under cursor  |
| `I`  | Insert at start of line       |     | `X`     | Delete character before cursor |
| `a`  | Insert after cursor           |     | `dd`    | Delete line                    |
| `A`  | Insert at end of line         |     | `D`     | Delete to end of line          |
| `o`  | New line below, enter insert  |     | `yy`    | Yank line                      |
| `O`  | New line above, enter insert  |     | `u`     | Undo                           |
| `s`  | Delete char and insert        |     | `<C-r>` | Redo                           |
| `S`  | Delete line and insert        |     | `.`     | Repeat last change             |
| `C`  | Delete to end of line, insert |     | `r{c}`  | Replace character with `c`     |
| `cc` | Delete entire line and insert |     | `J`     | Join line below to current     |
|      |                               |     | `gJ`    | Join line below (no space)     |
|      |                               |     | `>>`    | Indent line right              |
|      |                               |     | `<<`    | Indent line left               |

#### Search & Replace

| Key               | Description                    |
| ----------------- | ------------------------------ |
| `/pattern`        | Search forward                 |
| `?pattern`        | Search backward                |
| `n`               | Next match                     |
| `N`               | Previous match                 |
| `*`               | Search word under cursor (fwd) |
| `#`               | Search word under cursor (bwd) |
| `:%s/old/new/g`   | Replace all in file            |
| `:%s/old/new/gc`  | Replace all with confirmation  |
| `:s/old/new/g`    | Replace all on current line    |
| `{v}:s/old/new/g` | Replace in visual selection    |

#### Macros & Registers

| Key       | Description                    |
| --------- | ------------------------------ |
| `q{a}`    | Record macro into register `a` |
| `q`       | Stop recording                 |
| `@{a}`    | Play macro from register `a`   |
| `@@`      | Repeat last macro              |
| `{N}@{a}` | Play macro N times             |
| `"{a}y`   | Yank into register `a`         |
| `"{a}p`   | Paste from register `a`        |
| `:reg`    | View all registers             |

#### Visual Mode

| Key             | Description                    |
| --------------- | ------------------------------ |
| `v`             | Visual (character)             |
| `V`             | Visual line                    |
| `<C-v>`         | Visual block                   |
| `o`             | Move to other end of selection |
| `gv`            | Reselect last visual selection |
| `u`             | Lowercase selection            |
| `U`             | Uppercase selection            |
| `d` / `y` / `c` | Delete / yank / change         |
| `>` / `<`       | Indent / unindent              |
| `gc`            | Toggle comment on selection    |

#### Window & Split Management

| Key            | Description           |
| -------------- | --------------------- |
| `:sp`          | Horizontal split      |
| `:vsp`         | Vertical split        |
| `<C-w>h/j/k/l` | Move between splits   |
| `<C-w>w`       | Cycle through splits  |
| `<C-w>=`       | Equalize split sizes  |
| `<C-w>+` / `-` | Resize height         |
| `<C-w>>` / `<` | Resize width          |
| `<C-w>q`       | Close split           |
| `<C-w>T`       | Move split to new tab |

### LazyVim Shortcuts

#### UI/UX & Buffer Management

| Shortcut     | Description              |     | Shortcut                | Description          |
| ------------ | ------------------------ | --- | ----------------------- | -------------------- |
| `<leader>uC` | Colorscheme with preview |     | `<leader>fb`            | List open buffers    |
| `<leader>uD` | Code block dimming       |     | `<Shift>l` / `<Shift>h` | Next/Prev buffer     |
| `<leader>ul` | Toggle line number       |     | `]b` or `[b`            | Next/Prev buffer     |
| `<leader>uL` | Toggle relative number   |     | `<leader>bd`            | Close current buffer |
| `<leader>uw` | Toggle word wrap         |     | `<C-w>v`                | Split vertical       |
| `<C-/>`      | Toggle Terminal window   |     | `<C-w>s`                | Split horizontal     |
| `:Neotree`   | Neotree file explorer    |     | `<C-w>h/j/k/l`          | Navigate splits      |

#### Text Objects (Select) & Editing with Text Objects

| Shortcut | Description               |     | Shortcut | Description                 |
| -------- | ------------------------- | --- | -------- | --------------------------- |
| `viw`    | Select inner word         |     | `ciw`    | Change inner word           |
| `vi"`    | Select inner quotes       |     | `ci"`    | Change inner quotes         |
| `vi{`    | Select inner curly braces |     | `ci{`    | Change inner curly braces   |
| `vip`    | Select inner paragraph    |     | `cip`    | Change inner paragraph      |
| `va[`    | Select around [] braces   |     | `ca(`    | Change around parentheses   |
| `dap`    | Delete around paragraph   |     | `di"`    | Delete inner quotes         |
|          |                           |     | `dip`    | Delete inner paragraph      |
|          |                           |     | `yip`    | Yank inner paragraph        |
|          |                           |     | `yiw`    | Yank inner word             |
|          |                           |     | `=ip`    | Auto-indent inner paragraph |
|          |                           |     | `gU iw`  | Uppercase inner word        |
|          |                           |     | `gu iw`  | Lowercase inner word        |
|          |                           |     | `g~ iw`  | Toggle case inner word      |

#### Commenting

| Shortcut      | Description                                      |
| ------------- | ------------------------------------------------ |
| `gcc`         | Toggle comment on current line                   |
| `gc{motion}`  | Toggle comment over motion (e.g. `gcip`, `gc3j`) |
| `gc` (visual) | Toggle comment on visual selection               |
| `gcip`        | Toggle comment on inner paragraph                |
| `gc3j`        | Toggle comment on current + 3 lines below        |
| `gco`         | Add comment below current line                   |
| `gcO`         | Add comment above current line                   |
| `gcA`         | Add inline comment at end of line                |

> `gc` is provided by `mini.comment` (LazyVim default) or `Comment.nvim`

#### Code Folding & Marks

| Shortcut     | Description                   |     | Shortcut        | Description                        |
| ------------ | ----------------------------- | --- | --------------- | ---------------------------------- |
| `zR` or `zi` | Open all folds                |     | `<leader>sm`    | View all marks                     |
| `zM`         | Close all folds               |     | `m[a-z]`        | Set local mark                     |
| `za`         | Toggle fold                   |     | `'[a-z]`        | Jump to mark                       |
| `zA`         | Toggle all folds under cursor |     | `` `[a-z] ``    | Jump to exact position             |
| `zc`         | Close fold                    |     | `' '`           | Jump to last position              |
| `zo`         | Open fold                     |     | `:delmarks a-z` | Delete lowercase marks             |
| `zO`         | Open all folds under cursor   |     | `:delmarks ax`  | Delete specific marks (a and x)    |
|              |                               |     | `:delmarks!`    | Delete all marks (except A-Z, 0-9) |

#### Functions & Symbols (LSP)

| Shortcut     | Description               |
| ------------ | ------------------------- |
| `:LspInfo`   | Show attached LSP info    |
| `<leader>cs` | Document symbols          |
| `gr`         | Find all references       |
| `gd`         | Go to definition          |
| `gD`         | Go to declaration         |
| `gy`         | Goto Type definition      |
| `K`          | Show docstring/type hints |
| `[[` or `]]` | Prev/Next reference       |

#### Diagnostics, Code Actions & Indentation

| Shortcut     | Description           |     | Shortcut     | Description    |     | Shortcut | Description              |
| ------------ | --------------------- | --- | ------------ | -------------- | --- | -------- | ------------------------ |
| `]d`         | Next diagnostic       |     | `<leader>cr` | Rename symbols |     | `>`      | Indent right             |
| `[d`         | Prev diagnostic       |     | `<leader>cf` | Format code    |     | `<`      | Indent left              |
| `<leader>sd` | Document diagnostics  |     | `<leader>ca` | Code actions   |     | `=ip`    | Indent current paragraph |
| `<leader>sD` | Workspace diagnostics |     |              |                |     | `gg=G`   | Auto-indent entire file  |

#### Search & Git (fzf-lua)

| Shortcut     | Description              |     | Shortcut     | Description             |
| ------------ | ------------------------ | --- | ------------ | ----------------------- |
| `<leader>sr` | Search and Replace       |     | `<leader>gc` | Commit log texts search |
| `<leader>fc` | Find Config files        |     | `<leader>gs` | Status (file search)    |
| `<leader>ff` | Find files (Root dir)    |     | `<leader>ge` | Git explorer (Neotree)  |
| `<leader>/`  | Grep (Root dir)          |     | `<leader>gf` | Current file history    |
| `<leader>sG` | Grep (CWD)               |     |              |                         |
| `<leader>ss` | Symbol search            |     |              |                         |
| `<leader>sc` | Command history          |     |              |                         |
| `<leader>sw` | Search word under cursor |     |              |                         |
| `<leader>sk` | Search all keymaps       |     |              |                         |
| `<leader>st` | Search TODO/WARNING      |     |              |                         |

#### LazyGit

| Shortcut     | Description            |
| ------------ | ---------------------- |
| `<leader>gg` | Open LazyGit window    |
| `<C-r>`      | Switch to recent repo  |
| `<C-b>`      | Filter files by status |
| `p`          | Git pull               |
| `P`          | Git push               |
| `<space>`    | Stage                  |
| `a`          | Stage all              |
| `c`          | Commit                 |
| `s`          | Stash                  |
| `z`          | Undo                   |
| `<C-z>`      | Redo                   |
| `i`          | Add to .gitignore      |
| `q`          | Quit                   |

---

## Qutebrowser

### Navigation & Searching

| Shortcut | Description                 |     | Shortcut | Description                   |
| -------- | --------------------------- | --- | -------- | ----------------------------- |
| `j`      | Scroll down                 |     | `/`      | Search on page                |
| `k`      | Scroll up                   |     | `?`      | Search backwards on page      |
| `h`      | Scroll left                 |     | `n`      | Next search result            |
| `l`      | Scroll right                |     | `N`      | Previous search result        |
| `gg`     | Go to top of page           |     | `*`      | Search for selected text      |
| `G`      | Go to bottom of page        |     | `#`      | Search backwards for selected |
| `d`      | Scroll down (half page)     |     |          |                               |
| `u`      | Scroll up (half page)       |     |          |                               |
| `f`      | Follow link (hint mode)     |     |          |                               |
| `F`      | Follow link in new tab      |     |          |                               |
| `;f`     | Follow link with hint       |     |          |                               |
| `;i`     | Hint image                  |     |          |                               |
| `;o`     | Hint and open (replace tab) |     |          |                               |
| `;O`     | Hint and open in new tab    |     |          |                               |

### Tab Management

| Shortcut | Description                   |
| -------- | ----------------------------- |
| `t`      | Open new tab                  |
| `w`      | Open new window               |
| `o`      | Open URL in current tab       |
| `O`      | Open URL in new tab           |
| `H`      | Back (history)                |
| `L`      | Forward (history)             |
| `J`      | Next tab                      |
| `K`      | Previous tab                  |
| `g0`     | Go to first tab               |
| `g$`     | Go to last tab                |
| `gt`     | Go to tab number (e.g. `3gt`) |
| `gT`     | Go to last tab                |
| `d`      | Delete/close current tab      |
| `D`      | Close all tabs except current |
| `u`      | Undo closed tab               |
| `co`     | Clone current tab             |
| `<<`     | Move tab left                 |
| `>>`     | Move tab right                |

### Page Controls & Bookmarks

| Shortcut | Description                   |     | Shortcut        | Description                   |
| -------- | ----------------------------- | --- | --------------- | ----------------------------- |
| `r`      | Reload page                   |     | `m`             | Set bookmark                  |
| `R`      | Reload page (ignore cache)    |     | `b`             | Open bookmark                 |
| `zi`     | Zoom in                       |     | `B`             | Open bookmark in new tab      |
| `zo`     | Zoom out                      |     | `:open`         | Open URL/search               |
| `z0`     | Reset zoom                    |     | `:history`      | Show browsing history         |
| `i`      | Insert mode (edit form)       |     | `:downloads`    | Show downloads                |
| `e`      | Edit URL                      |     | `:bookmark-add` | Add current page to bookmarks |
| `yy`     | Copy current URL              |     | `:qsave`        | Save page (HTML/PDF)          |
| `yd`     | Copy domain name              |     |                 |                               |
| `yt`     | Copy page title               |     |                 |                               |
| `pp`     | Open clipboard URL            |     |                 |                               |
| `Pp`     | Open clipboard URL in new tab |     |                 |                               |

### Command Mode & Fuzzy Tab

| Shortcut | Description        |     | Command | Description                 |
| -------- | ------------------ | --- | ------- | --------------------------- |
| `:`      | Enter command mode |     | `:b`    | Fuzzy-find open tab by name |
| `:q`     | Close tab          |     | `:tabs` | Show all open tabs          |
| `:qa`    | Close all tabs     |     |         |                             |
| `:w`     | Save page          |     |         |                             |
| `:set`   | Change settings    |     |         |                             |
| `:help`  | Show help          |     |         |                             |

### CLI Commands

| Command                            | Description          |
| ---------------------------------- | -------------------- |
| `qutebrowser`                      | Launch qutebrowser   |
| `qutebrowser [URL]`                | Open URL at launch   |
| `qutebrowser -s [setting] [value]` | Set config at launch |
| `qutebrowser --help`               | Show help            |
| `qutebrowser --version`            | Show version         |

---

## Vimium

| Shortcut | Description              |     | Shortcut | Description    |
| -------- | ------------------------ | --- | -------- | -------------- |
| `j`      | Scroll down              |     | `J`      | Next tab       |
| `k`      | Scroll up                |     | `K`      | Previous tab   |
| `d`      | Page down                |     | `x`      | Close tab      |
| `u`      | Page up                  |     | `X`      | Reopen tab     |
| `gg`     | Go to top                |     | `yt`     | Duplicate tab  |
| `G`      | Go to bottom             |     | `H`      | Back           |
| `f`      | Open link                |     | `L`      | Forward        |
| `F`      | Open link in new tab     |     | `r`      | Reload         |
| `o`      | Open URL / search        |     | `/`      | Find in page   |
| `O`      | Open in new tab          |     | `n`      | Next match     |
| `T`      | Switch tabs (fuzzy find) |     | `N`      | Previous match |
| `?`      | View shortcuts           |     |          |                |

---

## Aerospace

| Shortcut | Description             |
| -------- | ----------------------- |
| `<C-f>`  | Forward (Page down)     |
| `<C-d>`  | Move down (Half a page) |
| `<C-b>`  | Backward (Page up)      |
| `<C-u>`  | Move up (Half a page)   |
| `<C-o>`  | Jump back               |
| `<C-i>`  | Jump forward            |

---

## Configuration & Settings

### VSCode

#### Custom Keybindings (`keybindings.json`)

```json
{
  "key": "ctrl+j",
  "command": "workbench.action.terminal.focusNextPane"
},
{
  "key": "ctrl+k",
  "command": "workbench.action.terminal.focusPreviousPane"
}
```

#### Copilot — Prevent Editor Jumping

| Setting                                            | Value     | Effect                                  |
| -------------------------------------------------- | --------- | --------------------------------------- |
| `chat.editing.revealNextChangeOnResolve`           | `false`   | Stop auto-jump to next changed file     |
| `github.copilot.chat.newWorkspaceCreation.enabled` | `false`   | Disable project scaffolding             |
| `github.copilot.chat.useProjectTemplates`          | `false`   | Disable starter templates               |
| `inlineChat.renderMode`                            | `"hover"` | Keep inline chat lightweight            |
| `inlineChat.finishOnType`                          | `true`    | Close inline chat when typing continues |
| `chat.editMode.hidden`                             | `true`    | Hide edit mode UI                       |
| `chat.commandCenter.enabled`                       | `false`   | Remove chat button from title bar       |

#### Minimal UI Settings

| Setting                                  | Value                                                  | Effect                               |
| ---------------------------------------- | ------------------------------------------------------ | ------------------------------------ |
| `workbench.activityBar.visible`          | `false`                                                | Hide left activity bar               |
| `workbench.statusBar.visible`            | `false`                                                | Hide bottom status bar               |
| `breadcrumbs.enabled`                    | `false`                                                | Remove breadcrumb trail above editor |
| `editor.minimap.enabled`                 | `false`                                                | Disable minimap                      |
| `editor.lineNumbers`                     | `"relative"`                                           | Vim-style relative line numbers      |
| `editor.renderWhitespace`                | `"selection"`                                          | Show whitespace only on selection    |
| `editor.scrollbar.vertical`              | `"hidden"`                                             | Hide vertical scrollbar              |
| `editor.scrollbar.horizontal`            | `"hidden"`                                             | Hide horizontal scrollbar            |
| `workbench.editor.showTabs`              | `true`                                                 | Keep tabs visible                    |
| `workbench.sideBar.location`             | `"left"`                                               | Sidebar on the left                  |
| `workbench.panel.defaultLocation`        | `"bottom"`                                             | Terminal/panel at the bottom         |
| `workbench.panel.opensMaximized`         | `"never"`                                              | Prevent panel from going fullscreen  |
| `workbench.startupEditor`                | `"none"`                                               | Skip welcome screen                  |
| `update.mode`                            | `"manual"`                                             | Disable auto-updates                 |
| `extensions.autoUpdate`                  | `false`                                                | Disable extension auto-updates       |
| `editor.hover.enabled`                   | `false`                                                | Disable hover popups                 |
| `editor.parameterHints.enabled`          | `false`                                                | Disable parameter hints              |
| `terminal.integrated.defaultProfile.osx` | `"zsh"`                                                | Default shell                        |
| `terminal.integrated.fontSize`           | `13`                                                   | Terminal font size                   |
| `terminal.integrated.tabs.enabled`       | `true`                                                 | Enable terminal tabs                 |
| `terminal.integrated.tabs.location`      | `"right"`                                              | Terminal tabs on right               |
| `terminal.integrated.cursorBlinking`     | `true`                                                 | Blinking cursor                      |
| `explorer.confirmDelete`                 | `false`                                                | Skip delete confirmation             |
| `explorer.confirmDragAndDrop`            | `false`                                                | Skip drag/drop confirmation          |
| `explorer.compactFolders`                | `false`                                                | Show full folder tree                |
| `github.copilot.enable`                  | `{ "*": true, "plaintext": false, "markdown": false }` | Copilot on for code, off for text/md |

#### Full `settings.json` Bundle

```json
{
  "workbench.activityBar.visible": false,
  "workbench.statusBar.visible": false,
  "breadcrumbs.enabled": false,
  "editor.minimap.enabled": false,
  "editor.lineNumbers": "relative",
  "editor.renderWhitespace": "selection",
  "editor.scrollbar.vertical": "hidden",
  "editor.scrollbar.horizontal": "hidden",
  "workbench.editor.showTabs": true,
  "workbench.sideBar.location": "left",
  "workbench.panel.defaultLocation": "bottom",
  "workbench.panel.opensMaximized": "never",
  "workbench.startupEditor": "none",
  "update.mode": "manual",
  "extensions.autoUpdate": false,
  "editor.hover.enabled": false,
  "editor.parameterHints.enabled": false,
  "terminal.integrated.defaultProfile.osx": "zsh",
  "terminal.integrated.fontSize": 13,
  "terminal.integrated.tabs.enabled": true,
  "terminal.integrated.tabs.location": "right",
  "terminal.integrated.cursorBlinking": true,
  "explorer.confirmDelete": false,
  "explorer.confirmDragAndDrop": false,
  "explorer.compactFolders": false,
  "chat.editing.revealNextChangeOnResolve": false,
  "github.copilot.chat.newWorkspaceCreation.enabled": false,
  "github.copilot.chat.useProjectTemplates": false,
  "inlineChat.renderMode": "hover",
  "inlineChat.finishOnType": true,
  "chat.editMode.hidden": true,
  "chat.commandCenter.enabled": false,
  "github.copilot.enable": {
    "*": true,
    "plaintext": false,
    "markdown": false
  }
}
```

#### Workflow Model

| Layer    | Role                          |
| -------- | ----------------------------- |
| Editor   | Code only                     |
| Terminal | Execution                     |
| Sidebar  | Temporary, opened on demand   |
| Chat     | Panel-based, not editor-based |
| Copilot  | Assistive, not layout-driving |

---

### Qutebrowser

#### Common Issues & Fixes

| Issue                       | Fix                                                                    |
| --------------------------- | ---------------------------------------------------------------------- |
| Tabs open in wrong position | `:set new_instance_open_target tab` / `:set tabs.new_position related` |
| Tabs close unexpectedly     | `:set tabs.select_on_remove last-used`                                 |
| Tabs feel "lost"            | Use `:b` instead of cycling with `J`/`K`                               |
| Check keybindings           | `:bind`                                                                |

#### Recommended Workflow

- Open tab: `t` → type URL → Enter
- Switch tab: `:b` → type name → Enter (preferred over `J`/`K` cycling)
- Close tab: `d`

#### Minimal Config (`~/.config/qutebrowser/config.py`)

```python
c.tabs.select_on_remove = "last-used"
c.tabs.new_position.related = True
c.tabs.background = True
```
