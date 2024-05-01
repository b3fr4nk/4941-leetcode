# https://leetcode.com/problems/plus-one/

def plus_one(digits):
    i = -1
    while digits[i] == 9:
        digits[i] = 0
        i -= 1
        if i < len(digits) * -1:
            i = 0
            digits.append(0)
            break
    digits[i] += 1

    return digits
