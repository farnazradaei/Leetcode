from collections import Counter
class Solution(object):
    def areOccurrencesEqual(self, s):
        counts = Counter(s)
        values = counts.values()
        
        if  len(set(values)) == 1:
                return(True)
        else:
                return(False)