def is_james_bond(nums):
    match_index = 0

    for num in nums:
        if num == 0 and match_index == 0:
            match_index += 1
        elif num == 0 and match_index == 1:
            match_index += 1
        elif num == 7 and match_index == 2:
            return True

    return False


print(is_james_bond([1, 2, 4, 0, 0, 7, 5]))  # True
print(is_james_bond([1, 7, 2, 0, 4, 5, 0]))  # False
print(is_james_bond([1, 0, 2, 0, 4, 7, 5]))  # True
