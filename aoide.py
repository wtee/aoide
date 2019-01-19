import numpy as np
import simpleaudio as sa

class Note:
    def __init__(self, pitch, duration):
        self.pitch = pitch
        self.duration = duration


class SixteenthNote(Note):
    def __init__(self, pitch):
        self.pitch = pitch
        self.duration = 0.0625


class EighthNote(Note):
    def __init__(self, pitch):
        self.pitch = pitch
        self.duration = 0.125


class QuarterNote(Note):
    def __init__(self, pitch):
        self.pitch = pitch
        self.duration = 0.25


class HalfNote(Note):
    def __init__(self, pitch):
        self.pitch = pitch
        self.duration = 0.5


class WholeNote(Note):
    def __init__(self, pitch):
        self.pitch = pitch
        self.duration = 1


class Wave:
    def __init__(self, sample_rate, tempo, note):
        """Accepts:
            sine
            triangle
            sawtooth
            inverse_sawtooth
            square
        """
        self.sample_rate = sample_rate
        # Beats per minute
        self.tempo = tempo
        self.duration = 100 / 60 * note.duration
        self.pitch = note.pitch

    def sine(self):
        output = (
            np.sin(
                2
                * np.pi
                * np.arange(self.sample_rate * self.duration)
                * self.pitch
                / self.sample_rate
            )
        ).astype(np.float32)

        return output


class Rest:
    def __init__(self, duration):
        self.pitch = 0
        self.duration = duration


class Chord:
    def __init__(self, duration, *notes):
        self.notes = sorted(notes)
        # Duration allows for simply playing the whole chord
        # for a span of time. Chords can also be used to 
        # generate appregios and what not by treating them
        # as a convenient collection of notes with or without
        # regard to the duration propetry.
        self.duration = duration
        self.notes = list(notes)


def play_list(sample_rate, waves):
    output = np.hstack(waves)
    output *= 32767 / np.max(np.abs(output))
    output = output.astype(np.int16)
    play_obj = sa.play_buffer(output, 1, 2, sample_rate)
    play_obj.wait_done()

