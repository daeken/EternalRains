import math

chromatic = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')

def note_to_freq(note):
	if note[1] in '#b':
		note, octave = chromatic.index(note[:2]), int(note[2:]) - 1
	else:
		note, octave = chromatic.index(note[0]), int(note[1:]) - 1
	steps = (octave * 12 + note) - 45
	
	return 440. * (2 ** (1. / 12)) ** steps

def freq_to_note(freq):
	note = int(round(12 * math.log(freq / 440., 2) + 69))
	return chromatic[note % 12] + str((note / 12) - 1)

def harmonics(fundamental, count):
	return [fundamental * (i + 1) for i in xrange(count)]

def sort_notes(notes):
	return map(freq_to_note, sorted(map(note_to_freq, list(set(notes)))))
