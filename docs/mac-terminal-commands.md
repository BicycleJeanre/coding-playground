# Mac Terminal Commands Reference

**Last Updated: 2026-04-27**

A practical reference for developers working in the macOS terminal. Commands are split into two sections:

- **Part 1 — macOS-Specific:** tools that exist only on macOS (or have macOS-only implementations)
- **Part 2 — Linux Standard / BSD:** commands standard on Linux distros that are also present on macOS (usually via the BSD layer)

> ⚠️ **BSD vs GNU:** Many "standard" tools on macOS are BSD variants, not GNU. This means flags sometimes differ from Linux (e.g., `sed -i ''` instead of `sed -i`, `date -v` instead of `date -d`). Install GNU coreutils via Homebrew if you need GNU-compatible behaviour.

---

## Part 1 — macOS-Specific Commands

### Clipboard

| Command | Description | Example |
|---------|-------------|---------|
| `pbcopy` | Copy stdin to the macOS clipboard | `cat file.txt \| pbcopy` |
| `pbpaste` | Paste clipboard contents to stdout | `pbpaste > output.txt` |

---

### File & App Interaction

| Command | Description | Example |
|---------|-------------|---------|
| `open` | Open a file, folder, or URL with its default application | `open .` / `open https://example.com` |
| `ditto` | Copy files/directories preserving all metadata, resource forks, and ACLs | `ditto src/ dst/` |
| `dot_clean` | Remove AppleDouble `._` files from a directory tree | `dot_clean ~/Downloads` |
| `GetFileInfo` | Print HFS+ file attributes (type, creator, flags) | `GetFileInfo myfile.txt` |
| `SetFile` | Set HFS+ file attributes | `SetFile -a E myfile.txt` |
| `xattr` | Inspect and manage extended attributes (used by Gatekeeper quarantine etc.) | `xattr -l file.dmg` / `xattr -d com.apple.quarantine file.dmg` |
| `textutil` | Convert between text formats: RTF, RTFD, HTML, DOC, DOCX, ODT, plain text | `textutil -convert html doc.rtf` |
| `sips` | Scriptable Image Processing System — resize, convert, and query images | `sips -z 256 256 image.png` |
| `tiffutil` | Process and inspect TIFF files | `tiffutil -info image.tiff` |
| `tiff2icns` | Convert a TIFF image into an Apple icon (.icns) | `tiff2icns icon.tiff icon.icns` |
| `iconutil` | Convert `.iconset` folders to `.icns` and back | `iconutil -c icns MyIcon.iconset` |
| `qlmanage` | Manage QuickLook previews; generate thumbnails from the command line | `qlmanage -p myfile.pdf` |
| `xar` | Create/extract `.xar` extensible archive format (used in .pkg files) | `xar -xf package.pkg` |
| `lsbom` | List the contents of a BOM (Bill of Materials) file from a package | `lsbom /var/db/receipts/com.example.pkg.bom` |
| `SplitForks` | Split resource forks into AppleDouble format | `SplitForks myfile` |
| `applesingle` | Encode/decode AppleSingle files | `applesingle -e myfile` |
| `macbinary` | Encode/decode MacBinary format | `macbinary encode myfile` |
| `binhex` | BinHex encode files (legacy Mac format) | `binhex myfile` |
| `trash` | Move files to the Trash (rather than deleting permanently) | `trash myfile.txt` |

---

### Spotlight & Metadata

| Command | Description | Example |
|---------|-------------|---------|
| `mdfind` | Spotlight search from the command line | `mdfind -name "report.pdf"` / `mdfind "kMDItemKind == 'PDF Document'"` |
| `mdls` | List all Spotlight metadata attributes for a file | `mdls myfile.pdf` |
| `mdimport` | Manually import files into the Spotlight index | `mdimport myfile.pdf` |
| `mdutil` | Manage the Spotlight index on a volume | `mdutil -s /` / `mdutil -E /` (erase index) |

---

### System Information

| Command | Description | Example |
|---------|-------------|---------|
| `sw_vers` | Print macOS version information | `sw_vers` / `sw_vers -productVersion` |
| `system_profiler` | Detailed hardware and software system profile | `system_profiler SPHardwareDataType` |
| `hostinfo` | Display CPU and memory hardware info | `hostinfo` |
| `vm_stat` | Virtual memory statistics (pages free, active, wired, etc.) | `vm_stat` |
| `pagesize` | Print the system memory page size in bytes | `pagesize` |
| `syslog` | Query the Apple System Log (ASL) / unified logging | `syslog -F raw \| head -20` |
| `log` | Query and stream the unified macOS logging system (Catalina+) | `log show --last 1h --predicate 'process == "Finder"'` |
| `machine` | Print the hardware machine type | `machine` |
| `uname` | Print OS/kernel name and version (BSD, also Linux) — included here for comparison | `uname -a` |

---

### Power & Sleep Management

| Command | Description | Example |
|---------|-------------|---------|
| `caffeinate` | Prevent the system from sleeping while a command runs | `caffeinate -i make` / `caffeinate -t 3600` |
| `pmset` | Get and set power management settings | `pmset -g` / `pmset sleepnow` |
| `powermetrics` | Sample CPU, GPU, and peripheral power usage in real time | `sudo powermetrics --samplers cpu_power -n 1` |
| `thermal` | Show thermal throttling status | `thermal` |
| `memory_pressure` | Show current memory pressure level and statistics | `memory_pressure` |

---

### Process & Performance Diagnostics

| Command | Description | Example |
|---------|-------------|---------|
| `sample` | Sample a running process and produce a call-tree report | `sample Safari 5` |
| `spindump` | Capture a spin/hang report for a process or the whole system | `sudo spindump` |
| `vmmap` | Print the virtual memory map of a process | `vmmap -summary $(pgrep Safari)` |
| `heap` | List heap allocations of a process | `heap $(pgrep myapp)` |
| `leaks` | Find memory leaks in a running process | `leaks $(pgrep myapp)` |
| `malloc_history` | Show allocation history for a process (requires MallocStackLogging) | `malloc_history $(pgrep myapp)ALLOC_ADDRESS` |
| `stringdups` | Find duplicate strings in a process's heap | `stringdups $(pgrep myapp)` |
| `footprint` | Show the memory footprint of a process | `footprint $(pgrep Safari)` |
| `fs_usage` | Real-time file system activity monitor | `sudo fs_usage -f filesys` |
| `sc_usage` | Real-time system call usage by process | `sudo sc_usage -c echo` |
| `dyld_usage` | Monitor dynamic linker activity | `sudo dyld_usage` |
| `latency` | Show interrupt and scheduling latency | `sudo latency` |
| `opensnoop` | DTrace-based: show files being opened in real time | `sudo opensnoop` |
| `execsnoop` | DTrace-based: show processes being executed in real time | `sudo execsnoop` |
| `iotop` | DTrace-based: show I/O by process | `sudo iotop` |
| `iosnoop` | DTrace-based: monitor I/O events | `sudo iosnoop` |
| `dtruss` | DTrace-based system call tracer (like strace on Linux) | `sudo dtruss ls` |
| `ktrace` | Low-level kernel trace facility | `sudo ktrace trace -S` |
| `tailspin` | Diagnose hangs and high-CPU spins | `sudo tailspin start` |
| `xctrace` | Record Instruments traces from the command line | `xctrace record --template 'Time Profiler' --launch -- myapp` |
| `taskinfo` | Display Mach task info for a process | `taskinfo $(pgrep Safari)` |
| `lskq` | List kernel queues (kqueues) for processes | `sudo lskq` |
| `lsmp` | List Mach ports for a process | `sudo lsmp -p $(pgrep myapp)` |
| `nettop` | Real-time network activity per process | `nettop -m tcp` |

---

### Audio & Media

| Command | Description | Example |
|---------|-------------|---------|
| `say` | Text-to-speech synthesis | `say "Hello, world"` / `say -v Daniel "Testing"` |
| `afplay` | Play an audio file in the terminal | `afplay alert.wav` |
| `afconvert` | Convert audio file formats | `afconvert input.wav output.m4a -f m4af -d aac` |
| `afinfo` | Display metadata about an audio file | `afinfo song.mp3` |

---

### Disk & Volume Management

| Command | Description | Example |
|---------|-------------|---------|
| `diskutil` | Manage disks and volumes (list, partition, format, repair, APFS) | `diskutil list` / `diskutil repairVolume /dev/disk1s1` |
| `hdiutil` | Create, mount, and manipulate disk images (`.dmg`) | `hdiutil create -size 100m -fs HFS+ myimage.dmg` |
| `trimforce` | Enable/disable TRIM for third-party SSDs | `sudo trimforce enable` |
| `drutil` | Optical disc utility — burn, eject, info | `drutil info` / `drutil burn -speed 4 /path/to/content` |

---

### Networking (macOS-Specific)

| Command | Description | Example |
|---------|-------------|---------|
| `networksetup` | Configure network settings (interfaces, DNS, proxies, Wi-Fi) | `networksetup -listallnetworkservices` / `networksetup -setdnsservers Wi-Fi 1.1.1.1` |
| `scutil` | System Configuration Utility — query/set network config, hostname | `scutil --get ComputerName` / `scutil --dns` |
| `ipconfig` | macOS version: query DHCP leases and interface info | `ipconfig getifaddr en0` / `ipconfig getsummary en0` |
| `airport` | Wi-Fi diagnostics and scanning (private framework, full path required) | `/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s` |
| `dns-sd` | DNS Service Discovery (Bonjour/mDNS) browser and registration | `dns-sd -B _http._tcp` |
| `wdutil` | Wireless diagnostics and Wi-Fi info | `sudo wdutil info` |
| `networkQuality` | Test network upload/download quality (macOS Monterey+) | `networkquality` |
| `nscurl` | NSURLSession-based curl for testing ATS (App Transport Security) | `nscurl --ats-diagnostics https://example.com` |
| `smbutil` | Query and manage SMB/CIFS network shares | `smbutil view //server` |
| `nettop` | Real-time network topology and traffic by process | `nettop -m tcp` |

---

### LaunchD & Services

| Command | Description | Example |
|---------|-------------|---------|
| `launchctl` | Manage launchd daemons and agents (macOS init system) | `launchctl list` / `launchctl load ~/Library/LaunchAgents/com.example.plist` |
| `launchd` | The macOS init and service management daemon (PID 1) | _(not invoked directly)_ |

---

### Directory Services & Accounts

| Command | Description | Example |
|---------|-------------|---------|
| `dscl` | Directory Service command line — manage users, groups, LDAP | `dscl . -list /Users` / `dscl . -read /Users/username` |
| `dscacheutil` | Query/flush the Directory Service cache | `dscacheutil -flushcache` |
| `dsmemberutil` | Query group membership | `dsmemberutil checkmembership -u username -g admin` |
| `dsexport` | Export Directory Service records | `dsexport output.plist /Local/Default dsRecTypeStandard:Users` |
| `dsimport` | Import Directory Service records | `dsimport records.plist /Local/Default M` |
| `odutil` | Open Directory utility — diagnose and manage OD connections | `odutil show configuration` |
| `pwpolicy` | Manage password policies | `sudo pwpolicy -getglobalpolicy` |

---

### Security & Keychain

| Command | Description | Example |
|---------|-------------|---------|
| `security` | Access and manage the macOS Keychain and certificates | `security find-generic-password -s "MyService"` / `security list-keychains` |
| `codesign` | Sign and verify code signatures | `codesign -s "Developer ID" MyApp.app` / `codesign -dv --verbose=4 MyApp.app` |
| `csrutil` | Manage System Integrity Protection (SIP) | `csrutil status` |
| `spctl` | System Policy Control — manage Gatekeeper | `spctl --assess --verbose MyApp.app` |
| `syspolicy_check` | Check notarization ticket status for an app | `syspolicy_check notarization-check MyApp.app` |
| `stapler` | Staple a notarization ticket to an app or dmg | `xcrun stapler staple MyApp.app` |
| `xprotect` | XProtect malware definitions management | `xprotect status` |
| `tccutil` | Manage the macOS privacy/permissions database (TCC) | `tccutil reset Camera com.example.myapp` |
| `csreq` | Create and inspect code signing requirement expressions | `csreq -r - -t <<< "identifier com.example.app"` |
| `certtool` | Create/manage certificates and keys in the Keychain | `certtool y` |
| `fdesetup` | FileVault 2 setup and management | `sudo fdesetup status` |
| `profiles` | Install, remove, and query configuration profiles | `profiles list` |
| `bputil` | Boot policy management (Apple Silicon) | `sudo bputil -d` (reduce security) |
| `devmodectl` | Enable/disable developer mode (Apple Silicon, macOS 13+) | `sudo devmodectl streaming enable` |
| `bioutil` | Manage biometric (Touch ID) configuration | `bioutil -s -c` |
| `eslogger` | Stream Endpoint Security events to stdout | `sudo eslogger exec fork` |
| `trustcachectl` | Manage the trust cache | `sudo trustcachectl check /usr/bin/swift` |

---

### Package & App Management

| Command | Description | Example |
|---------|-------------|---------|
| `softwareupdate` | macOS system software update utility | `softwareupdate -l` / `sudo softwareupdate -i -a` |
| `pkgbuild` | Build a macOS installer package (`.pkg`) | `pkgbuild --root ./payload --identifier com.example.pkg output.pkg` |
| `productbuild` | Build a macOS distribution package | `productbuild --distribution dist.xml --package-path ./pkgs output.pkg` |
| `productsign` | Sign a distribution package | `productsign --sign "Developer ID Installer" input.pkg output.pkg` |
| `installer` | Install macOS packages from the command line | `sudo installer -pkg MyPackage.pkg -target /` |
| `lsappinfo` | Query running application metadata | `lsappinfo list` |
| `pluginkit` | List and manage App Extension plugins | `pluginkit -m -A -p com.apple.share-services` |
| `swcutil` | Query the macOS software catalog | `swcutil lookup -b com.apple.finder` |
| `xcode-select` | Select the active Xcode or Command Line Tools path | `xcode-select -p` / `sudo xcode-select -s /Applications/Xcode.app` |
| `xcodebuild` | Build, test, archive Xcode projects from the command line | `xcodebuild -scheme MyApp -configuration Release build` |
| `xcrun` | Run Xcode developer tools without specifying their full path | `xcrun clang -o hello hello.c` / `xcrun simctl list` |
| `xctrace` | Record Instruments performance traces | `xctrace record --template 'Leaks' --launch -- ./myapp` |
| `agvtool` | Apple-generic versioning tool for Xcode projects | `agvtool what-version` / `agvtool bump -all` |
| `ibtool` | Compile and validate Interface Builder (`.xib`/`.storyboard`) files | `ibtool --compile out.nib MyView.xib` |
| `actool` | Compile asset catalogs (`.xcassets`) | `actool --compile ./output MyAssets.xcassets` |
| `genstrings` | Generate `.strings` localisation files from source code | `genstrings -o en.lproj *.m` |
| `xed` | Open files in Xcode from the command line | `xed .` |
| `sourcekit-lsp` | SourceKit Language Server Protocol implementation | `sourcekit-lsp` |

---

### Swift & Compiler (macOS/Apple)

| Command | Description | Example |
|---------|-------------|---------|
| `swift` | Run Swift scripts or start the Swift REPL | `swift myscript.swift` / `swift repl` |
| `swiftc` | Compile Swift source files | `swiftc -o hello hello.swift` |
| `swift-inspect` | Inspect Swift runtime metadata of a running process | `swift-inspect dump-conformance-cache $(pgrep myapp)` |
| `clang` | LLVM C/C++/Obj-C compiler (bundled with Xcode CLT) | `clang -o hello hello.c` |
| `clangd` | Clang Language Server Protocol daemon | `clangd` |
| `lldb` | LLVM debugger (default debugger on macOS) | `lldb ./myapp` |
| `dsymutil` | Manipulate debug symbol files (`.dSYM` bundles) | `dsymutil MyApp.app/Contents/MacOS/MyApp` |
| `dwarfdump` | Dump DWARF debug information from object files | `dwarfdump --all MyApp.dSYM` |
| `dyld_info` | Display dynamic library information | `dyld_info -exports /usr/lib/libSystem.B.dylib` |
| `otool` | Display object file headers and load commands | `otool -L /usr/bin/swift` |
| `lipo` | Create and inspect multi-architecture (fat) binaries | `lipo -info /usr/bin/python3` / `lipo -create x86.o arm.o -output fat.o` |
| `install_name_tool` | Modify embedded library install names in a binary | `install_name_tool -change old.dylib new.dylib myapp` |
| `nm` | List symbol table entries in object files | `nm -g /usr/lib/libSystem.B.dylib` |
| `strings` | Extract printable strings from binaries | `strings /usr/bin/ssh` |
| `strip` | Remove symbols from object files | `strip -S myapp` |
| `size` | Display the size of sections in an object file | `size /usr/bin/python3` |
| `vtool` | Display and modify version-min load commands | `vtool -show /usr/bin/clang` |
| `atos` | Translate addresses to symbol names (for crash reports) | `atos -o MyApp.dSYM/Contents/Resources/DWARF/MyApp -l 0x100000000 0x100001234` |
| `segedit` | Extract segments from a Mach-O binary | `segedit binary -extract __TEXT __text output.bin` |
| `cmpdylib` | Compare two versions of a dynamic library for compatibility | `cmpdylib libold.dylib libnew.dylib` |
| `nmedit` | Edit symbol visibility in an object file | `nmedit -p input.o` |
| `libtool` | Create static and dynamic libraries (macOS version) | `libtool -static -o libfoo.a foo.o bar.o` |
| `ranlib` | Regenerate the archive table of contents | `ranlib libfoo.a` |

---

### Automation & Scripting

| Command | Description | Example |
|---------|-------------|---------|
| `osascript` | Run AppleScript or JavaScript for Automation (JXA) | `osascript -e 'tell app "Finder" to empty trash'` |
| `osacompile` | Compile an AppleScript into a script bundle or applet | `osacompile -o script.scpt script.applescript` |
| `osadecompile` | Decompile a compiled AppleScript back to source | `osadecompile script.scpt` |
| `osalang` | List all installed OSA scripting languages | `osalang -l` |
| `automator` | Run an Automator workflow from the command line | `automator workflow.workflow` |
| `shortcuts` | Run, list, and manage Shortcuts (macOS Monterey+) | `shortcuts list` / `shortcuts run "My Shortcut"` |
| `sdef` | Extract scriptability definitions from an app | `sdef /Applications/Safari.app` |

---

### User Defaults & Preferences

| Command | Description | Example |
|---------|-------------|---------|
| `defaults` | Read and write macOS user defaults (`.plist` preferences) | `defaults read com.apple.dock` / `defaults write com.apple.finder AppleShowAllFiles YES` |
| `plutil` | Validate, convert, and lint `.plist` files | `plutil -p Info.plist` / `plutil -convert json Info.plist` |
| `PlistBuddy` | Edit `.plist` files with fine-grained key access | `/usr/libexec/PlistBuddy -c "Print :CFBundleVersion" Info.plist` |

---

### System Maintenance & Diagnostics

| Command | Description | Example |
|---------|-------------|---------|
| `tmutil` | Time Machine management (enable, backup, restore, compare) | `tmutil status` / `sudo tmutil startbackup` |
| `sysdiagnose` | Collect a comprehensive system diagnostic archive | `sudo sysdiagnose` |
| `mddiagnose` | Collect a Spotlight diagnostic report | `sudo mddiagnose` |
| `hpmdiagnose` | Collect hardware diagnostics | `sudo hpmdiagnose` |
| `wdutil` | Wireless/Wi-Fi diagnostics info collector | `sudo wdutil diagnose` |
| `nvram` | Read and write NVRAM/PRAM variables | `nvram -p` / `sudo nvram boot-args="-v"` |
| `systemextensionsctl` | Manage system extensions (kernel extensions replacement) | `systemextensionsctl list` |
| `kextutil` | Load and validate kernel extensions (deprecated in Ventura) | `sudo kextutil MyExtension.kext` |
| `kmutil` | Modern kernel collection management tool | `kmutil showloaded` |
| `notifyutil` | Post and observe macOS notification system events | `notifyutil -p com.apple.system.config.network_change` |
| `AssetCacheManagerUtil` | Manage the Content Caching service | `AssetCacheManagerUtil status` |
| `AssetCacheLocatorUtil` | Locate nearby content caches | `AssetCacheLocatorUtil` |
| `fileproviderctl` | Debug and manage File Provider extensions (iCloud Drive etc.) | `fileproviderctl status` |
| `brctl` | Diagnose CloudDocs (iCloud Drive) sync state | `brctl diagnose` / `brctl log --wait` |
| `sfltool` | Manage the shared file list (Login Items, Recent Documents) | `sfltool list` |

---

### Fonts & Typography

| Command | Description | Example |
|---------|-------------|---------|
| `atsutil` | Query the macOS font activation service | `atsutil fonts -list` |
| `fontrestore` | Restore default system fonts | `sudo fontrestore default` |

---

### Miscellaneous macOS Tools

| Command | Description | Example |
|---------|-------------|---------|
| `uuidgen` | Generate a new UUID | `uuidgen` |
| `tccutil` | Reset app privacy/permission settings | `tccutil reset Microphone com.example.app` |
| `shazam` | Identify a song playing through the microphone | `shazam` |
| `SafeEjectGPU` | Safely eject an eGPU | `SafeEjectGPU Eject` |
| `powermetrics` | Per-core CPU/GPU/DRAM power sampling | `sudo powermetrics --samplers all -n 1` |
| `opendiff` | Launch FileMerge diff from the command line | `opendiff file1.txt file2.txt` |
| `xip` | Create and verify `.xip` secure archives | `xip --sign "Developer ID" --timestamp MyFiles.xip` |
| `DeRez` | Decompile resource forks to Rez source (legacy) | `DeRez -only 'icns' myapp` |
| `Rez` | Compile Rez resource description files (legacy) | `Rez -o output MyResources.r` |
| `app-sso` | Inspect and reset Enterprise SSO plugin sessions | `app-sso -l` |
| `mcxquery` | Query Managed Client Extension (MCX) settings | `mcxquery -user username` |
| `usdcat` | Convert/combine Universal Scene Description files | `usdcat input.usd --out output.usda` |
| `usdchecker` | Validate a USD file for compliance | `usdchecker scene.usd` |

---

## Part 2 — Linux Standard / BSD Commands (also on macOS)

> These commands are standard on Linux and available on macOS. Most are BSD implementations — check `man` pages for flag differences.

### Navigation & File Management

| Command | Description | Example |
|---------|-------------|---------|
| `ls` | List directory contents | `ls -lahG` |
| `pwd` | Print working directory | `pwd` |
| `cd` | Change directory | `cd ~/Projects` |
| `pushd` / `popd` | Push/pop the directory stack | `pushd /tmp && popd` |
| `cp` | Copy files and directories | `cp -r src/ dst/` |
| `mv` | Move or rename files | `mv old.txt new.txt` |
| `rm` | Remove files or directories | `rm -rf build/` |
| `mkdir` | Create directories | `mkdir -p a/b/c` |
| `rmdir` | Remove empty directories | `rmdir emptydir` |
| `touch` | Create empty files or update timestamps | `touch newfile.txt` |
| `ln` | Create hard or symbolic links | `ln -s /usr/local/bin/node node` |
| `find` | Search for files by name, type, date, size, etc. | `find . -name "*.log" -mtime +7` |
| `locate` | Fast filename search using a pre-built index | `locate nginx.conf` |
| `tree` | Display directory tree (if installed) | `tree -L 2 src/` |
| `stat` | Display detailed file metadata | `stat myfile.txt` |
| `file` | Determine the type of a file | `file unknown.bin` |
| `readlink` | Print resolved symlink path | `readlink -f /usr/bin/python3` |
| `basename` | Strip directory and suffix from a path | `basename /usr/local/bin/node` |
| `dirname` | Extract directory component of a path | `dirname /usr/local/bin/node` |
| `realpath` / `resolveLinks` | Resolve the canonical absolute path | `realpath ./relative/path` |

---

### Text Processing

| Command | Description | Example |
|---------|-------------|---------|
| `cat` | Concatenate and print file contents | `cat file.txt` |
| `less` | Page through file contents interactively | `less largefile.log` |
| `more` | Simpler pager | `more file.txt` |
| `head` | Print the first N lines of a file | `head -20 access.log` |
| `tail` | Print the last N lines; `-f` follows live output | `tail -f /var/log/system.log` |
| `grep` | Search text with regular expressions | `grep -rn "TODO" src/` |
| `egrep` / `fgrep` | Extended regex grep / fixed-string grep | `egrep "(foo\|bar)" file.txt` |
| `awk` | Pattern scanning and text processing language | `awk '{print $1, $3}' data.csv` |
| `sed` | Stream editor for text transformation | `sed 's/foo/bar/g' file.txt` |
| `cut` | Extract columns from delimited text | `cut -d',' -f1,3 data.csv` |
| `paste` | Merge lines from multiple files | `paste file1.txt file2.txt` |
| `join` | Join lines from two files on a common field | `join -1 1 -2 1 a.txt b.txt` |
| `sort` | Sort lines of text | `sort -k2 -n data.txt` |
| `uniq` | Remove or report duplicate lines | `sort file.txt \| uniq -c` |
| `wc` | Count lines, words, and characters | `wc -l *.py` |
| `tr` | Translate or delete characters | `echo "HELLO" \| tr 'A-Z' 'a-z'` |
| `col` | Filter reverse line feeds | `nroff -man page.1 \| col -b` |
| `colrm` | Remove columns from a file | `colrm 10 20 file.txt` |
| `column` | Format output into aligned columns | `column -t -s',' data.csv` |
| `fmt` | Reformat paragraph text to a given width | `fmt -w 72 essay.txt` |
| `fold` | Wrap lines to a specified width | `fold -s -w 80 longtext.txt` |
| `expand` / `unexpand` | Convert tabs to spaces / spaces to tabs | `expand -t 4 file.py` |
| `rev` | Reverse each line character by character | `echo "hello" \| rev` |
| `diff` | Compare two files line by line | `diff -u original.txt modified.txt` |
| `diff3` | Three-way file comparison | `diff3 mine.txt base.txt theirs.txt` |
| `sdiff` | Side-by-side file diff | `sdiff file1.txt file2.txt` |
| `patch` | Apply a diff/patch file | `patch < changes.patch` |
| `vimdiff` | Diff two files in Vim | `vimdiff original.txt modified.txt` |
| `od` | Dump file in octal, hex, or other formats | `od -An -tx1 binary.bin` |
| `xxd` | Hex dump and reverse hex dump | `xxd binary.bin` / `xxd -r hex.txt binary.bin` |
| `hexdump` | Display file in hex/ASCII format | `hexdump -C binary.bin \| head` |
| `strings` | Extract printable strings from a binary file | `strings /usr/bin/ls` |
| `iconv` | Convert text between character encodings | `iconv -f UTF-16 -t UTF-8 input.txt` |
| `printf` | Format and print data (more portable than `echo`) | `printf "%-10s %d\n" "item" 42` |
| `echo` | Print a line of text | `echo "Hello, world"` |
| `bc` | Arbitrary-precision calculator | `echo "scale=2; 22/7" \| bc` |
| `dc` | Reverse-Polish notation desk calculator | `echo "5 3 + p" \| dc` |
| `expr` | Evaluate expressions | `expr 10 \* 5` |
| `xargs` | Build and execute commands from stdin | `find . -name "*.bak" \| xargs rm` |

---

### File Content & Encoding

| Command | Description | Example |
|---------|-------------|---------|
| `base64` | Encode or decode base64 | `base64 image.png \| head` / `base64 -d encoded.txt` |
| `b64encode` / `b64decode` | BSD base64 variants | `b64encode -r image.png` |
| `uuencode` / `uudecode` | UUencode/decode files | `uuencode file.bin file.bin > encoded.txt` |
| `binhex` | BinHex encode (also listed above; BSD utility) | `binhex file` |
| `compress` / `uncompress` | Lempel-Ziv compression (legacy `.Z` format) | `compress file.txt` |
| `gzip` / `gunzip` | GNU zip compression | `gzip -9 archive.tar` |
| `bzip2` / `bunzip2` | BZip2 compression | `bzip2 -k file.txt` |
| `zcat` / `bzcat` | Decompress to stdout without writing a file | `zcat archive.gz \| head` |
| `zip` / `unzip` | Zip archive creation and extraction | `zip -r output.zip dir/` / `unzip archive.zip` |
| `tar` | Tape archive — bundle, compress, and extract files | `tar czf archive.tar.gz dir/` / `tar xzf archive.tar.gz` |
| `cpio` | Copy files to/from archives | `find . -print \| cpio -o > archive.cpio` |
| `bsdtar` | BSD implementation of tar (same as `tar` on macOS) | `bsdtar xf archive.tar` |
| `shasum` | Compute SHA-1/224/256/384/512 checksums | `shasum -a 256 file.iso` |
| `cksum` / `sum` | Compute checksums | `cksum file.txt` |
| `md5` | Compute MD5 digest (BSD; use `md5sum` on Linux) | `md5 file.iso` |
| `crc32` | Compute CRC32 checksum | `crc32 file.bin` |

---

### Shell & Job Control

| Command | Description | Example |
|---------|-------------|---------|
| `bash` / `sh` / `zsh` | Shell interpreters | `bash script.sh` |
| `env` | Run a command in a modified environment | `env PATH=/usr/local/bin:$PATH make` |
| `export` | Set environment variables | `export NODE_ENV=production` |
| `alias` | Create command aliases | `alias ll='ls -lahG'` |
| `type` | Show how a command name is interpreted | `type grep` |
| `which` | Locate the executable for a command | `which python3` |
| `whereis` | Find binary, source, and man page locations | `whereis git` |
| `hash` | Show/clear the shell's command location cache | `hash -r` |
| `jobs` | List background and suspended jobs | `jobs -l` |
| `bg` | Resume a job in the background | `bg %1` |
| `fg` | Bring a background job to the foreground | `fg %1` |
| `nohup` | Run a command immune to hangups | `nohup ./server &` |
| `disown` | Remove a job from the shell's job table | `disown %1` |
| `wait` | Wait for background processes to finish | `wait $PID` |
| `kill` | Send a signal to a process | `kill -9 $PID` |
| `killall` | Kill processes by name | `killall node` |
| `pkill` / `pgrep` | Kill/find processes by name pattern | `pkill -f "python server"` |
| `screen` | Terminal multiplexer with persistent sessions | `screen -S mysession` |
| `tmux` | Modern terminal multiplexer (install via Homebrew) | `tmux new -s dev` |
| `time` | Measure how long a command takes | `time make` |
| `ulimit` | Get/set resource limits for the shell | `ulimit -n 4096` |

---

### Process Management

| Command | Description | Example |
|---------|-------------|---------|
| `ps` | Show running processes | `ps aux` / `ps -ef` |
| `top` | Interactive process monitor | `top -o cpu` |
| `kill` | Send a signal to a process by PID | `kill -TERM 1234` |
| `nice` | Run a command with modified scheduling priority | `nice -n 10 make` |
| `renice` | Change the priority of a running process | `renice -n 5 -p $PID` |
| `lsof` | List open files and the processes using them | `lsof -i :8080` |
| `fuser` | Identify processes using a file or socket | `fuser 8080/tcp` |
| `uptime` | Show how long the system has been running + load avg | `uptime` |
| `w` | Show who is logged in and what they are doing | `w` |
| `who` / `whoami` | Print logged-in users / current user | `whoami` |
| `id` | Print user and group IDs | `id` |
| `last` | Show recent login history | `last -10` |
| `users` | List currently logged-in usernames | `users` |

---

### Scheduling

| Command | Description | Example |
|---------|-------------|---------|
| `cron` | Daemon for time-based job scheduling | _(run by the system)_ |
| `crontab` | Edit the cron table for scheduled jobs | `crontab -e` / `crontab -l` |
| `at` | Schedule a one-time command | `echo "say done" \| at now + 5 minutes` |
| `atq` | List pending `at` jobs | `atq` |
| `atrm` | Remove a pending `at` job | `atrm 3` |

---

### Networking (Standard)

| Command | Description | Example |
|---------|-------------|---------|
| `curl` | Transfer data with URLs (HTTP, FTP, etc.) | `curl -sSL https://example.com` |
| `wget` | Download files from the web *(not installed by default — use Homebrew)* | `wget https://example.com/file.tar.gz` |
| `ssh` | Secure shell remote login | `ssh user@host` |
| `scp` | Securely copy files over SSH | `scp file.txt user@host:/remote/path/` |
| `sftp` | Interactive secure file transfer | `sftp user@host` |
| `rsync` | Fast, incremental file synchronisation over SSH or local | `rsync -avz src/ user@host:/dst/` |
| `nc` (netcat) | TCP/UDP Swiss army knife — port scan, chat, proxy | `nc -zv host 80` / `nc -l 9090` |
| `ping` | Send ICMP echo requests to test connectivity | `ping -c 4 google.com` |
| `traceroute` | Trace the route packets take to a host | `traceroute google.com` |
| `dig` | DNS query tool | `dig A example.com` / `dig @8.8.8.8 example.com` |
| `nslookup` | Interactive DNS query (older) | `nslookup example.com` |
| `host` | Simple DNS lookup | `host example.com` |
| `delv` | DNSSEC-validating DNS lookup | `delv example.com` |
| `nsupdate` | Dynamic DNS update utility | `nsupdate -v update.txt` |
| `netstat` | Network connections, routing tables, interface stats | `netstat -antp` |
| `ifconfig` | Configure network interfaces | `ifconfig en0` |
| `arp` | Manipulate the ARP cache | `arp -a` |
| `route` | View/manipulate the IP routing table | `netstat -rn` |
| `nfsstat` | NFS statistics | `nfsstat -c` |
| `showmount` | Show NFS exports from a server | `showmount -e server` |
| `tftp` | Trivial FTP client | `tftp 192.168.1.1` |
| `telnet` | Telnet client (also useful for testing ports) | `telnet host 25` |
| `whois` | Query WHOIS domain registration info | `whois example.com` |
| `fping` | Ping multiple hosts at once | `fping -a -g 192.168.1.0/24` |
| `iperf3` | Network bandwidth measurement | `iperf3 -c server_host` |
| `snmpwalk` | Walk an SNMP MIB tree | `snmpwalk -v2c -c public localhost` |
| `ldapsearch` | Search an LDAP directory | `ldapsearch -H ldap://host -b "dc=example,dc=com"` |
| `openssl` | Swiss army knife for TLS/SSL, certs, crypto | `openssl s_client -connect example.com:443` |
| `ssh-keygen` | Generate SSH key pairs | `ssh-keygen -t ed25519 -C "email@example.com"` |
| `ssh-add` | Add SSH keys to the agent | `ssh-add ~/.ssh/id_ed25519` |
| `ssh-agent` | SSH authentication agent | `eval $(ssh-agent)` |

---

### Disk & Storage

| Command | Description | Example |
|---------|-------------|---------|
| `df` | Report disk space usage on mounted filesystems | `df -h` |
| `du` | Estimate file and directory space usage | `du -sh */ \| sort -rh` |
| `mount` / `umount` | Mount and unmount filesystems | `mount -t hfs /dev/disk2s1 /mnt` |
| `dd` | Low-level copy and convert — create disk images, wipe | `sudo dd if=/dev/disk2 of=backup.img bs=4m` |
| `fsck` | Filesystem check and repair | `sudo fsck_apfs /dev/disk1s1` |
| `sync` | Flush filesystem write buffers to disk | `sync` |

---

### Permissions & Ownership

| Command | Description | Example |
|---------|-------------|---------|
| `chmod` | Change file/directory permissions | `chmod 755 script.sh` / `chmod +x deploy.sh` |
| `chown` | Change file owner and group | `chown user:group file.txt` |
| `chgrp` | Change the group ownership | `chgrp staff file.txt` |
| `chflags` | Change BSD file flags (macOS/BSD feature) | `chflags hidden file.txt` |
| `umask` | Set the default permission mask | `umask 022` |
| `sudo` | Execute a command as another user (typically root) | `sudo rm /private/etc/hosts` |
| `su` | Switch user | `su - username` |
| `newgrp` | Log in to a new group | `newgrp staff` |

---

### Build & Development Tools

| Command | Description | Example |
|---------|-------------|---------|
| `make` / `gnumake` | Build automation using Makefiles | `make clean && make -j4` |
| `gcc` / `g++` | GNU C/C++ compiler (via Command Line Tools) | `gcc -o hello hello.c` |
| `cc` / `c++` | Alias for the system C/C++ compiler | `cc -Wall -o out main.c` |
| `ar` | Create, modify, and extract from archives (static libs) | `ar rcs libfoo.a foo.o` |
| `as` | Assembler | `as -o hello.o hello.s` |
| `ld` | Linker | `ld -o hello hello.o -lSystem` |
| `cpp` | C preprocessor | `cpp -DDEBUG main.c` |
| `m4` / `gm4` | Macro processor | `m4 template.m4` |
| `bison` | YACC-compatible parser generator | `bison -d grammar.y` |
| `flex` | Fast lexical analyser generator | `flex scanner.l` |
| `gperf` | Perfect hash function generator | `gperf keywords.gperf` |
| `indent` | Reformat C source code | `indent -kr file.c` |
| `ctags` | Generate tags index for source files | `ctags -R src/` |
| `git` | Distributed version control | `git log --oneline -10` |
| `python3` | Python 3 interpreter | `python3 -m http.server 8080` |
| `pip3` | Python 3 package manager | `pip3 install requests` |
| `ruby` | Ruby interpreter | `ruby -e 'puts "hello"'` |
| `gem` | Ruby package manager | `gem install bundler` |
| `rails` / `rake` | Ruby on Rails / Ruby build tool | `rails new myapp` |
| `perl` | Perl interpreter | `perl -pe 's/foo/bar/g' file.txt` |
| `irb` | Interactive Ruby REPL | `irb` |
| `rdoc` | Ruby documentation generator | `rdoc lib/` |
| `sqlite3` | SQLite3 command-line client | `sqlite3 mydb.db` |
| `jq` | Command-line JSON processor | `curl -s api/endpoint \| jq '.items[]'` |
| `xmllint` | Validate and query XML/HTML documents | `xmllint --format page.html` |
| `xsltproc` | Apply XSLT stylesheets to XML | `xsltproc style.xsl input.xml` |
| `java` / `javac` | JVM runtime / Java compiler | `javac Hello.java && java Hello` |

---

### Manual & Help

| Command | Description | Example |
|---------|-------------|---------|
| `man` | Display manual pages | `man grep` |
| `apropos` | Search manual page descriptions by keyword | `apropos certificate` |
| `whatis` | Show a one-line description of a command | `whatis find` |
| `help` | Show built-in shell command help | `help cd` |
| `info` | Read Info documentation (GNU) | `info make` |

---

### Miscellaneous Standard Tools

| Command | Description | Example |
|---------|-------------|---------|
| `uname` | Print OS name and version | `uname -a` |
| `hostname` | Print or set the system hostname | `hostname` |
| `date` | Print or set the system date/time | `date "+%Y-%m-%d %H:%M:%S"` |
| `cal` | Display a calendar | `cal 2026` |
| `banner` | Print a large ASCII banner | `banner "Hello"` |
| `seq` | Print a sequence of numbers | `seq 1 10` |
| `yes` | Print a string repeatedly until killed | `yes \| head -5` |
| `true` / `false` | Return exit code 0 or 1 | `true && echo "ok"` |
| `sleep` | Pause for a given number of seconds | `sleep 2 && notify` |
| `tee` | Read stdin and write to both stdout and a file | `make 2>&1 \| tee build.log` |
| `watch` | Run a command repeatedly *(install via Homebrew on macOS)* | `watch -n 2 df -h` |
| `script` | Record a terminal session to a file | `script session.log` |
| `tty` | Print the filename of the connected terminal | `tty` |
| `stty` | Set terminal I/O options | `stty -a` |
| `reset` | Reset/reinitialise the terminal | `reset` |
| `clear` | Clear the terminal screen | `clear` |
| `locale` | Show locale/internationalisation settings | `locale` |
| `units` | Convert between units of measurement | `units "60 mph" "km/h"` |
| `bc` | Arbitrary precision calculator | `echo "2^64" \| bc` |
| `lp` / `lpr` | Print files via CUPS | `lpr -P printer file.pdf` |
| `lpq` / `lprm` | Show/manage the print queue | `lpq` |
| `at` | Schedule one-time jobs | `echo "say wake up" \| at 09:00 AM` |
| `logger` | Write messages to the system log | `logger "deployment started"` |
| `wall` | Broadcast a message to all logged-in users | `wall "Server rebooting in 5 minutes"` |
| `write` / `talk` | Send messages to other terminal sessions | `write username` |
| `mesg` | Enable/disable receiving messages | `mesg n` |
| `finger` | Look up information about a user | `finger username` |
| `leave` | Remind yourself to leave at a set time | `leave 1700` |
| `lock` | Lock the terminal | `lock` |
| `tabs` | Set tab stops on a terminal | `tabs 4` |
| `tput` | Query and set terminal capabilities | `tput cols` / `tput setaf 2` |

---

*Verified against macOS 15.7.4 (Sequoia) with Xcode Command Line Tools installed. Third-party tools (VS Code `code`, VirtualBox, Homebrew packages) are excluded.*
