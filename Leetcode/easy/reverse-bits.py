""" 
# REVERSE BITS

Reverse bits of a given 32 bits unsigned integer.

Note:

Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.
Follow up:

If this function is called many times, how would you optimize it?

Example 1:

Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
 
Constraints:

The input must be a binary string of length 32 
"""

class Solution:
    def reverseBits(self, n: int) -> int:      
      l = 1 << 31
      r = 1 
      
      # Continue until the bits from each bitmask meet each other.
      while l > r:
        # Check if current bits from the left and right are 1 or 0.
        l_bit = 1 if n & l else 0
        r_bit = 1 if n & r else 0
        
        # If two bits are different, we need to inverse them.
        if l_bit != r_bit:
          # Invert the bits in original number usin XOR.
          n = n ^ l ^ r
        
        # Shiftin left bitmask to the right and the right one to the left.
        l = l >> 1
        r = r << 1
        
      return n