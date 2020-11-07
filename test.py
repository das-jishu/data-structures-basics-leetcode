class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        x = self.permute(nums)
        return x
    
    def permute(self, nums):
        if len(nums) == 1:
            return [nums]

        result = []
        for i, x in enumerate(nums):
            if i > 0 and x == nums[i - 1]:
                continue
            y = self.permute(nums[:i] + nums[i+1:])
            for t in y:
                t.append(x)
                result.append(t)

        return result

if __name__ == "__main__":
    s = Solution()
    print(s.permuteUnique([1, 1, 2]))