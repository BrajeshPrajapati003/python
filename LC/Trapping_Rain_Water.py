# 42. Trapping Rain Water
def trap(height):
    n = len(height)

    # edge case
    if n == 1:
        return 0
    
    # create arrays
    leftMax = [0]*n
    rightMax = [0]*n

    # fill leftMax -> max height from left till idx i
    leftMax[0] = height[0]
    for i in range(1, n):
        leftMax[i] = max(leftMax[i-1], height[i])

    # fill rightMax -> max height from right till idx i
    rightMax[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        rightMax[i] = max(rightMax[i+1], height[i])

    # calc water
    water = 0
    for i in range(n):
        # water level = min of both sides
        water += min(leftMax[i], rightMax[i]) - height[i]
    
    return water

height = list(map(int, input().split(",")))
print(trap(height))
