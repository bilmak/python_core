def get_pairs(nums: list) -> list[tuple]:
    result = []
    if len(nums) <= 1:
        return result

    for i in range(0, len(nums)-1):
        result.extend([(nums[i], nums[i+1])])

    return result


a = get_pairs([6, 3, 8, 1, 4])
print(a)
