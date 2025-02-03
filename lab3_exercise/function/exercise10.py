def main(nums):
    list1 = []
    for num in nums:
        if num not in list1:
            list1.append(num)
    return list1

print(main([1, 2, 2, 3, 4, 4, 5]))
