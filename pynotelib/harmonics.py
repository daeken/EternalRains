from util import *

notes = ('E2', )#('D3', 'A3', 'D4', 'F#4')
hnotes = []
for note in notes:
	fundamental = note_to_freq(note)
	hnotes += map(freq_to_note, harmonics(fundamental, 20))

print sort_notes(hnotes)[:20]
