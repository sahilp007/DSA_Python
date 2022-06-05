height = [3, 1, 2, 4, 0, 1, 3, 2]

left = []
right = []
water = 0
lc = -111111111111
rc = -111111111111

for i in range(len(height)):
    if height[i] > lc:
        lc = height[i]
    left.append(lc)
# print(left)

hr = list(reversed(height))
for i in range(len(hr)):
    if hr[i] > rc:
        rc = hr[i]
    right.append(rc)
right.reverse()
# print(right)

for i in range(len(height)):
    l = left[i]
    r = right[i]
    water += min(l, r) - height[i]

print(water)
