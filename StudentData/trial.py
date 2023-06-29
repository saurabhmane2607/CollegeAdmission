s=["the","quick","brown","fox","quick"]
word1 ="the"
word2 ="csd"

def dist():
    ind=-1
    num=-1
    min_ind=len(s)+1
    for i in range(len(s)):
        if s[i] == word1:
            ind=i
        elif s[i]==word2:
            num=i
        if ind != -1 and num != -1:
            min_ind= num-ind
    return min_ind

result=dist()
print(result)