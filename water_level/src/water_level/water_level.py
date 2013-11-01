'''
Created on Nov 1, 2013

@author: sina
'''

def find_max_index(height_map):
    return height_map.index(max(height_map))

def find_min_index(height_map):
    return height_map.index(min(height_map))

def calc_vol(height_map, water_height):
    vol = 0
    print(height_map)
    print(water_height)
    for i in height_map:
        if water_height - i < 0:
            print("WTF")
        vol += water_height - i
    return vol

def find_vol(height_map):
    if len(height_map) < 3:
        return 0
    min_index = find_min_index(height_map)
    print("min_index: %s" % min_index)
    
    if min_index == 0:
        return find_vol(height_map[1:])
    if min_index == len(height_map) - 1:
        return find_vol(height_map[:min_index])
    
    left_partition = height_map[:min_index]
    left_hill = find_max_index(left_partition)
    print("left_hill: %s" % left_hill)
    print("left_partition: %s" % left_partition)

    right_partition = height_map[min_index:]
    right_hill = min_index + find_max_index(right_partition)
    print("right_partition: %s" % right_partition)
    print("right_hill: %s" % right_hill)

    water_height = min([height_map[right_hill], height_map[left_hill]])
    vol = calc_vol(height_map[left_hill+1:right_hill], water_height)

    vol += find_vol(height_map[right_hill:])
    return vol

if __name__ == '__main__':
    find_vol([2,5,1,3,1,2,1,7,7,6,1,7])

