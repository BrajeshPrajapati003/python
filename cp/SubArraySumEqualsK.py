class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        sum = 0
        map = {0: 1}

        for num in nums:
            sum += num

            if (sum - k) in map:
                ans += map[sum - k]

            map[sum] = map.get(sum, 0) + 1

        return ans

# Imap: How many times have I seen a prefix sum such that removing it gives sum = k?
