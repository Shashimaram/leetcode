nums = [0,0,1,1,1,2,2,3,3,4]


for x in range(len(nums)):
    current_number = nums[x]
    next_number = nums[x+1]
    if current_number == next_number:
        del nums[nums[x+1]]
        print(nums)
    else:
        continue

print(nums)