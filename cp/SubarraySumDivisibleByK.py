# count subarrays with sum divisible by k
def countSubarraySumDivisibleByK(nums: list, k: int) -> int:
    map = {0: 1}
    sum = count = 0

    for i in range(len(nums)):
        sum += nums[i]

        rem = ((sum%k)+k)%k # for -ve values
        if rem in map:
            count += map[rem]
        
        map[rem] = map.get(rem, 0) + 1
    return count

nums = list(map(int, input().split()))
k = int(input())

print(countSubarraySumDivisibleByK(nums, k))

