def mul():
    nums = [2, 7, 11, 15, 5, 1, 51, 3]
    target = 10
    result = []
    if target % 2 == 0:
        a = target / 2
        for i in range(len(nums)):
            if nums[i] == a:
                nums[i] += 0.1
        # print(nums)
    for num in nums:
        if target - num in nums:
            result.append(nums.index(num))
            # return nums.index(num)
    # print(nums)
mul()