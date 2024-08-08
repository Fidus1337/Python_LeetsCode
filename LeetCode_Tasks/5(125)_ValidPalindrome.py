"""
A phrase is a palindrome if, after converting all uppercase 
letters into lowercase letters and removing 
all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
"""


class Solution:
    def isPalindrome_worst_solution(self, sentence: str) -> bool:
        temp_list = []

        for letter in sentence:
            if letter.isalnum():
                temp_list.append(letter.lower())
        if temp_list == list(reversed(temp_list)):
            return True
        else:
            return False

    def isPalindrome(self, sentence: str) -> bool:
        left, right = 0, len(sentence) - 1

        sentence = sentence.lower()

        while left < right:
            if not sentence[left].isalnum():
                left += 1
            elif not sentence[right].isalnum():
                right -= 1
            else:
                if sentence[left] != sentence[right]:
                    return False
                left += 1
                right -= 1

        return True


sol = Solution()
s = 'A man, a plan, a canal: Panama'
print(sol.isPalindrome(s))
