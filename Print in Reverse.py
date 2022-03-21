# Write a program to print the input array A of size N in reverse order where you have to take integer N and further N elements as input from user.
# I/P : Format: A single line representing N followed by N integers of the array A
# O/P : A single line containing N space separated integers representing elements of the input array in reverse order.

def main():
    inp = list(map(int,input().split()))  #Reading space seperated user input and putting them in a list as integer
    N = inp[0] #First entry in the list represents number of element as an input
    for i in range(1, N+1): #Initialize a loop for number of elements
        print(inp[N-i+1],end=' ') #Printing the array value from last to first

    return 0

if __name__ == '__main__':
    main()
