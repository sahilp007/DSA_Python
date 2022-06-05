ans1 = ""


def palindrome(s, pl):
    if s == s[::-1]:
        if pl < len(s):
            palin1 = s
            pl = len(s)
            print(palin1, pl)
            return palin1, len(s)
    else:
        print('1')
        palindrome(s[:-1], pl)
        print('2')
        palindrome(s[1:], pl)
        print('3')

        return "Nothing"
    print(s, len(s))
    # return palin


print(palindrome('baabc', 0))
