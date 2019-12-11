'''
The largest common divisor
The least common multiple
'''

def lea_com_mult(number1, simp_nums1, number2, simp_nums2):
    """
    find the least common multiple for two numbers with given 
    lists of simple numbers in given numbers
    """
    # find simple multipliers
    multip_for_first = simple_multip(number1, simp_nums1)
    multip_for_second = simple_multip(number2, simp_nums2)
    
    # take list for first num as start point
    result_list = list(multip_for_first)
    # intersection between two lists
    intersec = []

    # find the same numbers is both lists
    if len(multip_for_first) < len(multip_for_second): # may be a bug with <= and similar lists as for nums 169 and 143
        intersec.extend(find_unic_intersec(multip_for_first, multip_for_second))
    else:
        intersec.extend(find_unic_intersec(multip_for_second, multip_for_first))

    # delete all non-unique numbers from second list
    for i in intersec:
        for j in multip_for_second:
            if i == j:
                multip_for_second.remove(i)
                break
    
    result_list.extend(multip_for_second)

    return mult_list(result_list)


def larg_com_div(number1, simp_nums1, number2, simp_nums2):
    """
    find the largest common divisor for two numbers with given 
    lists of simple numbers in given numbers
    """
    # find simple multipliers
    multip_for_first = simple_multip(number1, simp_nums1)
    multip_for_second = simple_multip(number2, simp_nums2)
    
    print(multip_for_first)
    print(multip_for_second)

    result = []
    
    if len(multip_for_first) < len(multip_for_second): # may be a bug with <= and similar lists as for nums 169 and 143
        result.extend(find_unic_intersec(multip_for_first, multip_for_second))
    else:
        result.extend(find_unic_intersec(multip_for_second, multip_for_first))
    
    print(result)

    return mult_list(result)


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
    
    # append last number
    result.append(1)

    return result


def find_unic_intersec(lesser_list = [], larger_list = []):
    """
    Seek unik intersection in two lists os simple multipliers
    like 
    [2, 2, 2, 2, 1] and [2, 2, 5, 1] <- smaller one is main in comparison of this two
     |  |                |  |
    the result is [2, 2]
    """
    temp_list = []

    # easier to check smaller in larger than vice versa
    # if we have true comparison we don't check that number again
    for i in range(len(lesser_list)):
        
        # start next iteration from previous possition, don't have to check checked
        j = i
        while j < len(larger_list):

            # no reason to continue if we have true
            if lesser_list[i] == larger_list[j]:
                temp_list.append(larger_list[j])
                break

            j = j + 1

    return temp_list


def mult_list(list_in):

    result = 1
    for i in list_in:
        result = result * i

    return result
