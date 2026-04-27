# Terminal Graphics in C — ANSI Escape Codes & Pixel Rendering

## How a Terminal Works

A terminal is a **grid of character cells**. Each cell has:
- A **character** (the glyph drawn)
- A **foreground color** (the glyph's color)
- A **background color** (the cell's fill color)

"Graphics" in a terminal means filling those cells cleverly using ANSI escape codes.

---

## ANSI Escape Codes

Escape codes are byte sequences embedded in your stdout. The terminal emulator intercepts them as commands — they are never drawn as text.

### Anatomy

```
\033  [  <params>  <command letter>
 ESC  [  1;32      m
```

- `\033` = ESC character (hex `0x1B`)
- `[` = CSI (Control Sequence Introducer)
- params = semicolon-separated numbers
- command letter = what to do

---

## Color Codes (`m` command)

```c
printf("\033[<code>m");  // Set Graphics Rendition
```

| Code | Meaning |
|------|---------|
| `0` | Reset all formatting |
| `1` | Bold |
| `2` | Dim |
| `4` | Underline |
| `7` | Reverse (swap fg/bg) |
| `30–37` | Legacy foreground colors: black red green yellow blue magenta cyan white |
| `38` | Extended foreground-color introducer |
| `39` | Reset foreground to terminal default |
| `40–47` | Legacy background colors: black red green yellow blue magenta cyan white |
| `48` | Extended background-color introducer |
| `49` | Reset background to terminal default |
| `90–97` | Bright foreground colors |
| `100–107` | Bright background colors |

Chain multiple attributes with `;`:

```c
printf("\033[1;4;32mHello\033[0m");  // bold + underline + green, then reset
```

### The Full Color-Code Family

The foreground and background color controls come in matching families:

| Role | Legacy named colors | Extended form | Reset to default |
|------|---------------------|---------------|------------------|
| Foreground | `30-37`, `90-97` | `38;...` | `39` |
| Background | `40-47`, `100-107` | `48;...` | `49` |

### Full Legacy and Bright Mapping

Here is the explicit per-code mapping, with nothing implied:

| Foreground | Color | Background | Color |
|------------|-------|------------|-------|
| `30` | black | `40` | black |
| `31` | red | `41` | red |
| `32` | green | `42` | green |
| `33` | yellow | `43` | yellow |
| `34` | blue | `44` | blue |
| `35` | magenta | `45` | magenta |
| `36` | cyan | `46` | cyan |
| `37` | white | `47` | white |

Bright variants:

| Bright foreground | Color | Bright background | Color |
|-------------------|-------|-------------------|-------|
| `90` | bright black / gray | `100` | bright black / gray |
| `91` | bright red | `101` | bright red |
| `92` | bright green | `102` | bright green |
| `93` | bright yellow | `103` | bright yellow |
| `94` | bright blue | `104` | bright blue |
| `95` | bright magenta | `105` | bright magenta |
| `96` | bright cyan | `106` | bright cyan |
| `97` | bright white | `107` | bright white |

So if you want the complete picture:

- `30-37` = set one of the 8 legacy foreground colors
- `90-97` = set one of the 8 bright foreground colors
- `38;...` = set foreground using an extended format
- `39` = restore the foreground to the terminal's default
- `40-47` = set one of the 8 legacy background colors
- `100-107` = set one of the 8 bright background colors
- `48;...` = set background using an extended format
- `49` = restore the background to the terminal's default

Examples:

```c
printf("\033[31m");         // legacy red foreground
printf("\033[39m");         // default foreground
printf("\033[44m");         // legacy blue background
printf("\033[49m");         // default background
printf("\033[38;5;214m");   // extended foreground, indexed palette
printf("\033[48;2;0;0;0m"); // extended background, true RGB
```

### What `39` and `49` Mean

These are easy to miss, but they matter:

- `39` = reset **only the foreground color** back to the terminal theme default
- `49` = reset **only the background color** back to the terminal theme default

They are narrower than `0`.

```c
printf("\033[1;31mHello");  // bold red text
printf("\033[39m");         // foreground goes back to default, bold remains
printf("\033[0m");          // now everything resets
```

Likewise for background:

```c
printf("\033[44m");  // blue background
printf("\033[49m");  // default background
```

So the structure is intentional:

- `38` introduces an extended **foreground** color specification
- `39` resets **foreground**
- `48` introduces an extended **background** color specification
- `49` resets **background**

That is why it is useful to think in pairs:

| Pair | Meaning |
|------|---------|
| `38` / `39` | Extended foreground / default foreground |
| `48` / `49` | Extended background / default background |

### Two Numbering Systems: SGR Codes vs Color Indexes

This is the part that usually confuses people.

There are **two different kinds of numbers** inside `\033[...m`:

1. **SGR control codes** - these mean things like "set red foreground" or "turn on underline".
2. **Color data values** - these are extra arguments used by some SGR codes.

So these are **not the same kind of number**:

```c
printf("\033[31m");        // SGR code 31 = normal red foreground
printf("\033[44m");        // SGR code 44 = normal blue background
printf("\033[38;5;214m");  // SGR 38 = extended fg, 5 = 256-color mode, 214 = palette index
```

The table above only lists the **standalone SGR meaning codes** like `31`, `44`, `1`, `4`, and `0`.

### Where `38`, `39`, `48`, and `49` Come From

`38`, `39`, `48`, and `49` are themselves **SGR control codes**.

They were added as part of the extended-color convention used by modern terminals:

- `38` = set **foreground** color using an extended format
- `39` = restore **foreground** to the default color
- `48` = set **background** color using an extended format
- `49` = restore **background** to the default color

Think of them as the extended-color counterparts to:

- `30-37` = legacy foreground colors
- `40-47` = legacy background colors

So the split is:

| Form | Meaning |
|------|---------|
| `31` | Use legacy red foreground |
| `39` | Use the terminal's default foreground again |
| `44` | Use legacy blue background |
| `49` | Use the terminal's default background again |
| `38;...` | Use an extended foreground-color format |
| `48;...` | Use an extended background-color format |

After `38` or `48`, the next parameter tells the terminal **which extended format** you want:

- `5` = indexed 256-color palette
- `2` = explicit RGB true color

So these two patterns are parallel:

```c
printf("\033[38;5;214m");        // extended foreground -> indexed palette -> slot 214
printf("\033[48;5;21m");         // extended background -> indexed palette -> slot 21
printf("\033[38;2;255;100;0m");  // extended foreground -> RGB -> (255,100,0)
printf("\033[48;2;255;100;0m");  // extended background -> RGB -> (255,100,0)
```

In other words:

- `38` does **not** mean "color number 38"
- `39` does **not** mean "color number 39"
- `48` does **not** mean "color number 48"
- `49` does **not** mean "color number 49"

They are SGR operations:

- `38` = start extended foreground syntax
- `39` = reset foreground
- `48` = start extended background syntax
- `49` = reset background

It does **not** list palette indexes like `214`, because `214` has no meaning by itself. It only means something when it appears after:

- `38;5;N` for an indexed foreground color
- `48;5;N` for an indexed background color

Read this sequence left to right:

```c
\033[38;5;214m
```

- `38` = "I am about to set the foreground using an extended color format"
- `5` = "the format is 256-color indexed mode"
- `214` = "use palette entry 214"

That is why `214` is not "missing from the meaning grid". It is **not another SGR command**. It is the **payload value** for the earlier command.

### Where the 256 Colors Come From

The original ANSI / VT-style terminals only had a small named-color set:

- `30-37` / `40-47` = 8 normal colors
- `90-97` / `100-107` = 8 bright colors

Later, `xterm` introduced a widely adopted extension that added an **indexed 256-color palette**. Modern terminal emulators usually support it for compatibility.

That palette is:

| Index range | Meaning |
|------------|---------|
| `0-7` | The 8 base colors |
| `8-15` | The 8 bright colors |
| `16-231` | A 6 x 6 x 6 RGB color cube (`216` colors) |
| `232-255` | A 24-step grayscale ramp |

So:

```text
16 legacy colors
+ 216 cube colors
+ 24 grayscale colors
= 256 total
```

### Why They Are Not Confused with the Normal ANSI Colors

They are separated by **position and syntax**.

These mean named legacy colors:

```c
printf("\033[31m");  // legacy red foreground
printf("\033[42m");  // legacy green background
```

These mean indexed palette colors:

```c
printf("\033[38;5;1m");    // palette index 1 as foreground
printf("\033[48;5;214m");  // palette index 214 as background
```

Even though both use numbers, the terminal does not guess. It parses the sequence structurally:

- plain `31` means the SGR command "red foreground"
- `38;5;1` means "extended foreground color, indexed mode, slot 1"

So `1` in `38;5;1` is **not** the same thing as SGR `1` ("bold"). Context decides the meaning.

### Important Detail: Indexes `0-15` Overlap the Legacy Colors

This is also why examples can look odd at first.

In 256-color mode, indexes `0-15` correspond to the old 16 terminal colors. So these are conceptually related:

```c
printf("\033[31mred\033[0m");       // legacy named red
printf("\033[38;5;1mred\033[0m");   // palette slot 1, usually the same red family
```

But from `16` upward, you are no longer using the old named-color set. You are selecting entries from the larger xterm-style palette.

That is why examples often use values like `21`, `196`, or `214`: those are palette slots from the extended table, not legacy named-color codes.

### What Color Is a Given 256-Color Index?

For the 6 x 6 x 6 cube (`16-231`), each color is built from:

- red level `0-5`
- green level `0-5`
- blue level `0-5`

The index formula is:

```text
index = 16 + 36*r + 6*g + b
```

The usual channel values for each level are:

```text
0, 95, 135, 175, 215, 255
```

Examples:

- `21 = 16 + 36*0 + 6*0 + 5` -> `(0, 0, 255)` -> strong blue
- `214 = 16 + 36*5 + 6*3 + 0` -> `(255, 175, 0)` -> orange-ish

So this:

```c
printf("\033[38;5;214m");   // foreground color #214
printf("\033[48;5;21m");    // background color #21
```

is really saying:

- foreground = palette slot `214`
- background = palette slot `21`

not:

- "SGR code 214"
- "SGR code 21"

### Theme Dependence vs Exact RGB

One more subtle point:

- the legacy colors (`30-37`, `90-97`, and palette indexes `0-15`) are often mapped through the terminal's current theme
- the indexed cube / grayscale entries (`16-255`) are usually fixed to the terminal's 256-color palette
- true color (`38;2;R;G;B` / `48;2;R;G;B`) requests an explicit RGB value directly

So if you want "the user's terminal red", use legacy colors.

If you want a known palette slot like xterm orange `214`, use `38;5;214`.

If you want an exact RGB value, use true color.

### True Color (RGB)

```c
printf("\033[38;2;255;100;0m");  // foreground RGB
printf("\033[48;2;255;100;0m");  // background RGB
```

**Always reset after colored output:**

```c
printf("\033[0m");
```

---

## Cursor Movement

```c
"\033[<n>A"          // up n rows
"\033[<n>B"          // down n rows
"\033[<n>C"          // right n cols
"\033[<n>D"          // left n cols
"\033[<row>;<col>H"  // move to absolute position (1-indexed)
"\033[H"             // move to home (top-left, 1,1)
"\033[s"             // save cursor position
"\033[u"             // restore cursor position
```

## Screen Commands

```c
"\033[2J"   // clear entire screen
"\033[0J"   // clear from cursor to end of screen
"\033[2K"   // clear entire current line
"\033[0K"   // clear from cursor to end of line
```

## Hide/Show Cursor

```c
printf("\033[?25l");  // hide cursor (stops flicker during animation)
printf("\033[?25h");  // show cursor — always restore on exit!
```

---

## The Pixel Method

The key insight: **a space character with a background color IS a pixel.**

A space has no visible glyph, so only the background color is seen. That cell becomes a solid colored pixel.

```c
printf("\033[48;2;255;0;0m ");  // red pixel (space + red background)
printf("\033[48;2;0;255;0m ");  // green pixel
printf("\033[0m");               // reset
```

### Drawing a Colored Rectangle

```c
for (int y = 0; y < 10; y++) {
    for (int x = 0; x < 20; x++) {
        printf("\033[48;2;255;100;0m ");  // orange pixel
    }
    printf("\033[0m\n");  // reset + newline
}
```

### Full Block Character Alternative

Use `█` (U+2588) as a pixel with foreground color — no background trick needed:

```c
printf("\033[38;2;255;0;0m█\033[0m");  // red block pixel
```

### Half-Block Trick — 2× Vertical Resolution

Using `▀` (upper half block, U+2580), each terminal row holds **two pixel rows**:
- Top pixel = foreground color
- Bottom pixel = background color

```c
printf("\033[38;2;255;0;0m\033[48;2;0;0;255m▀\033[0m");
// top half = red, bottom half = blue — two rows in one cell
```

---

## Redrawing Without Flicker

### ❌ Clear Screen (causes flicker)

```c
printf("\033[2J\033[H");  // blanks the screen briefly
printf("%s", frame);
```

### ✅ Cursor Home (no flicker — standard approach)

```c
printf("\033[H");         // rewind cursor to top-left
printf("%s", frame);      // overwrite previous content in-place
fflush(stdout);
```

**Requirement:** every frame must be the **same dimensions** — same rows × cols. Otherwise old characters from previous frames bleed through on shorter frames.

### ✅✅ Diff Rendering (most efficient)

Only reprint cells that changed between frames (this is what ncurses does internally):

```c
for (int i = 0; i < WIDTH * HEIGHT; i++) {
    if (new_frame[i] != old_frame[i]) {
        printf("\033[%d;%dH", i / WIDTH + 1, i % WIDTH + 1);
        putchar(new_frame[i]);
    }
}
memcpy(old_frame, new_frame, WIDTH * HEIGHT);
```

---

## Game Loop Pattern

```c
#include <stdio.h>
#include <unistd.h>

#define WIDTH  80
#define HEIGHT 24

char frame[HEIGHT][WIDTH + 1];  // +1 for newline per row

void render() {
    printf("\033[H");                        // rewind cursor
    fwrite(frame, 1, sizeof(frame), stdout); // dump entire frame
    fflush(stdout);
}

int main() {
    printf("\033[?25l");  // hide cursor

    while (1) {
        // update frame buffer here...
        render();
        usleep(16666);    // ~60fps
    }

    printf("\033[?25h");  // restore cursor on exit
    printf("\033[0m");    // reset colors
    return 0;
}
```

---

## Summary

| Goal | Technique |
|------|-----------|
| Colored pixel | Space + `\033[48;2;R;G;Bm` (background color) |
| Block pixel | `█` + `\033[38;2;R;G;Bm` (foreground color) |
| 2× vertical res | `▀` with fg + bg colors |
| Redraw without flicker | `\033[H` cursor home, then overprint |
| Hide cursor during draw | `\033[?25l` / `\033[?25h` |
| Reset all formatting | `\033[0m` |
