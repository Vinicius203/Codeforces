friends_number, fence_height = map(int, input().split())


def calc_road_width(heights):
    road_width = 0
    for height in heights:
        if height <= fence_height:
            road_width += 1
        else:
            road_width += 2

    return road_width


heights = list(map(int, input().split()))
min_road_width = calc_road_width(heights)
print(min_road_width)
