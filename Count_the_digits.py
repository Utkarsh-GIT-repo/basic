#pseudocode for counting the digits in a number for custom number of inputs.
def main():
    #Accept Custom inputs
    number_of_input = int(input())
    #Run a loop for custom number numer of input and collect inputs from user
    for i in range(number_of_input):
        input_num = input()  #Accept input in a loop
        len_input_num = len(input_num)  #Calculate length 
        print(len_input_num)

    return 0

if __name__ == '__main__':
    main()
