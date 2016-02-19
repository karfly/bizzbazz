**The 'bizzbazz' task by Karim Iskakov**
====================================


----------


Formulation of the task:
----------------
>Input is a string. The output is a string where numbers are replaced with:

> - '*bizz*' if it is divided by 3
> - '*bazz*' if it is divided by 3
> - '*bizzbazz*' if it is divided by 3 and 5

> If the number does not fit this list, it is left untouched. Numbers can be signed ('**+**' or '**-**'). It's restricted to use explicit division (e.g. '**/**' or '**%**' ).

How to use:
----------------
**'From string' version (bizzbazz_from_string.py):**

>`$ ./bizzbazz_from_string.py [YOUR_STRING]`
>
>*Example:*
>
>`$ ./bizzbazz_from_string.py bizzbazz=15`
>`$ bizzbazz=bizzbazz`

**'From file' version (bizzbazz_from_file.py). First line must have a line folding ('\n'):**

>`$ ./bizzbazz_from_file.py [PATH_TO_THE_FILE]`

>*Example:*
>
>`$ ./bizzbazz_from_file.py myfile.txt`
>`$ Bee says "bizz bazz"`

*myfile.txt:*

>> Bee says "33 55"


Features
-------------

 - **Works with big strings and numbers**

 `$ ./bizzbazz_from_string.py big_string.txt`
 `$ It's gonna be legen... (wait for it) bizzbazz ...dary!`

*big_string.txt:*
> It's gonna be legen... (wait for it) 30000000000000000000
> 000000000000000000000000000000000000000000000000
> 000000000000000000000000000000000000000000000000
> 000000000000000000000000000000000000000000000000
> 000000000000000000000000000000000000000000000000
> 000000000000000000000000000000000000000000000000
> 00000000000000000000000000 ...dary

 - Awesome detection of signed numbers sequences:
 `$./bizzbazz_from_string.py +42-42++55--30+`
 `bizzbizz+bazz-bizzbazz+`
