class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Function to find the greatest common divisor
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        # Check if str1 can be formed by repeating a given pattern
        def canForm(s, pattern):
            if len(s) % len(pattern) != 0:
                return False
            return s == pattern * (len(s) // len(pattern))
        
        # Find the GCD of the lengths of str1 and str2
        gcd_len = gcd(len(str1), len(str2))
        
        # The potential largest string x that divides both str1 and str2
        potential_x = str1[:gcd_len]
        
        # Check if the potential_x can form both str1 and str2
        if canForm(str1, potential_x) and canForm(str2, potential_x):
            return potential_x
        else:
            return ""

