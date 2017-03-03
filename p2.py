term1 = 1
term2 = 0
sequence = 0
total = 0
while term2+term1 < 4000000:
	sequence = term1 + term2
	#print sequence
	term2 = term1 
	#print "term2: %r" %term2
	term1 = sequence
	#print "term1: %r" %term1
	
	if sequence % 2 == 0:
		total += sequence
		
print "Total even numbers:%r" %total
	
	