class Solution:
    def get_max(self, v1, v2):
        return max(v1, len(v2))

    def lengthOfLongestSubstring(self, s: str) -> int:
        pointer = 0
        max_len = 0
        temp_word = ""
        while pointer < len(s):
            if s[pointer] in temp_word:
                index = temp_word.index(s[pointer])
                temp_word = temp_word[index + 1:]
            temp_word += s[pointer]
            max_len = self.get_max(max_len, temp_word)
            pointer += 1
        if temp_word:
            max_len = self.get_max(max_len, temp_word)
        return max_len
