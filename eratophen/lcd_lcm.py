'''
The largest common divisor
The least common multiple
'''
def simple_multip(num, simple_nums=[]):
    '''
    num - input number
    simple_nums - array which contains simple numbers for given one
    Parse number into simple multipliers and return all of them in 
    a list
    '''
    result = []
    
    div = num
    i = 0

    while div != 1:
        # check for simple multiplier
        if div % simple_nums[i] == 0:

            result.append(simple_nums[i])
            div = div / simple_nums[i]
        else:
            # take the next simple number in case of divide failure
            i = i + 1
    
    result.append(1)

    return result

def least_common_multiple(number1, simp_nums1, number2, simp_nums2):
    """
    find the least common multiple for two numbers with given 
    lists of simple numbers in given numbers
    """
    # find simple multipliers
    multip_for_first = simple_multip(number1, simp_nums1)
    multip_for_second = simple_multip(number2, simp_nums2)
    
    # take list for first num as start point
    result_list = list(multip_for_first)

    # check if number from the second list is in result_list
    for i in multip_for_second:
        
        temp = []
        last = 1
        for j in result_list:
            
            if j != i and i != last:
                temp.append(i)
                last = i
        
        # add missing numbers into list
        result_list.extend(temp)

    # form a variable for result of multiplying    
    result = 1

    for i in result_list:
        result = result * i
    
    return result

