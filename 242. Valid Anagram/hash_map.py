class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # construct letters_count map
        letters_count = {}
        for letter in s:
            if letter in letters_count:
                letters_count[letter] += 1
            else:
                letters_count[letter] = 1

        # check letter exists
        for letter in t:
            if letters_count.get(letter, 0) > 0:
                letters_count[letter] -= 1
            else:
                return False

        return all(count == 0 for count in letters_count.values())
