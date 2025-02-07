def spy_game(nums):
    to_find = [0,0,7]
    new_list =[]
    for num in nums:
        if num == 7 or num == 0:
            new_list.append(num)
    
    if new_list == to_find:
        pass


spy_game([1,2,4,0,0,7,5])
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0])