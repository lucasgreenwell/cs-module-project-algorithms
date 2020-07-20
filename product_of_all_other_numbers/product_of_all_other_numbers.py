'''
Input: a List of integers
Returns: a List of integers
'''
import math
def product_of_all_other_numbers(arr):
    #multiply the whole array toogether and call it product
    #set up result array
    #loop through the whole array
        #divide the product by the current index and push the result onto the result array
    product = 1
    for num in arr:
        product = product * num
    res = []
    for num in arr:
        res.append(product / num)

    return res


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
