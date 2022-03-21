# Given an array A and an integer B, find the number of occurrences of B in A.

# I/P : A = [1, 2, 2], B = 2 
# O/P : 2


class Solution:
    def solve(self, A, B):
        x = 0  #Initialize counter
        if B in A: #Checking if the number exists in the list
            for i in range(len(A)): #If the number is found, run a loop to count the occurance
                if A[i] == B: #Check for each occurance
                    x = x+1  #Count the number of occurance
            return x #Return the counter
        else:
            return 0  #If the number is not found, return 0
