# Revisit: 2
from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        return ''.join([self.encode_length(len(s)) + s for s in strs])

    def encode_length(self, num: int) -> str:
        return f'{num:03d}'

    def decode(self, s: str) -> List[str]:
        result, i = [], 0
        while i < len(s):
            word_length = int(s[i:i+3])
            i += 3
            result.append(s[i:i+word_length])
            i += word_length
        return result
