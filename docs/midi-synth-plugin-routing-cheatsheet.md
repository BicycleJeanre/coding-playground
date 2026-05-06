# MIDI Synth / Controller / Rompler Routing Cheatsheet

## 1. Core Terms

| Term | Meaning |
|---|---|
| MIDI | Note/control data, not audio. |
| MIDI channel | One of 16 lanes inside a MIDI stream. |
| Plugin instrument | Turns MIDI into audio. |
| Synth | Generates sound electronically. |
| Sampler | Plays recorded samples. |
| Rompler | Sampler-style instrument with built-in sounds. |
| Controller | Hardware/software that sends MIDI. |
| Audio output | Sound coming out of a plugin. |
| Plugin output channel | An audio output path, not a MIDI channel. |

## 2. The Most Important Distinction

MIDI channels and plugin output channels are different things.

`MIDI channel = which part/instrument receives notes`

`Audio output = where the sound comes out`

Example:

- MIDI channel 1 sends notes to a piano part.
- MIDI channel 2 sends notes to a bass part.
- Plugin output 1/2 carries the piano audio.
- Plugin output 3/4 carries the bass audio.

## 3. Simple Instrument Setup

Most beginner-friendly plugin instruments work like this:

`Step editor -> MIDI notes -> plugin -> stereo audio output`

Typical setup:

- Track contains MIDI clip.
- MIDI notes use channel 1 or "Any".
- Plugin receives MIDI.
- Plugin outputs stereo audio to the same track.

## 4. Multitimbral Instruments

A multitimbral plugin can play multiple sounds at once.

Typical example:

| MIDI Channel | Plugin Part | Sound |
|---:|---|---|
| 1 | Part 1 | Piano |
| 2 | Part 2 | Bass |
| 3 | Part 3 | Strings |
| 10 | Part 10 | Drums |

This is common in:

- General MIDI modules and SoundFont players
- Some romplers and Kontakt-style instruments
- Drum plugins with separate outputs

## 5. Multi-Output Plugins

Some plugins expose several audio outputs.

Example:

| Plugin Output | Audio |
|---|---|
| Out 1/2 | Main stereo |
| Out 3/4 | Bass |
| Out 5/6 | Drums |
These outputs are for mixing audio separately.

They do not decide which MIDI notes trigger which sound.

## 6. Step Editor vs Plugin Parts

The step editor usually creates MIDI notes.

Useful note properties:

- Note pitch: C3, D#4, etc.
- Velocity: how hard the note is played.
- Length: how long the note lasts.
- MIDI channel: which plugin part receives it.

If every note is on MIDI channel 1, only parts listening to channel 1 will respond.

## 7. Common Problem

"The plugin has lots of output channels. How do I match them to the step editor?"

Usually, you do not match step-editor lanes to output channels directly.

Instead:

1. Step editor note uses a MIDI channel.
2. Plugin receives that MIDI channel.
3. Plugin part plays a sound.
4. Plugin routes that part's audio to an output.

So the chain is:

`Step editor MIDI channel -> plugin part -> plugin audio output`

## 8. Best Beginner Routing

Start with one instrument per track.

Example:

| Track | Plugin | MIDI Channel | Audio Output |
|---|---|---:|---|
| Piano | Rompler | 1 | Main stereo |
| Bass | Bass plugin | 1 | Main stereo |
| Drums | Drum plugin | 1 or 10 | Main stereo |
| Strings | Rompler | 1 | Main stereo |

This is easier than using one plugin with many MIDI channels and outputs.

Use multi-output routing only when you need separate mixing from one plugin.

## 9. General MIDI Basics

General MIDI is a standard sound map.

Rules:

- 16 MIDI channels.
- Channel 10 is usually drums.
- Program changes select sounds.
General MIDI is useful for old MIDI files.

It is less important when writing your own tracks in a DAW.

## 10. Plugin Types

| Type | What It Does | Typical Use |
|---|---|---|
| Synth | Creates sound electronically | Leads, basses, pads |
| Sampler | Plays loaded samples | Real instruments, drums |
| Rompler | Plays built-in sample sounds | Pianos, strings, brass |
| Drum machine | Maps notes to drum hits | Beats |
| SoundFont player | Loads `.sf2` libraries | General MIDI sounds |
| Audio effect | Changes sound after plugin | EQ, reverb, compression |

## 11. Drum Note Mapping

Drum plugins often use notes instead of pitches.

Common General MIDI drum notes:

| MIDI Note | Drum |
|---:|---|
| 36 | Kick |
| 38 | Snare |
| 42 | Closed hi-hat |
| 46 | Open hi-hat |
| 49 | Crash |
| 51 | Ride |

If the wrong drum plays, the step editor is probably using the wrong note number.

## 12. Troubleshooting Checklist

If you get no sound:

1. Confirm the plugin is an instrument, not an effect.
2. Put the plugin after the MIDI clip on the same track.
3. Check the track is not muted.
4. Check the plugin preset has a sound loaded.
5. Set MIDI notes to channel 1 or "Any".
6. Check the plugin part is listening to that channel.
7. Use the main stereo output first.

If only one sound plays:

1. The plugin may not be multitimbral.
2. All notes may be on the same MIDI channel.
3. The plugin may only have one active part loaded.

If audio outputs look confusing:

1. Ignore extra outputs at first.
2. Use the main stereo output.

## 13. Waveform Step Editor — Fixing Row / Plugin Mismatches

Each row in Waveform's step editor sends one specific MIDI note pitch.
Each sound in your plugin is triggered by one specific MIDI note.
If these don't match, rows produce silence and some plugin sounds are unreachable.

**Step-by-step fix:**

1. Open the plugin editor and note which MIDI note triggers each sound.
   - Example: kick = C1 (note 36), snare = D1 (note 38), hi-hat = F#1 (note 42).
   - Check the plugin's documentation or drum map view if the UI is unclear.

2. In the step editor, right-click a row label to reassign the MIDI note it sends.
   - Set it to match the note the plugin expects for that sound.

3. If a plugin sound has no row, add a new row and assign it to the correct note.

4. If a row has no matching plugin sound, either reassign it or delete it.

**Auto-labelling shortcut:**

Some plugins export note names to the DAW (Tracktion's own drum sampler does this).
If your plugin supports it, Waveform will automatically label rows with the correct sound names.
Look for a "note names", "drum map", or "key map" option inside the plugin.

**Quick reference — common GM drum notes:**

| Row label | MIDI Note | Note name |
|---|---:|---|
| Kick | 36 | C1 |
| Snare | 38 | D1 |
| Closed hi-hat | 42 | F#1 |
| Open hi-hat | 46 | A#1 |
| Crash | 49 | C#2 |
| Ride | 51 | D#2 |

Non-GM plugins may use a completely different note layout — always verify in the plugin first.

## 14. Practical Rule

- Writing music in Waveform: use separate tracks for separate instruments.
- Playing General MIDI files: use one multitimbral plugin with the right MIDI channels.
- Mixing drums separately: use multi-output drums after the basic kit is already playing.

---

## 15. Plugin Formats

| Format | Full Name | Platform | Notes |
|---|---|---|---|
| VST2 | Virtual Studio Technology 2 | Win / Mac / Linux | Widely supported, older standard |
| VST3 | Virtual Studio Technology 3 | Win / Mac / Linux | Improved performance, better MIDI handling |
| AU | Audio Units | Mac only | Native macOS/iOS format |
| CLAP | CLever Audio Plug-in | Win / Mac / Linux | Newer open standard, growing support |
| AAX | Avid Audio Extension | Win / Mac | Pro Tools only |

Waveform supports VST2, VST3, and AU (on Mac).
Prefer VST3 when a plugin offers both VST2 and VST3 — it handles MIDI notes off and parameter automation more reliably.

## 16. Waveform — Setting Up an Instrument Track

1. Create a new track (right-click in the track area → **Add Track**).
2. Click the track's plugin area and choose **Add Plugin → Instruments**.
3. Select your plugin from the browser.
4. The plugin now sits in the instrument slot; MIDI clips on that track feed into it.
5. Audio from the plugin plays back through the same track's output.
6. To set the MIDI channel the track sends on: open the track properties and set **MIDI channel** (default is channel 1).

Step track variant:

1. Right-click in the track area → **Add Step Clip** (or convert an existing clip).
2. Assign a plugin to the track as above.
3. Each row in the step editor sends notes to that plugin.

## 17. Waveform Step Editor — Controls Reference

| Control | What It Does |
|---|---|
| Row label | Shows the note/sound for that row; right-click to reassign |
| Step button | Toggles a note on/off at that step |
| Velocity per step | Right-click a lit step to set its velocity |
| Note length per step | Right-click a lit step to set how long it sustains |
| Pattern length | Drag the end of the clip or set bar count in clip properties |
| Step resolution | Sets the grid (1/8, 1/16, 1/32, etc.) — found in the step editor toolbar |
| Swing | Offsets even-numbered steps to add groove — in the step editor toolbar |
| Channel per row | Right-click a row to assign it to a specific MIDI channel |

## 18. MIDI CC (Control Change) Messages

CC messages change parameters in real time — volume, modulation, expression, etc.

Common CCs:

| CC Number | Name | Typical Use |
|---:|---|---|
| 1 | Modulation wheel | Vibrato depth, filter, etc. |
| 7 | Channel volume | Overall part volume |
| 10 | Pan | Stereo position |
| 11 | Expression | Dynamics within a phrase |
| 64 | Sustain pedal | Hold notes |
| 74 | Brightness / cutoff | Filter cutoff on many synths |

In Waveform, add CC automation by:

1. Opening a MIDI clip in the piano roll.
2. Clicking the **automation lane** at the bottom.
3. Selecting the CC number you want to draw.

Or use a **MIDI Modifier** plugin on the track (see §19).

## 19. MIDI Modifiers in Waveform

MIDI modifiers sit on a track and transform MIDI before it reaches the instrument plugin.

Access them: click the track's plugin chain → **Add Plugin → MIDI Modifiers**.

| Modifier | What It Does |
|---|---|
| Arpeggiator | Turns held chords into rhythmic note patterns |
| Chord Player | Turns single notes into full chords |
| Pitch Bend | Adds or offsets pitch bend data |
| Velocity | Scales, randomises, or clamps note velocities |
| Note Repeat | Repeats notes at a set rate while held |
| Transpose | Shifts all notes up or down by semitones |
| MIDI Channel Filter | Blocks or allows specific MIDI channels |
| Randomiser | Randomly varies pitch, velocity, or timing |

Modifiers are non-destructive — they do not change the clip data, only what the plugin receives.

## 20. Connecting External MIDI Devices in Waveform

**Hardware controller (keyboard, pad, etc.):**

1. Connect via USB or MIDI interface.
2. In Waveform: **Settings → MIDI Devices** — enable the input device.
3. Arm a track for recording; the controller now sends MIDI to that track's plugin.

**Hardware synth as output:**

1. Connect the synth's MIDI IN to your interface's MIDI OUT.
2. In **Settings → MIDI Devices** — enable the output device.
3. On the Waveform track, set the output to that MIDI device instead of a plugin.
4. The track sends MIDI out to the hardware synth; audio comes back via audio interface inputs.

**Hardware synth clock sync:**

- Enable **MIDI Clock Send** in Waveform's settings to keep hardware in time with the project.

## 21. Multi-Output Routing in Waveform

Some plugins expose multiple stereo outputs (e.g. a drum plugin with kick, snare, and overhead outputs).

Setup in Waveform:

1. Add the plugin to a track as usual.
2. Click the plugin's output section — Waveform shows available outputs.
3. Enable additional outputs; Waveform creates extra tracks automatically (sub-tracks or sends).
4. Each output track can then have its own EQ, compression, and level.

Use case:

| Plugin Output | Track | Processing |
|---|---|---|
| Out 1/2 (kick) | Kick track | Heavy compression |
| Out 3/4 (snare) | Snare track | Reverb, EQ |
| Out 5/6 (overhead) | OH track | High-pass filter |
| Out 7/8 (master) | Drums bus | Glue compression |

Only use this when you need separate mixing. For most work, a single stereo output is simpler.

## 22. Program / Patch Changes

A program change tells a plugin (or hardware synth) to switch to a different preset/sound mid-sequence.

| Term | Meaning |
|---|---|
| Program Change (PC) | MIDI message that selects a patch number (0–127) |
| Bank Select (CC 0 / CC 32) | Selects a bank before the program change |

In Waveform:

1. Open a MIDI clip in the piano roll.
2. In the event list or automation lanes, insert a **Program Change** event at the desired position.
3. Set the program number to match the patch you want on the plugin.

Most modern plugins respond to program changes, but behaviour varies — check the plugin docs.

## 23. MIDI Clock and Sync

MIDI clock keeps multiple devices or plugins in tempo sync.

| Message | Purpose |
|---|---|
| MIDI Clock | 24 pulses per quarter note; slaves follow master tempo |
| MIDI Start / Stop | Tells slaves to start or stop playback |
| MIDI Song Position | Tells a slave where in the song to jump to |

In Waveform:

- **Sending clock to hardware:** Settings → MIDI → enable clock output on the relevant port.
- **Receiving clock from hardware:** Set Waveform's sync source to an external MIDI clock input (Settings → Synchronisation).
- For plugins that sync to host tempo (LFOs, delays, arpeggiators): they read Waveform's tempo automatically — no manual clock setup needed.

## 24. Latency, Buffer Size, and Plugin Delay Compensation

**Buffer size** controls how much audio the CPU processes at once.

| Buffer Size | Latency | CPU Load | Use For |
|---|---:|---|---|
| 64–128 samples | Very low | High | Live playing / recording |
| 256–512 samples | Low | Moderate | Most studio work |
| 1024+ samples | Higher | Low | Mixing / mastering only |

**Plugin Delay Compensation (PDC):**

Some plugins (especially lookahead compressors and analysers) introduce a fixed delay.
Waveform handles PDC automatically — all tracks are time-aligned behind the scenes.
If tracks sound out of sync, check that PDC is enabled in **Settings → Audio**.

**MIDI-specific latency:**

- External hardware synths have extra latency (MIDI transmission + synth audio).
- Compensate by nudging the hardware track backward in the timeline, or use the track delay offset in Waveform's track properties.
