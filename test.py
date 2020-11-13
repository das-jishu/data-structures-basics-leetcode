class Solution:
    def numDecodings(self, s: str) -> int:
        return self.decode(s, 0, 1) + self.decode(s, 0, 2)
        
    def decode(self, s, start, jump):
        print("checking s:",s[start:],"with jump:",jump)
        if start >= len(s) or start + jump > len(s):
            return 0

        temp = s[start:start+jump]
        if start + jump == len(s):
            print("temp:", temp)
            if 1 <= int(temp) <= 26:
                print("VALID")
                return 1
            else:
                return 0

        if not 1 <= int(temp) <= 26:
            return 0
    
        return self.decode(s, start + jump, 1) + self.decode(s, start + jump, 2)
    
if __name__ == "__main__":
    s = Solution()
    print(s.numDecodings("12252636"))