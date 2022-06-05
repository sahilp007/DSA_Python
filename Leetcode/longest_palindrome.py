s = "aaaa"


def countSubstrings(s) -> int:
    def expand(left, right):

        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        s1 = s[:left] + s[right:]
        return len(s1)

    palindromes = 0
    for i in range(len(s)):
        # palindromes = max(expand(i, i + 1), palindromes)
        palindromes = max(expand(i, i), palindromes)
    return palindromes


print(countSubstrings(s))
