# height = [20, 20,20,30]
#
# mw, l, r = 0, 0, len(height) - 1
#
# while l < r:
#     hl = height[l]
#     hr = height[r]
#     w = r - l
#     mw = max(mw, min(hl, hr) * w)
#
#     if hl < hr:
#         l += 1
#     elif hl > hr:
#         r -= 1
#     else:
#         r -= 1
#         l += 1
# print(mw)


h = {1: 5, 2: 8, 3: 11}

a=list(h.values())
b=h.update()
print(h,a)