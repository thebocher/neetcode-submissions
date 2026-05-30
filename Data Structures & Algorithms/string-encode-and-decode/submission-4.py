class Solution:

    def encode(self, strs: List[str]) -> str:
        result = '#'.join([f'{len(s)}#{s}' for s in strs])
        return result

    def decode(self, s: str) -> List[str]:
        i = 0
        strs = []

        print(s)
        while i < len(s):
            length_end = s.index('#', i)
            length = int(s[i:length_end])
            word = s[length_end+1:length_end+1+length]
            strs.append(word)
            i = length_end+1+length+1
        
        return strs
                