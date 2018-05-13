# Give two strings. Find the longest common substring
def lcsLength(str1, str2):
    """
    Build the direct table,
    and count the characters. 
    There are two situations:
    1. if str1[x] == str2[y], then compare last characters str1[x-1] and str2[y-1]. 
    2. if str1[x] != str2[y], then compare str1[x-1] and str2[y] or str1[x] and str2[y-1].
    """
    str1_len = len(str1)
    str2_len = len(str2)
    cnt = [[0 for x in range(str1_len + 1)] for y in range(str2_len + 1)]
    direct = [['none' for x in range(str1_len + 1)]
              for y in range(str2_len + 1)]

    for x in range(1, str1_len + 1):
        for y in range(1, str2_len + 1):
            if str1[x - 1] == str2[y - 1]:
                cnt[y][x] = cnt[y - 1][x - 1] + 1
                direct[y][x] = 'upper-left'
            # direct to the largest cnt value
            elif cnt[y - 1][x] >= cnt[y][x - 1]:
                cnt[y][x] = cnt[y - 1][x]
                direct[y][x] = 'up'
            else:
                cnt[y][x] = cnt[y][x - 1]
                direct[y][x] = 'left'

    return cnt, direct


def printLCS(direct, str1, x, y):
    """
    Through the direct table, show the LCS. 
    """
    if x == 0 or y == 0:
        return
    elif direct[y][x] == 'upper-left':  # characters match
        printLCS(direct, str1, x - 1, y - 1)
        print(str1[x - 1], end='')
    elif direct[y][x] == 'up':
        printLCS(direct, str1, x, y - 1)
    else:
        printLCS(direct, str1, x - 1, y)


if __name__ == '__main__':
    str1 = 'geeksforgeek'
    str2 = 'geeksabcgeek'
    cnt, direct = lcsLength(str1, str2)
    printLCS(direct, str1, len(str1), len(str2))
