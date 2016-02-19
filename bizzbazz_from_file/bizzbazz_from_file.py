#!/usr/bin/python

import sys
import string

# Functions >>

def is_divided_by_3(n_str) : # Note, that this function gets a string as an argument (to work with big numbers)

        if (n_str[0] == '+' or n_str[0] == '-') :
                n_str = n_str[1:]

        if (len(n_str) == 1) : # End of recursion
                if ((n_str == '0') or (n_str == '3') or (n_str == '6') or (n_str == '9')) :
                        return True
                else :
                        return False

        sum = 0
        for char in n_str :
                sum += int(char)

        return is_divided_by_3(str(sum))

def is_divided_by_5(n_str) : # Note, that this function gets a string as an argument (to work with big numbers)

        if (n_str[-1] == '0' or n_str[-1] == '5') :
                return True
        else :
                return False

# Converts a number according to 'bizzbazz' task rules
def bizzbazz(n_str) : # Note, that this function gets a string as an argument (to work with big numbers)

        if (is_divided_by_3(n_str) and is_divided_by_5(n_str)) :
                return 'bizzbazz'

        elif (is_divided_by_3(n_str)) :
                return 'bizz'

        elif (is_divided_by_5(n_str)) :
                return 'bazz'

        else :
                return n_str

# Main >>

def main():

        if (len(sys.argv) != 2) :
                print  "Wrong number of arguments!"
                sys.exit(1)

        with open(sys.argv[1], 'r') as file:
                string = file.readline()

        string = string[:-1] # Removing the last '\n' character
        string_len = len(string)

        answer = '' # Here we'll keep the output string, which is answer to the task
        number = '' # Temp value for collecting a single number in the string

        for i in xrange(string_len) :

                if (i < (string_len - 1)) : # Not the last character of the string

                        if (string[i].isdigit()) :
                                number += string[i]

                        elif ((string[i] == '+' or string[i] == '-') and string[i + 1].isdigit()) : # Numbers can start with single '+' or single '-'

                                if (number != ''): # A number can be followed by a number. Example: '+42-42'
                                        answer += bizzbazz(number) # Adding current number

                                        number = ''
                                        number += string[i] # Starting filling next number
                                else :
                                        number += string[i]

                        else : # If we're here, we know that current char is not a part of a number

                                if (number != '') :
                                        answer += bizzbazz(number) + string[i]
                                else :
                                        answer += string[i]

                                number = ''

                else : # If it is last character of the string
                        if (string[i].isdigit()) :
                                number += string[i]
                                answer += bizzbazz(number)
                                number = ''
                        else :
                                if (number != '') :
                                    answer += bizzbazz(number)
                                else :
                                    answer += string[i]
        print answer

        sys.exit(0)

if __name__ == "__main__":
    main()
