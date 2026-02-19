# Count subarrays whose xor = k
def countXorSubarraysEqualK(nums: list, k: int) -> int:
    map = {0:1}
    count = xorVal = 0

    for num in nums:
        xorVal ^= num
        needed = xorVal ^ k

        if needed in map:
            count += map[needed]

        map[xorVal] = map.get(xorVal, 0) + 1
    
    return count


