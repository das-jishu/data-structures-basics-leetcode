def subset(nums):
    if len(nums) == 0:
        return []
    
    if len(nums) == 1:
        return [[], nums]
    
    res = []
    #or i, x in enumerate(nums):
    x = nums[0]
    t = subset(nums[1:])
    print("t:",t)
    res.extend(t)
    print("res:",res)
    for y in t:
        temp = [x]
        """ for k in y:
            temp.append(k) """
        temp.extend(y)
        res.append(temp)
    print("res at end:", res)       
    return res

if __name__ == "__main__":
    print(subset([1, 2, 4]))