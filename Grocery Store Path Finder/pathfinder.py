import colorama
from colorama import Fore
from copy import deepcopy

colorama.init(autoreset=True)


def display_shortest_path(mat, mat2, t_map, visited, x1, y1, x2, y2, min_dis, dis, pass_val):
    if x1 == x2 and y1 == y2:
        if min_dis > dis:
            min_dis = dis
            mat2 = deepcopy(t_map)
            for p_1 in range(20):
                for p_2 in range(20):
                    if visited[p_1][p_2] == 1:
                        mat2[p_1][p_2] = pass_val
        return min_dis, mat2
    if (((x1 == x2 - 1) and (y1 == y2)) or ((x1 == x2 + 1) and (y1 == y2)) or ((x1 == x2) and (y1 == y2 - 1)) or (
            (x1 == x2) and (y1 == y2 + 1))):
        if min_dis > dis:
            min_dis = dis + 1
            mat2 = deepcopy(t_map)
            for p_1 in range(20):
                for p_2 in range(20):
                    if visited[p_1][p_2] == 1:
                        mat2[p_1][p_2] = pass_val
        return min_dis, mat2

    visited[x1][y1] = 1

    # move to the bottom cell
    if isSafe(mat, visited, x1 + 1, y1) and min_dis > dis + 1:
        min_dis, mat2 = display_shortest_path(mat, mat2, t_map, visited, x1 + 1, y1, x2, y2, min_dis, dis + 1, pass_val)
    # move to the right cell
    if isSafe(mat, visited, x1, y1 + 1) and min_dis > dis + 1:
        min_dis, mat2 = display_shortest_path(mat, mat2, t_map, visited, x1, y1 + 1, x2, y2, min_dis, dis + 1, pass_val)
    # move to the top cell
    if isSafe(mat, visited, x1 - 1, y1) and min_dis > dis + 1:
        min_dis, mat2 = display_shortest_path(mat, mat2, t_map, visited, x1 - 1, y1, x2, y2, min_dis, dis + 1, pass_val)
    # move to the left cell
    if isSafe(mat, visited, x1, y1 - 1) and min_dis > dis + 1:
        min_dis, mat2 = display_shortest_path(mat, mat2, t_map, visited, x1, y1 - 1, x2, y2, min_dis, dis + 1, pass_val)

    visited[x1][y1] = 0
    return min_dis, mat2


def display_shortest_path_length(mat, mst_list, coordinates_list, route_list, length_a):
    path = 0
    t_route = []
    for n in range(length_a):
        temp_visited = []
        temp_visited = [[0 for v_1 in range(20)] for v_2 in range(20)]
        val1 = mst_list[n][0]
        val2 = mst_list[n][1]
        x1 = coordinates_list[val1][0]
        y1 = coordinates_list[val1][1]
        x2 = coordinates_list[val2][0]
        y2 = coordinates_list[val2][1]
        t_route = deepcopy(route_list)
        path, route_list = display_shortest_path(mat, route_list, t_route, temp_visited, x1, y1, x2, y2, 100, 0, n + 2)

    ends = []
    found = 0
    for f1 in range(length_a):
        found = 0
        for f2 in range(length_a):
            if mst_list[f1][0] == mst_list[f2][1]:
                found = 1
                break
        if not found:
            ends.append(mst_list[f1][0])
            break
    for f1 in range(length_a):
        found = 0
        for f2 in range(length_a):
            if mst_list[f1][1] == mst_list[f2][0]:
                found = 1
                break
        if not found:
            ends.append(mst_list[f1][1])
            break
    t_route = deepcopy(route_list)
    path, route_list = display_shortest_path(mat, route_list, t_route, temp_visited, 19, 10, coordinates[ends[0]][0],
                                             coordinates[ends[0]][1], 100, 0, 83)
    t_route = deepcopy(route_list)
    path, route_list = display_shortest_path(mat, route_list, t_route, temp_visited, 19, 10, coordinates[ends[1]][0],
                                             coordinates[ends[1]][1], 100, 0, 69)
    t_route = deepcopy(route_list)
    return route_list


def prim_algo(G, V):
    mst = []
    INF = 9999999
    minimumdistance = 0
    # number of vertices in graph
    # create a 2d array of size 5x5
    # for adjacency matrix to represent graph
    # selected will become true otherwise false
    # selected = [0, 0, 0, 0, 0]
    selected = []
    for f in range(V):
        selected.append(0)
    # set number of edge to 0
    no_edge = 0
    # the number of ede in minimum spanning tree will be
    # always less than(V - 1), where V is number of vertices in
    # graph
    # choose 0th vertex and make it true
    selected[0] = True
    # print for edge and weight
    while no_edge < V - 1:
        # For every vertex in the set S, find the all adjacent vertices
        # , calculate the distance from the vertex selected at step 1.
        # if the vertex is already in the set S, discard it otherwise
        # choose another vertex nearest to selected vertex  at step 1.
        minimum = INF
        x = 0
        y = 0
        for g in range(V):
            if selected[g]:
                for h in range(V):
                    if (not selected[h]) and G[g][h]:
                        # not in selected and there is an edge
                        if minimum > G[g][h]:
                            minimum = G[g][h]
                            x = g
                            y = h
        mst.append([x, y])
        minimumdistance += minimum
        selected[y] = True
        no_edge += 1
    return mst


def isSafe(mat, visited, x, y):
    safety = (0 <= x < 20 and 0 <= y < 20) and mat[x][y] != 1 and (not visited[x][y])
    return safety


def findShortestPath(mat, visited, x1, y1, x2, y2, min_dis, dis):
    if x1 == x2 and y1 == y2:
        if min_dis > dis:
            min_dis = dis
        return min_dis
    if (((x1 == x2 - 1) and (y1 == y2)) or ((x1 == x2 + 1) and (y1 == y2)) or ((x1 == x2) and (y1 == y2 - 1)) or (
            (x1 == x2) and (y1 == y2 + 1))):
        if min_dis > dis:
            min_dis = dis + 1
        return min_dis
    visited[x1][y1] = 1
    # move to the bottom cell
    if isSafe(mat, visited, x1 + 1, y1) and min_dis > dis + 1:
        min_dis = findShortestPath(mat, visited, x1 + 1, y1, x2, y2, min_dis, dis + 1)
    # move to the right cell
    if isSafe(mat, visited, x1, y1 + 1) and min_dis > dis + 1:
        min_dis = findShortestPath(mat, visited, x1, y1 + 1, x2, y2, min_dis, dis + 1)
    # move to the top cell
    if isSafe(mat, visited, x1 - 1, y1) and min_dis > dis + 1:
        min_dis = findShortestPath(mat, visited, x1 - 1, y1, x2, y2, min_dis, dis + 1)
    # move to the left cell
    if isSafe(mat, visited, x1, y1 - 1) and min_dis > dis + 1:
        min_dis = findShortestPath(mat, visited, x1, y1 - 1, x2, y2, min_dis, dis + 1)

    # backtrack: remove (x1,y1) from the visited matrix
    visited[x1][y1] = 0
    return min_dis


def findShortestPathLength(mat, x1, y1, x2, y2):
    visited = [[0 for i in range(20)] for j in range(20)]
    dis = 100
    if (x1 == 19 and y1 == 10 and x2 == 19 and y2 == 11) or (x1 == 19 and y1 == 11 and x2 == 19 and y2 == 10):
        return 0
    dis = findShortestPath(mat, visited, x1, y1, x2, y2, dis, 0)
    if dis != 100:
        return dis
    else:
        return -1


# driver code
location = []

print("\n=================================================================================================================================================\n")
print("\n                                           <<<    <<<    <<<     WELCOME     >>>    >>>    >>>                                                   \n")
print("\n=================================================================================================================================================\n\n")
with open("map.txt") as textFile:
    for line in textFile:
        location_t = [item.strip() for item in line.split(',')]
        location.append(location_t)

with open("storeitems.txt") as f:
    content = f.readlines()
    items = [x.strip() for x in content]

f = open("discounts.txt", "r")
discount = f.readlines()
discount = [x.strip() for x in discount]

x_c = []
y_c = []

for l in range(20):
    for m in range(20):
        location[l][m] = int(location[l][m])

for i in range(0, 20):
    for j in range(0, 20):
        temp = location[i][j]
        if temp == 1:
            x_c.append(i)
            y_c.append(j)

items_list = []
print("\nEnter number of shopping list items: ")
item_no = int(input())
print("\nEnter names of shopping list items: ")
for a in range(item_no):
    item = input()
    items_list.append(item)

print("\nYour Shopping list has been received !")
coordinates = []
index_positions = []
for b in items_list:
    if b in items:
        position = items.index(b)
        index_positions.append(position)

for c in index_positions:
    p1 = x_c[c]
    p2 = y_c[c]
    coordinates.append([p1, p2])

distances = []

for d in range(0, item_no, 1):
    temp = []
    x_1 = coordinates[d][0]
    y_1 = coordinates[d][1]
    for e in range(0, item_no, 1):
        x_2 = coordinates[e][0]
        y_2 = coordinates[e][1]
        dist = findShortestPathLength(location, x_1, y_1, x_2, y_2)
        temp.append(dist)
    distances.append(temp)

mst1 = prim_algo(distances, item_no)
length = len(mst1)

route_t = deepcopy(location)
complete_path = display_shortest_path_length(location, mst1, coordinates, route_t, length)

print("\n\n======================================================   <<<     DISCOUNTS     >>>   ============================================================")
print("\nItem\t\tDiscount\n")
for f1 in range(item_no):
    print(items_list[f1], "\t\t", discount[index_positions[f1]])

complete_path[19][10] = "X"
complete_path[19][11] = "X"
for c1 in range(item_no):
    xv1 = coordinates[c1][0]
    xv2 = coordinates[c1][1]
    complete_path[xv1][xv2] = "X"

print("\n\n==============================================   <<<     OPTIMAL PATH WITH DIRECTIONS     >>>   ================================================")
print("\n\nHere is your path with the directions.\nFollow this path to save your time!\n\n")
for z1 in range(20):
    for z2 in range(20):
        if complete_path[z1][z2] == 83:
            print(Fore.RED + 'S', end=" ")
        elif complete_path[z1][z2] == 69:
            print(Fore.RED + 'E', end=" ")
        elif complete_path[z1][z2] != 1 and complete_path[z1][z2] != 0:
            print(Fore.RED + str(complete_path[z1][z2]), end=" ")
        else:
            print(complete_path[z1][z2], end=" ")
    print("")

aisles = []
for coord in range(len(coordinates)):
    if coordinates[coord][0] == 0:
        aisles.append("upper shelf")
    elif coordinates[coord][1] == 0:
        aisles.append("first aisle")
    elif coordinates[coord][1] == 2:
        aisles.append("second aisle")
    elif coordinates[coord][1] == 4:
        aisles.append("third aisle")
    elif coordinates[coord][1] == 6:
        aisles.append("fourth aisle")
    elif coordinates[coord][1] == 8:
        aisles.append("fifth aisle")
    elif coordinates[coord][1] == 10:
        aisles.append("sixth aisle")
    elif coordinates[coord][1] == 12:
        aisles.append("seventh aisle")
    elif coordinates[coord][1] == 14:
        aisles.append("eighth aisle")
    elif coordinates[coord][1] == 16:
        aisles.append("ninth aisle")
    elif coordinates[coord][1] == 18:
        aisles.append("tenth aisle")

d1 = 0
d2 = 0
temp_d = 500
print("\nDIRECTIONS:\n")
for num in range(item_no - 1):
    d1 = mst1[num][0]
    d2 = mst1[num][1]
    if temp_d != d1:
        print("pick", items_list[d1], "from", aisles[d1])
        print("pick", items_list[d2], "from", aisles[d2])
    else:
        print("pick", items_list[d2], "from", aisles[d2])
    temp_d = d2
print("\n======================================================   <<<     GOOD BYE     >>>   ============================================================\n")