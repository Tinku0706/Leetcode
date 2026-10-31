class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mp=Counter(words)
        ls = list(mp.keys())     
        ls.sort(key=lambda x: (-mp[x], x))
        return ls[:k]  #means "give me the top k elements" 
    #-mp[x] → higher frequency comes first
#x → if frequencies are equal, alphabetical order