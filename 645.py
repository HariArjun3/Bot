def findErrorNums(nums: list) -> list:
    n = len(nums)
    sum_nums = sum(set(nums))
    sum_nums_2 = sum(nums)
    return [sum(nums) - sum(set(nums)), n * (n + 1) // 2 - sum(set(nums))]



print(findErrorNums([1, 2, 2, 4]))  # [2, 2]
