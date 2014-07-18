import notelib

tests = (
	('low_e_open', ('E2', )), 
	('a_open', ('A2', )), 
	('d_open', ('D3', )), 
	('g_open', ('G3', )), 
	('b_open', ('B3', )), 
	('high_e_open', ('E4', )), 
	('c_chord', ('E2', 'C2', 'E3', 'G3', 'C3', 'E4')), 
	('e_chord', ('E2', 'B2', 'E3', 'G#3', 'B3', 'E4')), 
	('d_chord', ('D3', 'A3', 'D4', 'F#4')), 
)

"""
for fn, _ in tests:
	for _, notes in tests:
		print fn, notes, '%i%%' % (notelib.listen('samples/%s.wav' % fn, notes) * 100)
"""

print '<table border="1">'
print '<tr>'
print '<td>&nbsp;</td>'
for tfn, _ in tests:
	print '<th>%s</th>' % tfn
print '</tr>'
for fn, _ in tests:
	print '<tr>'
	print '<th>%s</th>' % fn
	for _, notes in tests:
		print '<td>%i%%</td>' % (notelib.listen('samples/%s.wav' % fn, notes) * 100)
	print '</tr>'
print '</table>'
