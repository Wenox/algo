# Revisit: 2 – 10/02/2024
# Revisit: 2 – 14/06/2025
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for i, word in enumerate(words):
            if x in word:
                result.append(i)
        return result