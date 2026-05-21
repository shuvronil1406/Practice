#LC 17. Letter Combinations of a Phone Number

#CODE:

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def letterCombinations(self, digits: str):
        
            if not digits:
                return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        ans = []

        def backtrack(index, path):

            if len(path) == len(digits):
                ans.append(path)
                return

            possible_letters = phone[digits[index]]

            for letter in possible_letters:
                backtrack(index + 1, path + letter)

        backtrack(0, "")

        return ans
        
        