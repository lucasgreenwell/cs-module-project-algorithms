'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    for num in  arr:
        if arr.count(num) < 2:
            return num
    # for num in arr:
    #     count = 0
    #     for num_again in arr:
    #         if num_again == num:
    #             count += 1
    #     if count < 2:
    #         return num




if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")