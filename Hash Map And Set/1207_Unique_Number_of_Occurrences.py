class Solution:
    def uniqueOccurrences(self, arr):
        occurrence_count = {}
        for num in arr:
            if num in occurrence_count:
                occurrence_count[num] += 1
            else:
                occurrence_count[num] = 1
        counts = list(occurrence_count.values())
        return len(counts) == len(set(counts))
