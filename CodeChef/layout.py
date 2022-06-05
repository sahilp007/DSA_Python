

try:
    t = int(input())
    for j in range(t):
        p = list(map(int, input().rstrip().split()))

        n, k = p[0], p[1]


except:
    pass

'''
remove array duplicates
a = list(dit.fromkeysc(a))


remove duplicates in nested lists
res = list(set(tuple(sorted(sub)) for sub in test_list))


def countBits(self, num):
        
        setBits = [0] * (num+1)
        # (i & (i -1)) is actually Brian Kernighan’s Algorithm, so always keep it handy for counting ones
        for i in range(1 ,num+1):
            setBits[i] = setBits[i & (i-1)] + 1
        return setBits
'''