def strStr(haystack, needle):
    # iterate over haystack starting at 0 ending at length haystack - len of needle
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    # check if chunk is == to needle
    # if it is return i

    # return -1
    return -1
