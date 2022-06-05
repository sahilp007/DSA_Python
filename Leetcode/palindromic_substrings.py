# TIME LIMIT EXCEEDED

# indexes = []
#
#
# def ans(s, start, end):
#     if start >= end:
#         return
#     if s[start:end] == s[start:end][::-1]:
#         indexes.append([start, end])
#
#     ans(s, start + 1, end)
#     ans(s, start, end - 1)
#
#
# # indexes = list(set(tuple(sorted(index) for index in indexes)))
# ans(s, 0, len(s))
# res = list(set(tuple(sorted(sub)) for sub in indexes))
# ans = len(res)
# print(ans)

s = "aaaa"


def countSubstrings(s) -> int:
    def expand(left, right):

        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count

    palindromes = 0
    for i in range(len(s)):
        palindromes += expand(i, i)
        palindromes += expand(i, i + 1)
    return palindromes


print(countSubstrings(s))
