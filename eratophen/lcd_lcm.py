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

    print(result_list)
    return mult_list(result_list)


def larg_com_div(number1, simp_nums1, number2, simp_nums2):
    """
    find the largest common divisor for two numbers with given 
    lists of simple numbers in given numbers
    """
    # find simple multipliers
    multip_for_first = simple_multip(number1, simp_nums1)
    multip_for_second = simple_multip(number2, simp_nums2)

    result = []
    
    if len(multip_for_first) <= len(multip_for_second):
        result.extend(find_unic_intersec(multip_for_first, multip_for_second))
    else:
        result.extend(find_unic_intersec(multip_for_second, multip_for_first))

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
    
    result.append(1)

    return result


def find_unic_intersec(lesser_list = [], larger_list = []):

    temp_list = []

    for i in range(len(lesser_list)):

        j = i
        while j < len(larger_list):

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
