#pseducode for sum of individual digits of the input numbers
#The number of input numbers are custom 
def main():
    number_of_inputs = int(input()) #Number of input numbers in to be captured in new lines
    for i in range(number_of_inputs):
        capture_input = str(input()) #Capture the number of input numbers and convert them to string
        sum_of_digits = 0 #initialize the sum of digits of the input number as 0 per loop
        for s in capture_input: #Splitting the input number in seperate digits
            sum_of_digits = int(s)+sum_of_digits #Calculating the sum of digits in the loop
        print(sum_of_digits)
    return 0

if __name__ == '__main__':
    main()
