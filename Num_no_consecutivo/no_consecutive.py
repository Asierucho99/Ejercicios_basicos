def no_consecutive():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for x in range(len(nums) - 1):
        if nums[x + 1] != nums[x] + 1: 
            print("No consecutive")
            return
    return print(None)
            
no_consecutive()
