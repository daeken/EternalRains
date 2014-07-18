import math
import collections
from util import *
import numpy as np
import scipy.io.wavfile as wav

def find_peaks(bins, freqs):
	peaks = {}

	needle = 0
	downward = False
	prev = 0
	prev_peak = 0
	for i, bin in enumerate(bins):
		if bin > needle and downward:
			if prev != 0:
				peaks[prev] = prev_peak
			prev = prev_peak = 0
			downward = False
		elif bin > prev_peak and not downward:
			prev = freqs[i]
			prev_peak = bin
		elif bin < needle:
			downward = True
		needle = bin

	return peaks

def analyze(fn):
	samplerate, samples = wav.read(fn)
	samples = [sample[0] for sample in samples]

	bins = np.fft.rfft(samples) / samplerate / 2
	
	notebins = collections.defaultdict(int)
	freqs = rfftfreq(len(bins) * 2, 1./samplerate)
	amp = np.abs(bins)
	peaks = [(freq_to_note(freq), mag) for freq, mag in find_peaks(amp, freqs).items()]
	binned = [(note, 20 * math.log(mag, 10)) for note, mag in sorted(peaks, lambda x, y: cmp(y[1], x[1]))]
	
	return collections.OrderedDict((note, mag) for note, mag in binned if mag > 0)
