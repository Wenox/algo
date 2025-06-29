# Revisit: 1 –– 11/02/2024
# Revisit: 2 –– 14/06/2025
class Solution:
    def defangIPaddr(self, address: str) -> str:
        # return address.replace('.', '[.]')
        result = [''] * (len(address) + 6)
        i = 0
        for c in address:
            if c == '.':
                result[i:i + 3] = '[.]'
                i += 3
            else:
                result[i] = c
                i += 1
        return ''.join(result)
