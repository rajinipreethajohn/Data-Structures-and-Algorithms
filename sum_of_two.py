list = [2,5,8,10,24]

def sum_of_two_elements(list):
    """Returns the sum of subsequent two elements in a list of numbers"""
    new_list = []
    print(new_list)
    for i in range(len(list)-1):
        two_sum = (list[i] + list[i+1])
        print(two_sum)
        new_list.append(two_sum)
    return(new_list)

print(sum_of_two_elements(list))