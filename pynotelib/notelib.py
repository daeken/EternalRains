from util import *
import spectrum

def listen(fn, notes):
	hnotes = []
	for note in notes:
		fundamental = note_to_freq(note)
		hnotes += map(freq_to_note, harmonics(fundamental, 20))

	hnotes = sort_notes(hnotes)[:20]
	anotes = spectrum.analyze(fn).keys()[:20]
	print hnotes
	print anotes
