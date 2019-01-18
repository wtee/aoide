import numpy as np

class Note:
    def __init__(self, pitch, duration):
        self.pitch = pitch
        self.duration = duration


class Wave:
    def __init__(self, form, sample_rate, note):
        """Accepts:
            sine
            triangle
            sawtooth
            inverse_sawtooth
            square
        """
        self.sample_rate = sample_rate
        if form == "sine":
            self.output  = (np.sin(2 * np.pi * np.arange(self.sample_rate * note.duration) * note.pitch / self.sample_rate)).astype(np.float32)
        else:
            print("Only the sine waveform is supported currently.")

