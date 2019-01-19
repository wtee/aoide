import numpy as np
import simpleaudio as sa

from aoide import EighthNote, QuarterNote, Wave, play_list

d5 = 587.3295
a4 = 440.0000
g4 = 391.9954
e4 = 329.6276
d4 = 293.6648

notes = [EighthNote(d4), EighthNote(e4), QuarterNote(g4), EighthNote(d4), EighthNote(e4), EighthNote(d4), QuarterNote(g4), QuarterNote(a4), EighthNote(a4), EighthNote(g4), QuarterNote(e4), EighthNote(d4), EighthNote(d4), EighthNote(g4), EighthNote(g4)]
tempo = 60
sample_rate = 48000

wave_forms = [wave.sine() for wave in [Wave(sample_rate, tempo, note) for note in notes]]

play_list(sample_rate, wave_forms)


