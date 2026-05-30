class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 1
        longest = 0

        while r <= len(s):
            counts = {}
            for ss in s[l:r]:
                counts.setdefault(ss, 0)
                counts[ss] += 1
            
            max_counts = max(counts.values())
            subs_len = r-l
            
            if subs_len - max_counts > k:
                l += 1
                continue
            
            longest = max(longest, subs_len)
            r += 1
            print(r)
        
        return longest

            

            