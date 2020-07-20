'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # set up variables for the beginning and end of the window
    #set up a result array
    #loop through the array
        #if the window can't keep moving break the loop
        #slice the array
        #push the maximum element in the slice
        # iterate the window
    #return the result array
    beginning_of_the_window = 0
    end_of_the_window = k
    res = []
    for num in nums:
        if end_of_the_window > len(nums):
            break
        window = nums[beginning_of_the_window:end_of_the_window]
        window.sort()
        print(window)
        res.append(window[-1])
        beginning_of_the_window += 1
        end_of_the_window += 1
    return res




if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
