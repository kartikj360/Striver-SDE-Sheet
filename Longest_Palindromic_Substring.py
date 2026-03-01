"""
5. Longest Palindromic Substring
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome=""
        palindrome_len=0
        for i in range(len(s)):

            # odd
            left,right=i,i
            while left>=0 and right< len(s) and s[left]==s[right]:
                if (right-left+1)>palindrome_len:
                    palindrome_len=right-left+1
                    palindrome=s[left:right+1]
                left-=1
                right+=1
            # even 
            left,right=i,i+1
            while left>=0 and right< len(s) and s[left]==s[right]:
                if (right-left+1)>palindrome_len:
                    palindrome_len=right-left+1
                    palindrome=s[left:right+1]
                left-=1
                right+=1
        return palindrome