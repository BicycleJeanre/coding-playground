# Arduino Uno — Getting Started Guide (Mac M1)

---

## What is Arduino Uno?

The **Arduino Uno** is an open-source microcontroller board based on the **ATmega328P** chip. It is one of the most popular boards in the Arduino family and is ideal for beginners and prototyping.

### Key Specs

| Feature | Detail |
|---|---|
| Microcontroller | ATmega328P |
| Operating Voltage | 5V |
| Digital I/O Pins | 14 (6 PWM capable) |
| Analog Input Pins | 6 |
| Flash Memory | 32 KB |
| SRAM | 2 KB |
| EEPROM | 1 KB |
| Clock Speed | 16 MHz |
| USB Connection | Type-B |

---

## Board Overview

```
                  ┌─────────────────────────────┐
     USB Type-B ──┤                             ├── Power Jack (7–12V)
                  │        Arduino Uno          │
   Digital Pins ──┤  0–13  (PWM: 3,5,6,9,10,11) ├── Analog Pins A0–A5
                  │                             │
         Reset ───┤  [RST]          ATmega328P  │
                  └─────────────────────────────┘
```

### Important Pin Types

- **Digital Pins (0–13)** — Read or write HIGH/LOW signals
- **PWM Pins (~3, ~5, ~6, ~9, ~10, ~11)** — Simulate analog output via Pulse Width Modulation
- **Analog Pins (A0–A5)** — Read analog voltages (0–5V mapped to 0–1023)
- **Power Pins** — 3.3V, 5V, GND, Vin
- **UART (0, 1)** — Serial communication (TX/RX)
- **I2C (A4, A5)** — SDA/SCL for I2C devices
- **SPI (10, 11, 12, 13)** — SS, MOSI, MISO, SCK

---

## Installation on Mac M1 (Apple Silicon)

### Step 1 — Download Arduino IDE 2

1. Go to [https://www.arduino.cc/en/software](https://www.arduino.cc/en/software)
2. Under **Download Options**, select **macOS Apple Silicon** (the `.dmg` for ARM64)
3. Download and open the `.dmg` file
4. Drag **Arduino IDE** into your `/Applications` folder

> **Important:** Do NOT download the Intel version — it will run under Rosetta but may cause driver and port detection issues on M1.

---

### Step 2 — Launch the Arduino IDE

1. Open **Finder > Applications**
2. Double-click **Arduino IDE**
3. On first launch, macOS may show a security prompt — click **Open** to allow it
4. The IDE will install additional required components automatically on first run

---

### Step 3 — Install the CH340 Driver (Clone Boards Only)

Some clone Arduino Uno boards use a **CH340G** USB chip instead of the official ATmega16U2. M1 Macs may not recognize this chip without an additional driver.

**To check your board's chip:** Look near the USB port — it will say either `ATmega16U2`, `CH340`, or `CH341`.

#### Official Uno (ATmega16U2) — No extra driver needed
macOS includes native support. Plug in and proceed to Step 4.

#### Clone Uno (CH340/CH341) — Install CH340 driver

1. Download the driver from: [https://github.com/adrianmihalko/ch340g-ch34g-ch34x-mac-os-x-driver](https://github.com/adrianmihalko/ch340g-ch34g-ch34x-mac-os-x-driver)
2. Run the `.pkg` installer
3. Go to **System Settings > Privacy & Security** and allow the driver extension
4. Restart your Mac
5. Reconnect your Arduino

---

### Step 4 — Connect the Board

1. Connect your Arduino Uno to your Mac via **USB Type-B cable**
2. Open **Arduino IDE**
3. Go to **Tools > Board > Arduino AVR Boards > Arduino Uno**
4. Go to **Tools > Port** and select the port that shows:
   - `/dev/cu.usbmodem...` (official Uno)
   - `/dev/cu.wchusbserial...` (CH340 clone)

---

### Step 5 — Upload Your First Sketch (Blink)

The **Blink** sketch is the "Hello World" of Arduino.

1. In the IDE, go to **File > Examples > 01.Basics > Blink**
2. The following code will open:

```cpp
void setup() {
  pinMode(LED_BUILTIN, OUTPUT); // Set built-in LED pin as output
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH); // Turn LED on
  delay(1000);                     // Wait 1 second
  digitalWrite(LED_BUILTIN, LOW);  // Turn LED off
  delay(1000);                     // Wait 1 second
}
```

3. Click the **Upload** button (right arrow icon) or press `Cmd + U`
4. Wait for **"Done uploading"** in the status bar
5. The built-in LED on your board (labeled **L**) will start blinking every second

---

## Core Concepts

### `setup()` vs `loop()`

```cpp
void setup() {
  // Runs ONCE when the board powers on or resets
  // Use for: pin modes, Serial.begin(), initializing libraries
}

void loop() {
  // Runs FOREVER in a continuous loop
  // Use for: reading sensors, controlling outputs, logic
}
```

### Digital Read / Write

```cpp
pinMode(7, OUTPUT);          // Set pin 7 as output
digitalWrite(7, HIGH);       // Set pin 7 to 5V (on)
digitalWrite(7, LOW);        // Set pin 7 to 0V (off)

pinMode(2, INPUT_PULLUP);    // Set pin 2 as input with internal pull-up
int state = digitalRead(2);  // Read HIGH or LOW
```

### Analog Read

```cpp
int value = analogRead(A0);               // Returns 0–1023 (maps 0–5V)
float voltage = value * (5.0 / 1023.0);  // Convert to volts
```

### PWM (Analog-like Output)

```cpp
analogWrite(9, 128); // Write ~50% duty cycle to PWM pin 9 (range: 0–255)
```

### Serial Monitor

```cpp
void setup() {
  Serial.begin(9600); // Start serial communication at 9600 baud
}

void loop() {
  Serial.println("Hello from Arduino!"); // Print to Serial Monitor
  delay(1000);
}
```

Open the **Serial Monitor** with `Cmd + Shift + M` or via **Tools > Serial Monitor**.

---

## Power Options

| Method | Voltage Range | Notes |
|---|---|---|
| USB (Type-B) | 5V | Easiest — powers via computer |
| DC Barrel Jack | 7–12V | Use a regulated wall adapter |
| Vin Pin | 7–12V | Same as barrel jack, via pin |
| 3.3V / 5V Pins | Fixed | Output only — do not use as input power |

---

## Troubleshooting on Mac M1

| Problem | Solution |
|---|---|
| Port not showing in IDE | Check driver (CH340 vs ATmega16U2), try a different USB cable |
| `avrdude: stk500_recv(): programmer is not responding` | Wrong port selected, or board not recognized — unplug and replug |
| Security warning on driver install | Go to System Settings > Privacy & Security > allow the extension |
| Upload fails intermittently | Try a shorter/better USB cable; avoid USB hubs |
| IDE crashes on launch | Re-download the ARM64 version of Arduino IDE 2 |

---

## Useful Resources

- Official Docs: [https://docs.arduino.cc](https://docs.arduino.cc)
- Language Reference: [https://www.arduino.cc/reference/en](https://www.arduino.cc/reference/en)
- Arduino Forum: [https://forum.arduino.cc](https://forum.arduino.cc)
- Project Hub: [https://projecthub.arduino.cc](https://projecthub.arduino.cc)

---

*Guide written for Arduino IDE 2.x on macOS (Apple Silicon / M1)*
