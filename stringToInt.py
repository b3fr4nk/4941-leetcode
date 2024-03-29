def myAtoi(s):
    num = 0
    negative = False
    num_stack = []  # treat this as a stack by appending and traversing in reverse order

    s = s.strip()

    if len(s) == 0:
        return 0

    if s[0] == "-":
        s = s[1:]
        negative = True
    elif s[0] == "+":
        s = s[1:]

    for i in range(len(s)):
        if not s[i].isnumeric():
            break
        else:
            num_stack.append(s[i])
    for i in range(1, len(num_stack) + 1):
        num += int(num_stack[-i])*(10**(i-1))

        if num > 2**31 and negative:
            num = 2**31
            break
        elif num > 2**31 - 1 and not negative:
            num = 2**31 - 1
            break

    if negative:
        num = num - (num*2)

    return num


print(myAtoi('-4241    jfkasdl'))
