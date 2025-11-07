def filter_and_concat(nums: list[int], min_val: int) -> str:
    new_list=[]
    for num in nums:
        if num > min_val:
            new_list.append(str(num))
            
    return ",".join(new_list)


print(filter_and_concat([2, 5, 7, 1, 9], 4))

