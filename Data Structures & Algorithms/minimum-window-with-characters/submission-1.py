class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = {}
        
        for v in t:
            t_map[v] = 1 + t_map.get(v, 0)
        
        counts = {}
        l = 0
        have, need = 0, len(t_map)
        res = [-1, -1]
        res_len = float('inf')

        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)

            if s[r] in t_map and counts[s[r]] == t_map[s[r]]:
                have += 1
            
            while have == need:
                if r-l+1 < res_len:
                    res_len = r-l+1
                    res = [l, r]

                counts[s[l]] -= 1

                if s[l] in t_map and counts[s[l]] < t_map[s[l]]:
                    have -= 1

                l += 1
        l, r = res

        return s[l:r+1] if res_len != float('inf') else ''
