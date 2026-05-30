class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = {}

        for v in t:
            t_map.setdefault(v, 0)
            t_map[v] += 1
        
        need = len(t_map)
        have = 0

        t_have = {
            v: 0 for v in t_map
        }
        l, r = 0, 1
        result = None

        print(t_map)
        while True:
            # print(11, have, need, s[min(len(s)-1, l)], s[min(r, len(s))-1], t_have, l, r)
            if have < need:
                if r > len(s):
                    break

                v = s[r-1]
                if v in t_map:
                    t_have[v] += 1

                    if t_have[v] == t_map[v]:
                        have += 1
                    
                    if have != need:
                        r += 1
                else:
                    r += 1

                if r > len(s):
                    break
            else:
                if result is None:
                    result = [l, r]
                elif result[1]-result[0] > r-l:
                    result = [l, r]

                v = s[l]
                if v in t_map:
                    t_have[v] -= 1
                    
                    if t_have[v] < t_map[v]:
                        have -= 1
                        r += 1
                
                l += 1

                if l >= r:
                    break
            # print(22, have, need, s[min(len(s)-1, l)], s[min(r, len(s))-1], t_have, l, r)
            
        
        if result is None:
            return ''

        return s[result[0]:result[1]]

        
            