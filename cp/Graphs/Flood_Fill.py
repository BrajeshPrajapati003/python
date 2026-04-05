'''
Given:
    a image image
    a starting cell (sr, sc)
    a newColor
Goal: Replace the color of starting cell & all connected same-color cells with newColor
'''
def floodFill(image, sr, sc, newColor):
    original = image[sr][sc]

    if original == newColor: # imp edge case
        return image
    
    dfs(image, sr, sc, original, newColor)
    return image


def dfs(image, i, j, oc, nc):
    n = len(image); m = len(image[0])

    # boundary + color check
    if i<0 or j<0 or i>=n or j>=m or image[i][j] != oc:
        return
    
    # color change
    image[i][j] = nc

    # explore all 4 directions
    dfs(image, i-1, j, oc, nc)
    dfs(image, i+1, j, oc, nc)
    dfs(image, i, j-1, oc, nc)
    dfs(image, i, j+1, oc, nc)
