# assignment-04.py
# Teo Espero
# 20200511
# This program was created to illustrate the use of functions and
# how they can be called recursively within themselves:
# This program takes a whole number as parameter and returns a string containing the number spelled out in English.

########################################################################################################################
def get_sign(n):
    # this function does nothing more byt determine the sign of the number being converted
    if n < 0:
        what_is_the_sign = 'negative '
    else:
        what_is_the_sign = ''
    return what_is_the_sign

########################################################################################################################
def spellNumberLessThan10 (n):
    # "spellNumberLessThan10 ( n )" that takes a number n as parameter (with 0<=n<10) and returns
    # a string containing the word for that number.

    sign = get_sign(n)
    n = abs(n)
    digit=['zero', 'one ', 'two ', 'three ', 'four ', 'five ', 'six ', 'seven ', 'eight ', 'nine ']
    return sign + digit[n]

########################################################################################################################
def spellThreeDigitNumber(n):
    # "spellThreeDigitNumber( n )" that takes a number n as parameter (with 0<=n<1000) and returns a string
    # containing the words for that number.

    sign = get_sign(n)
    n = abs(n)
    if n < 1000:
        if n < 100:
            if n < 10:
                place = spellNumberLessThan10(n)
            elif n >= 10 and n < 20:
                position = n % 10
                # print(position)
                place_value = ['ten ', 'eleven ', 'twelve ', 'thirteen ', 'fourteen ', 'fifteen ', 'sixteen ', 'seventeen ', 'eighteen ', 'nineteen ']
                place = place_value[position]
            elif n > 19:
                position = n // 10
                # print(position)
                position = position - 1
                place_value = ['', 'twenty ', 'thirty ', 'forty ', 'fifty ', 'sixty ', 'seventy ', 'eighty ', 'ninety ']
                place = place_value[position]
                n = n - ((n // 10 * 10))
                if n > 0:
                    place = place + spellNumberLessThan10(n)
        else:
            # print(n)
            position = n // 100
            # print(position)
            place = spellNumberLessThan10(position) + 'hundred '
            n = n - ((n // 100 * 100))
            # print(n)
            if n > 0:
                place = place + spellThreeDigitNumber(n)
    else:
        position = n // 1000
        # print(position)
        place = spellNumberLessThan10(position) + 'thousand '
        n = n - ((n // 1000 * 1000))
        # print(n)
        if n > 0:
            place = place + spellThreeDigitNumber(n)
    return sign + place

########################################################################################################################
def spell(n):
    # "spell( n )" that takes a number n as parameter (with 0 <= n <=999,999,999) and returns a
    # string containing the words for that number.

    sign = get_sign(n)
    n = abs(n)
    if n < 1000000000: #999,999,999
        if n < 100000000: #99,999,999
            if n < 10000000: #9,999,999
                if n < 1000000:  # 999,999
                    if n < 100000:  # 99,999
                        if n < 10000:  # 9,999
                            place = spellThreeDigitNumber(n)
                            return sign + place
                        else:
                            position = n // 1000
                            place = spellThreeDigitNumber(position) + 'thousand '
                            n = n - ((n // 1000*  1000))
                            if n > 0:
                                place = place + spell(n)
                    else:
                        position = n // 100000
                        place = spellNumberLessThan10(position) + 'hundred '
                        n = n - ((n // 100000 * 100000))
                        if n > 0:
                            place = place + spell(n)
                else:
                    position = n // 1000000
                    place = spellNumberLessThan10(position) + 'million '
                    n = n - ((n // 1000000 * 1000000))
                    if n > 0:
                        place = place + spell(n)
            else:
                position = n // 1000000
                place = spellThreeDigitNumber(position) + 'million '
                n = n - ((n // 1000000 * 1000000))
                if n > 0:
                    place = place + spell(n)
        else:
            position = n // 100000000
            place = spellNumberLessThan10(position) + 'hundred '
            n = n - ((n // 100000000 * 100000000))
            if n > 0:
                place = place + spell(n)
    else:
        place = 'Value too large'
    return sign + place

########################################################################################################################
# MAIN PROGRAM

######## TESTs function spell()  ###########
print (spell (123456789).title() )
print (spell (456678).title() )
print (spell (66).title() )
print (spell (-123456789).title() )
print (spell (-456678).title() )
print (spell (-418).title() )
print (spell (-13456678).title() )
print (spell (0).title() )
print (spell (10004).title() )

####### OUTPUT #######
'''
One Hundred Twenty Three Million Four Hundred Fifty Six Thousand Seven Hundred Eighty Nine 
Four Hundred Fifty Six Thousand Six Hundred Seventy Eight 
Sixty Six 
Negative One Hundred Twenty Three Million Four Hundred Fifty Six Thousand Seven Hundred Eighty Nine 
Negative Four Hundred Fifty Six Thousand Six Hundred Seventy Eight 
Negative Four Hundred Eighteen 
Negative Thirteen Million Four Hundred Fifty Six Thousand Six Hundred Seventy Eight 
Zero
Ten Thousand Four 
'''