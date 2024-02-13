from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        return ''.join([chr(len(s)) + s for s in strs])

    def decode(self, s: str) -> List[str]:
        result, i = [], 0
        while i < len(s):
            word_length = ord(result[i])
            i += 1
            result.append(s[i:i+word_length])
            i += word_length
        return result
