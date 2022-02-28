#Check if the given input integer is Palindromic Integer.

def main():
    capture_input = str(input()) #Capture the input as string
    stri = ''
    for i in capture_input: #Reverse the input
        stri = i + stri
    if stri == capture_input: #Check if the input is eq to reversed input
        print('Yes')
    else:
        print('No')
    return 0

if __name__ == '__main__':
    main()
