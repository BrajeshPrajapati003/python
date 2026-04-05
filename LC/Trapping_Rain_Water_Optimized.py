# 42. Trapping_Rain_Water_Optimized
def trap(height):
    n = len(height)

    if n == 0:
        return 0
    
    left, right = 0, len(height)-1
    leftMax = rightMax = 0 # max seen from left & right
    water = 0
    
    while left <= right:

        # if left side is smaller -> process left
        if height[left] <= height[right]:

            if height[left] >= leftMax: # update max
                leftMax = height[left]
            else: # water trapped
                water += leftMax - height[left]

            left += 1

        # process right side
        else:

            if height[right] >= rightMax:
                rightMax = height[right]
            else:
                water += rightMax - height[right]

            right -= 1
    
    return water

height = list(map(int, input().split(",")))
print(trap(height))
