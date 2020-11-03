
def threeSum(nums):
    result = []
    if len(nums) < 3:
        return []
    for i, t in enumerate(nums):
        val = search(nums[:i] + nums[i+1:], -t)
        if len(val) != 0:
            val.append(t)
            result.append(val)
            
    return (result)

def search(arr, value):
    s = set()
    for x in arr:
        if (value - x) not in s:
            s.add(x)
        else:
            print("FOUND")
            return [x, value - x] 
    return []

if __name__ == "__main__":
    print(threeSum([-1, -3, 4]))