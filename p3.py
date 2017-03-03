#finding factors
number = 600851475143
max_divisor = 600851475143
divisor = 1
factors = []

while divisor < max_divisor:
    remainder = number % divisor
    if remainder == 0:
        max_divisor = number/divisor
        factors.append(max_divisor)    
        factors.append(divisor)
        print  "%s and %s are factors" % (divisor , max_divisor)
        
        
    divisor += 1
    
factors.sort()
print "All Done!"    
print factors

#testing for primes
test_number  = factors[-2]
divisor = 1
position = -2

while divisor < test_number:

    remainder = test_number % divisor
    
    if divisor > 1 and remainder == 0:
        print "%s is NOT a prime" % test_number
        divisor = 1
        position = position - 1
        test_number = factors[position]
        
    
    divisor += 1

print "%s is the largest prime!" % test_number    
exit()