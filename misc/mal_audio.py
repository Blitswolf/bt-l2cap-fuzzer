"""
screech.py — generate an unpleasant tone from maths and play it live.

No audio file involved. A tone is just a sine wave computed sample by
sample, then handed to your sound output (which routes to whatever
speaker is connected — including a Bluetooth one).

Install the two dependencies first:
    pip install numpy sounddevice
"""

import numpy as np
import sounddevice as sd

# --- settings you can play with -------------------------------------
SAMPLE_RATE = 44100     # samples per second (CD quality)
DURATION    = 3.0       # seconds
VOLUME      = 0.3       # 0.0 to 1.0 — START LOW, your ears will thank you
FREQ        = 3000      # Hz. 2000-4000 is where hearing is most sensitive


def tone(freq, duration, volume):
    """Build a plain sine-wave tone.

    The core line is the sine formula:
        sample = volume * sin(2*pi * freq * t)
    where t is an array of time points. numpy does it for every sample
    at once instead of looping.
    """
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    wave = volume * np.sin(2 * np.pi * freq * t)
    return wave.astype(np.float32)


def screech(duration, volume):
    """A nastier version: two close frequencies that 'beat' against each
    other, plus a harsh higher harmonic. Deliberately grating."""
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    a = np.sin(2 * np.pi * 3000 * t)          # base piercing tone
    b = np.sin(2 * np.pi * 3007 * t)          # 7 Hz off -> wobbling beat
    c = 0.5 * np.sin(2 * np.pi * 6000 * t)    # harsh harmonic on top
    wave = volume * (a + b + c) / 2.5         # mix and keep it in range
    return wave.astype(np.float32)


if __name__ == "__main__":
    # Swap tone(...) for screech(...) to switch between the two.
    audio = screech(DURATION, VOLUME)
    print(f"Playing for {DURATION}s at volume {VOLUME}. Ctrl+C to stop.")
    sd.play(audio, SAMPLE_RATE)
    sd.wait()   # block until it finishes
    print("Done.")