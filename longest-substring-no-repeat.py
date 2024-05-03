def lengthOfLongestSubstring(s):
    output = 0
    left = 0
    letters = {}

    for i in range(len(s)):
        if s[i] not in letters:
            output = max(output, i-left+1)

        else:
            if letters[s[i]] < left:
                output = max(output, i-left + 1)
            else:
                left = letters[s[i]] + 1
        letters[s[i]] = i

    return output
