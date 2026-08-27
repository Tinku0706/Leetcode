class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mp=Counter(words)
        ls = list(mp.keys())     
        ls.sort(key=lambda x: (-mp[x], x))
        return ls[:k]  #means "give me the top k elements" 
    #-mp[x] → higher frequency comes first
#x → if frequencies are equal, alphabetical order
# class Solution:
#     def topKFrequent(self, words: List[str], k: int) -> List[str]:
#         mp=Counter(words)
#         ls=[]
#         mp=dict(sorted(mp.items(), key=lambda x: (-x[1], x[0])))
#         for key,value in mp.items():
#             if len(ls)<k:
#                 ls.append(key)
#             else:
#                 break
#         return ls
