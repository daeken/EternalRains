from util import *
import spectrum

def listen(fn, notes):
	anotes = spectrum.analyze(fn).items()
	top = max(mag for note, mag in anotes)
	anotes = dict((note, mag / top) for note, mag in anotes if mag / top > 0.5)
	confidence = 0.0
	part = 1. / len(notes)
	for note in notes:
		if note not in anotes:
			hnotes = harmonics(note, 5)[1:]
			for i, hnote in enumerate(hnotes):
				if hnote in anotes:
					confidence += part * ((len(hnotes) - i) / len(hnotes)) / 2
					break
		else:
			confidence += part
	return confidence
