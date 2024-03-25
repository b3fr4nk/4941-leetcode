def romanToInt(s):
    sum = 0
    translations = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    subtraction = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }

    i = 0

    while i < len(s):
        # check for subtraction cases
        if i < len(s) - 1:
            pair = s[i:i+2]
            if pair in subtraction:
                # skip the next numeral since it is part of the subtraction case
                i += 2
                sum += subtraction[pair]
                continue

        sum += translations[s[i]]
        i += 1

    return sum


print(romanToInt('XIV'))
