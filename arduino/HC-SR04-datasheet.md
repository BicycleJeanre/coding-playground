# HC-SR04 Ultrasonic Distance Sensor — Datasheet & Reference

---

## Overview

The **HC-SR04** is an ultrasonic ranging module that uses sonar to measure the distance to an object. It emits a 40kHz ultrasonic pulse, waits for the echo to
return, and outputs the travel time as a pulse width on the Echo pin. It is commonly used in Arduino robotics, obstacle detection, and level sensing projects.

---

## Electrical Specifications

| Parameter                 | Value                              |
| ------------------------- | ---------------------------------- |
| Power Supply              | +5V DC                             |
| Quiescent Current         | < 2mA                              |
| Working Current           | 15mA                               |
| Operating Frequency       | 40kHz                              |
| Ranging Distance          | 2cm – 400cm (0.8in – 157in)        |
| Resolution                | 0.3cm                              |
| Measuring Angle           | 30° (effectual angle < 15°)        |
| Trigger Input Pulse Width | 10µS TTL pulse                     |
| Echo Output Signal        | TTL pulse proportional to distance |
| Dimensions                | 45mm × 20mm × 15mm                 |

---

## Pinout

```
  ┌──────────────────────────────────┐
  │  [O]           [O]               │
  │  TX            RX                │
  │                                  │
  │  VCC   TRIG   ECHO   GND        │
  └──┬──────┬──────┬──────┬──────────┘
     1      2      3      4
```

| Pin | Name     | Direction | Description                                                                             |
| --- | -------- | --------- | --------------------------------------------------------------------------------------- |
| 1   | **VCC**  | Power In  | Connect to **+5V DC**                                                                   |
| 2   | **TRIG** | Input     | Trigger pin — receives the 10µS pulse from the microcontroller to start a measurement   |
| 3   | **ECHO** | Output    | Echo pin — outputs a HIGH pulse whose duration is proportional to the measured distance |
| 4   | **GND**  | Ground    | Connect to GND                                                                          |

> **Note:** From the Arduino's perspective, TRIG is set as `OUTPUT` and ECHO is set as `INPUT`.

---

## How It Works

### Step-by-Step Sequence

1. The microcontroller sends a **10µS HIGH pulse** on the **TRIG** pin
2. The module emits **8 cycles of 40kHz ultrasonic sound** from the transmitter (TX)
3. The sound travels through the air and reflects off the nearest object
4. The receiver (RX) picks up the reflected echo
5. The **ECHO** pin goes HIGH for the duration of the round-trip travel time
6. The microcontroller measures the pulse width and calculates distance

### Timing Diagram

```time
TRIG:  _____|‾‾10µS‾‾‾|________________________________________
ECHO:  ______________|‾|‾|‾|‾‾‾ travel time (T) ‾‾‾‾‾|__________
```
```time
  |log start ---- read echo On? ------ log end time ---- echo off? 
  |


```
---

## Distance Calculation

The speed of sound in air at 20°C is **343 m/s** (0.0343 cm/µS).

Since the pulse travels **to the object AND back**, divide travel time by 2:

$$\text{distance} = \frac{\text{travel time (µS)}}{2} \times 0.0343 \text{ cm/µS}$$

Or using the commonly used integer shorthand:

$$\text{distance (cm)} = \frac{\text{duration (µS)}}{2 \times 29.1}$$

$$\text{distance (inches)} = \frac{\text{duration (µS)}}{2 \times 74}$$

---

## Wiring to Arduino Uno

| HC-SR04 Pin | Arduino Uno Pin |
| ----------- | --------------- |
| VCC         | 5V              |
| TRIG        | Pin 11          |
| ECHO        | Pin 12          |
| GND         | GND             |

---

## Arduino Code — No Library

```cpp
int trigPin = 11;
int echoPin = 12;
long duration, cm, inches;

void setup() {
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  // Send a clean 10µS HIGH pulse on TRIG
  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Measure how long ECHO stays HIGH (in microseconds)
  duration = pulseIn(echoPin, HIGH);

  // Convert to distance
  cm     = (duration / 2) / 29.1;
  inches = (duration / 2) / 74;

  Serial.print(inches);
  Serial.print("in,  ");
  Serial.print(cm);
  Serial.println("cm");

  delay(250);
}
```

---

## Arduino Code — With NewPing Library

Install **NewPing** via Library Manager or download from:
[https://bitbucket.org/teckel12/arduino-new-ping](https://bitbucket.org/teckel12/arduino-new-ping/get/master.zip)

```cpp
#include <NewPing.h>

#define TRIGGER_PIN  11
#define ECHO_PIN     12
#define MAX_DISTANCE 200  // Maximum distance in cm

NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE);

void setup() {
  Serial.begin(9600);
}

void loop() {
  delay(50);
  unsigned int distance = sonar.ping_cm();  // Returns distance in cm
  Serial.print(distance);
  Serial.println("cm");
}
```

> Use `sonar.ping_in()` to get the result in inches instead.

---

## Using Two Sensors

Assign separate TRIG/ECHO pins for each sensor:

```cpp
int trigPin1 = 11,  echoPin1 = 12;
int trigPin2 = 9,   echoPin2 = 10;
long duration1, cm1, duration2, cm2;

void setup() {
  Serial.begin(9600);
  pinMode(trigPin1, OUTPUT); pinMode(echoPin1, INPUT);
  pinMode(trigPin2, OUTPUT); pinMode(echoPin2, INPUT);
}

void loop() {
  // Sensor 1
  digitalWrite(trigPin1, LOW);  delayMicroseconds(5);
  digitalWrite(trigPin1, HIGH); delayMicroseconds(10);
  digitalWrite(trigPin1, LOW);
  duration1 = pulseIn(echoPin1, HIGH);
  cm1 = (duration1 / 2) / 29.1;

  // Sensor 2
  digitalWrite(trigPin2, LOW);  delayMicroseconds(5);
  digitalWrite(trigPin2, HIGH); delayMicroseconds(10);
  digitalWrite(trigPin2, LOW);
  duration2 = pulseIn(echoPin2, HIGH);
  cm2 = (duration2 / 2) / 29.1;

  Serial.print("Sensor 1: "); Serial.print(cm1); Serial.println("cm");
  Serial.print("Sensor 2: "); Serial.print(cm2); Serial.println("cm");
  delay(250);
}
```

> **Note:** The Arduino Uno has 14 digital pins — each HC-SR04 uses 2, so you can connect up to **7 sensors** in theory (leaving pins 0/1 for Serial).

---

## Important Notes & Gotchas

### `pulseIn()` Timeout

If no echo is received (e.g. the target is out of range or no object present), `pulseIn()` will **block for up to 1 second** by default. Use the timeout
parameter to avoid hangs:

```cpp
duration = pulseIn(echoPin, HIGH, 25000); // 25ms timeout (~4.3m max)
```

### TRIG Pin Pull-up Behavior

The TRIG pin has an internal 10kΩ pull-up resistor on many modules. When nothing is connected, it floats HIGH — always drive it LOW before sending a trigger
pulse.

### Cheap Clone Warning

Low-cost HC-SR04 clones (< $1) may **lack a timeout** on the echo pin. If no return echo is detected, the Echo pin can stay HIGH indefinitely, locking up
`pulseIn()`. Symptoms:

- Works fine, then stops responding
- Touching the sensor or making a loud sound near it "unlocks" it
- Power cycling the sensor restores function

**Fix:** Use a transistor to software-control power to the sensor, or buy from a reputable supplier (~$2 units from established sellers typically include the
36ms timeout).

### Minimum Distance

The sensor has a **blind zone of ~2cm**. Objects closer than 2cm may not be detected reliably. Some clones have an even larger blind zone.

### Measurement Rate

Trigger the sensor **no faster than every 60ms** (~16Hz) to avoid the outgoing pulse interfering with the incoming echo. Using the NewPing library handles this
automatically.

### Angle

The beam has an effective angle of ~15° either side of center (30° total cone). Objects significantly off-axis may not reflect enough sound back to the
receiver.

---

## Troubleshooting

| Symptom                      | Likely Cause               | Solution                                               |
| ---------------------------- | -------------------------- | ------------------------------------------------------ |
| Always reads 0               | Wrong pin, broken sensor   | Check wiring; swap sensor                              |
| Always reads max distance    | No echo received, timeout  | Add `pulseIn` timeout; check for obstructions          |
| Erratic readings             | Interference, bad cable    | Keep wires short; add 100µF cap on VCC                 |
| Sensor locks up and stops    | Clone with no echo timeout | Add timeout to `pulseIn()`; power-cycle via transistor |
| Serial monitor shows garbage | Baud rate mismatch         | Match `Serial.begin()` baud to Serial Monitor dropdown |

---

## Resources

- Arduino `pulseIn()` reference:
  [https://www.arduino.cc/reference/en/language/functions/advanced-io/pulsein/](https://www.arduino.cc/reference/en/language/functions/advanced-io/pulsein/)
- NewPing library: [https://bitbucket.org/teckel12/arduino-new-ping](https://bitbucket.org/teckel12/arduino-new-ping)
- Full guide (Random Nerd Tutorials):
  [https://randomnerdtutorials.com/complete-guide-for-ultrasonic-sensor-hc-sr04/](https://randomnerdtutorials.com/complete-guide-for-ultrasonic-sensor-hc-sr04/)

---

_Reference compiled from HC-SR04 datasheet and verified community documentation._
