def lengthOfLastWord(s):
    s = s.rstrip()

    end = len(s) - 1

    while s[end] != ' ':
        if end == 0:
            return len(s)
        end -= 1

    return len(s) - 1 - end


print(lengthOfLastWord('  hello world  '))


# https://leetcode.com/problems/length-of-last-word/description/?submissionId=1219672780
