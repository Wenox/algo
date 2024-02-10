from collections import Counter
from typing import List

# OK, but time limit

class Solution:
    def is_anagram(self, counter, t: str) -> bool:
        return counter == Counter(t)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_words = {}
        for word in strs:
            matched = False

            # consider only groups of same length
            matched_groups = grouped_words.get(len(word), [])
            if not matched_groups:
                matched_groups.append([word])
                grouped_words[len(word)] = matched_groups
                continue

            counter = Counter(word)
            for group in matched_groups:
                if self.is_anagram(counter, group[0]):
                    group.append(word)
                    matched = True
                    break

            if not matched:
                matched_groups.append([word])

        return [item for sublist in grouped_words.values() for item in sublist]




