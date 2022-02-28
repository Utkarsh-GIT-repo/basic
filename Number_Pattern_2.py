#Write a program to input an integer N from user and print the given number pattern.
#Input -> 4
#Output
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 

def main():
    pattern_input = int(input()) #Capture input for the number levels the pattern needs to be generated
    tri = 0 #Initialize the pattern number series
    for i in range(1,pattern_input+1): #Initial pattern loops 
        for j in range(i):
            tri = tri+1 #Incrementing the numbers in the pattern
            print(tri, end= " ") #horizontal  scaling and preventing the cursor from moving to next line
        print() #Move the pattern to next line
    return 0

if __name__ == '__main__':
    main()
