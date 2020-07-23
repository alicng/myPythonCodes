def t_sum(times):
	tlist = [ x.split(":") for x in times ]
	seconds = sum([ int(x[2]) for x in tlist ])
	minutes = sum([ int(x[1]) for x in tlist ]) + int(seconds/60)
	hours = sum([ int(x[0]) for x in tlist ]) + int(minutes/60)
	return [ hours , minutes % 60 , seconds % 60]
