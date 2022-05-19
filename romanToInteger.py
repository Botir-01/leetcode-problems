class Solution:
    def __init__(self):
        self.roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        self.integer_numbers = 0

    def roman_to_int(self, s: str) -> int:
        for i in range(len(s) - 1, -1, -1):
            number = self.roman[s[i]]
            if 3 * number < self.integer_numbers:
                self.integer_numbers -= number
            else:
                self.integer_numbers += number
        return self.integer_numbers