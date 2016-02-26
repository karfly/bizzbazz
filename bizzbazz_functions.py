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

        return (n_str[-1] == '0' or n_str[-1] == '5')

# Converts a number according to 'bizzbazz' task rules
def bizzbazz(n_str) : # Note, that this function gets a string as an argument (to work with big numbers)

        divided_by_3 = is_divided_by_3(n_str)
        divided_by_5 = is_divided_by_5(n_str)

        if (divided_by_3 and divided_by_5) :
                return 'bizzbazz'

        elif (divided_by_3) :
                return 'bizz'

        elif (divided_by_5) :
                return 'bazz'

        else :
                return n_str
