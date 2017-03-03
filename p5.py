number = 2520
number_found = 0

def divisibleby20(number_for_testing):
    is_num = 1
    #print "testing %s" % number_for_testing
    for i in range (1,21):
        remainder = number_for_testing % i
        #print remainder
        if remainder != 0:
            is_num = 0
            #print "is num is %s" % is_num
            
    return is_num
    

while number_found == 0:
    #print "is %s divisible by 20?" % number
    is_num = divisibleby20(number)
    
    if is_num == 1:
        number_found = 1
        print "number found!"
        print number
        exit()
        
    number = number + 1
    

    