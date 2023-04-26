class Solution:
    def isHappy(self, n: int) -> bool:
        counter = 0
        while n != 7 and n != 1:
            if counter > 9:
                return False
            
            n = sum([eval(x) ** 2 for x in str(n)])
            counter += 1
        return n in [1, 7]
