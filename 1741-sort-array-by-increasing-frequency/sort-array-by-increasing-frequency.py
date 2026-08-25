class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        result = sorted(nums, key=lambda x: (freq[x], -x))
        return result
        

#"Given these two elements (a and b), which one should come first?"
#It does not swap elements itself. It only returns a negative, positive, or zero value. Python's timsort algorithm uses that answer to decide whether to keep the order or reorder the elements.