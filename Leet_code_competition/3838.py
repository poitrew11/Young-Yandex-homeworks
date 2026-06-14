"""
First heavy realization
"""

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        s = ''
        for i in range(len(words)):
            full_sum = 0
            for j in range(len(words[i])):
                ch = ord(words[i][j]) - 97
                full_sum += weights[ch]
            sum_after_mod = full_sum % 26
            mod_for_norm = abs(25 - sum_after_mod)
            final_ch = mod_for_norm + 97
            final_ch = chr(final_ch)
            s += final_ch
        return s
