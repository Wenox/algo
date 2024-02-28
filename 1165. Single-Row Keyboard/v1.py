class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        key_to_index = {}
        for i in range(len(keyboard)):
            key_to_index[keyboard[i]] = i

        time = 0
        curr_index = 0
        for c in word:
            new_index = key_to_index[c]
            time += abs(curr_index - new_index)
            curr_index = new_index

        return time
