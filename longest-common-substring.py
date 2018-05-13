# Give two strings. Find the longest common substring
def lcs(str1, str2):
    """
    Find the longest common substring in str1 and str2. 
    Time complexity is O(mn), where m and n are string length of str1 and str2, respectively. 
    And it need to create a 2-D array 'cnt'.
    The auxiliary space is big-theta(mn).
    """
    str1_len = len(str1)
    str2_len = len(str2)
    # space complexity is big-theta(mn)
    cnt = [[0 for x in range(str1_len + 1)] for y in range(str2_len + 1)]

    # calculate the length of LCS
    # time complexity is O(mn)
    for y in range(str2_len + 1):
        for x in range(str1_len + 1):
            if x == 0 or y == 0:
                cnt[y][x] = 0
            elif str1[x - 1] == str2[y - 1]:
                cnt[y][x] = cnt[y - 1][x - 1] + 1
            else:
                cnt[y][x] = max(cnt[y - 1][x], cnt[y][x - 1]) # record the optimize solution

    x, y = str1_len, str2_len
    lcs_num = cnt[y][x]
    lcs = [''] * lcs_num

    # print the LCS
    # time complexity is O(m+n)
    while x > 0 and y > 0:
        if str1[x - 1] == str2[y - 1]:
            lcs[lcs_num - 1] = str1[x - 1]
            lcs_num -= 1
            x -= 1
            y -= 1
        elif cnt[y - 1][x] >= cnt[y][x - 1]: # optimize solution
            y -= 1
        else:
            x -= 1

    return lcs


if __name__ == '__main__':
    str1 = 'geeksf21wfaisj'
    str2 = 'geeksabcgeeksadgwirwe'
    lcsstr = lcs(str1, str2)
    print(''.join(lcsstr))
