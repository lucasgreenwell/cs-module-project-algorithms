'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    #count all the zeroes
    num_of_zeroes = arr.count(0)
    #remove all the zeroes
    arr_without_any_zeroes = [num for num in arr if num != 0]
    #add all the zeros to the end
    for num in range(num_of_zeroes):
        arr_without_any_zeroes.append(0)
    return arr_without_any_zeroes


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")