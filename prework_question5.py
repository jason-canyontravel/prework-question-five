lst = [1, 2, 3, 4, 5, 5, 6]
any(lst[i]==lst[i+1] for i in range(len(lst)-1))
#outputs:
True