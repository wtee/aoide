#! /usr/bin/env python
"""Plays an A4 for 1 second."""

import sounddevice as sd

a4 = Note(440, 1)
wave = Wave("sine", 48000, a4)

sd.play(wave.output, wave.sample_rate, blocking=True)