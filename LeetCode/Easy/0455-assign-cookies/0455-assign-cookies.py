class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        s.sort()
        g.sort()

        now = 0
        child = 0
        n = 0
        for i in g:

            while now < len(s):
                if i > s[now]:
                    now += 1
                else:
                    n += 1
                    now += 1
                    break
                    
            if now >= len(s):
                break

        
        return n

