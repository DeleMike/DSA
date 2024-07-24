def maxArea(self, heights: List[int]) -> int:
    l = 0
    r = len(heights) - 1
    height_of_shortest_bar = 0 # length
    maximum_value = 0

    while l < r:
        distance_btw_l_r = r - l # get breadth
        if heights[r] < heights[l]:
            height_of_shortest_bar = heights[r]
        else:
            height_of_shortest_bar = heights[l]

        area = distance_btw_l_r * height_of_shortest_bar # A = length * breadth
        
        # update max value
        if area > maximum_value :
            maximum_value = area
        
        # update pointers
        if heights[r] < heights[l]:
            r -= 1
        else:
            l += 1

    return maximum_value


