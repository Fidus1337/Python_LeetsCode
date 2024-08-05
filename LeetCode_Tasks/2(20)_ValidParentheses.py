"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets_open = {
            '{': '}',
            '(': ')',
            '[': ']'
        }
        brackets_closed = {
            '}': '{',
            ')': '(',
            ']': '['
        }
        temp_list = []

        for symbol in s:
            if symbol in brackets_open:
                # If we find open brackets, then we add it to temp_list
                temp_list.append(symbol)
            elif symbol in brackets_closed:
                if temp_list and temp_list[-1] == brackets_closed[symbol]:
                    # If we find closed brackets and the last open bracket matches
                    temp_list.pop()
                else:
                    # For unpredictable cases
                    return False

        # If our temporary list is empty, then we return True
        return not temp_list

    def isValid2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(list(s)) % 2 != 0:
            return False
        L = []
        for x in s:
            if x == "(":
                L.append(")")
            elif x == "[":
                L.append("]")
            elif x == "{":
                L.append("}")
            elif len(L) != 0 and x == L.pop():
                continue
            else:
                return False
        if len(L) != 0:
            return False
        return True


# Пример использования
solution = Solution()
print(solution.isValid("({{{{}}}))"))  # True
print(solution.isValid("()[]{}"))  # True
print(solution.isValid("(]"))  # False
print(solution.isValid("([)]"))  # False
print(solution.isValid("{[]}"))  # True
