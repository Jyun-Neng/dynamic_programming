def knapsack(capacity, value, weight):
    """
    Give weights and values of n items, put these items in a knapsack of 
    finite capacity W to get the maximum total value in the knapsack.
    """
    # space complexity is big-theta(nW)
    K = [[0 for x in range(capacity+1)] for x in range(len(value)+1)]
    s = [0] * (capacity+1)
    # build table
    # time complexity is O(nW)
    for i in range(len(value)+1):
        for c in range(capacity+1):
            if i==0 or c==0:
                K[i][c] = 0
            elif weight[i-1] <= c:
                if value[i-1] + K[i-1][c-weight[i-1]] >  K[i-1][c]:
                    K[i][c] = value[i-1] + K[i-1][c-weight[i-1]]
                    s[c] = i
                else:    
                    K[i][c] = K[i-1][c]
                    s[c] = s[c-1]
            else:
                K[i][c] = K[i-1][c]

    return K[len(value)][capacity], s[capacity]


if __name__ == '__main__':
    weight = [10, 20, 30]
    value = [80, 100, 20]
    capacity = 50

    max_value, select = knapsack(capacity, value, weight)
    print('max value = ', max_value)
    print('select item = ', select)
