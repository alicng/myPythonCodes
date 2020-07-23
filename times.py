def t_sum(times):
	tlist = [ x.split(":") for x in times ]
	s = sum([ int(x[2]) for x in tlist ])
	m = sum([ int(x[1]) for x in tlist ]) + int(seconds/60)
	h = sum([ int(x[0]) for x in tlist ]) + int(minutes/60)
	return [ h , m % 60 , s % 60]
