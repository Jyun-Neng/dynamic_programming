def knapsack(capacity, value, weight):
    """
    Give weights and values of n items, put these items in a knapsack of 
    finite capacity W to get the maximum total value in the knapsack.
    """
    # space complexity is O(W)
    K = [[0 for x in range(capacity+1)] for x in range(2)]
    s = [0] * 2
    # build table
    # time complexity is O(nW)
    for i in range(len(value)+1):
        for c in range(capacity+1):
            if i==0 or c==0:
                K[i%2][c] = 0
            elif weight[i-1] <= c:
                if value[i-1] + K[(i-1)%2][c-weight[i-1]] >  K[(i-1)%2][c]:
                    K[i%2][c] = value[i-1] + K[(i-1)%2][c-weight[i-1]]
                    s[c%2] = i
                else:    
                    K[i%2][c] = K[(i-1)%2][c]
                    s[c%2] = s[(c-1)%2]
            else:
                K[i%2][c] = K[(i-1)%2][c]

    return K[len(value)%2][capacity], s[capacity%2]


if __name__ == '__main__':
    weight = [10, 60, 20]
    value = [80, 100, 20]
    capacity = 50

    max_value, select = knapsack(capacity, value, weight)
    print('max value = ', max_value)
    print('select item = ', select)
