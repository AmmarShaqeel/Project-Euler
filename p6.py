total_square = 0
total_sum = 0
for square in range(1, 101):
	total_square += square*square

for sum in range(1, 101):
	total_sum += sum
	
diffrence = total_sum*total_sum - total_square

print diffrence