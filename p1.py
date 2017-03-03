x = 3
y = 5
count = 1
total_three = 0
total_five = 0

while x < 1000:
	print "this is x: %r" %x
	total_three += 3*count
	print total_three
	count = count + 1
	x += 3
#print total_three

count = 1
while y < 1000:
	if count % 3 == 0:
		print "multiple of 3"
	else:
		total_five += 5*count
		print total_five
	count = count + 1
	y += 5
		
print total_five

print "%r" %(total_five + total_three)