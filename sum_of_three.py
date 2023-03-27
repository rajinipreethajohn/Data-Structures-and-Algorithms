
list = [2,5,8,10,24]

def sum_of_three_elements(list):
    """Returns the sum of subsequent three elements in a list of numbers"""
    new_list = []
    print(new_list)
    for i in range(len(list)-2):
        three_sum = (list[i] + list[i+1] + list[i+2])
        print(three_sum)
        new_list.append(three_sum)
    return(new_list)

print(sum_of_three_elements(list))