# You are given two non-negative integers, A and B. Find the value of the Least Common Multiple (LCM) of A and B.

# LCM of two integers is the smallest positive integer divisible by both.

# Input Format
# The first argument is an integer A.
# The second argument is an integer B.

# Output Format
# Return an integer.

# Input 1:

#  A = 2
#  B = 3 
  
#   Output 1:

#  6 

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def LCM(self, A, B):
        #1 to min(A, B) and find the largest number G such that both A and B are divisible by it.
        #Then, LCM = (A * B) / G.
        li = []
        for i in range(1, min(A,B)+1): 
            i = int(i)
            if A % i == 0 and B % i == 0:
                li.append(i)
        g = (A * B)/max(li)
        g = int(g)
        return g

      
      
