'''
Input: an integer
Returns: an integer
'''
import itertools
def eating_cookies(n):
    # Your code here
    #create a list containing 1,2,3 the number of times that n is divisible by and also create a counter variable
    # create all permutations of that list and if the permutation adds up to n, then increment the counter
    #return the counter
    # possible_addends = []
    # for i in range(0, n):
    #     possible_addends.append(1)
    # for i in range(n // 2):
    #     possible_addends.append(2)
    # for i in range(n // 3):
    #     possible_addends.append(3)
    # result = [seq for i in range(len(possible_addends), 0, -1) for seq in itertools.combinations(possible_addends, i) if sum(seq) == n]
    # return len(result)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
