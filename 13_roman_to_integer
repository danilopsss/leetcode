class Solution:
    CONVERSION_TABLE = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def get_roman_number(self, s):
        return self.CONVERSION_TABLE.get(s)
    
    def romanToInt(self, s: str) -> int:
        operations = [self.get_roman_number(s[0])]
        for idx in range(1, len(s)):
            if not self.get_roman_number(s[idx]) <=  operations[-1]:
                operations[-1] *= -1
            operations.append(
                    self.get_roman_number(s[idx])
                )

        return sum(operations)
