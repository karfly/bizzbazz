#!/usr/bin/python

import sys
import string

from bizzbazz_functions import is_divided_by_3, is_divided_by_5, bizzbazz

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
