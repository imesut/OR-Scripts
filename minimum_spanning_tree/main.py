import random
import time
start_time = time.time()

cn = [] #connected_nodes
cnk = ["0", "A", "B", "C", "D", "E", "T"] #unconnected_nodes
n = len(cnk)

"""
To solve Example 2 at page 11, define cnk and arcs like below:
cnk = [1, 2, 3, 4, 5, 6]
arcs = [[1, 2, 1], [1, 4, 7], [4, 6, 3], [3, 6, 10], [3, 4, 5], [1, 3, 6],[2, 4, 4], [2, 3, 6], [2, 5, 3], [1, 5, 9], [4, 5, 8]]
"""

#arcs[from, to, weight]
arcs = [
["0", "A", 2], ["0", "C", 4], ["0", "B", 5], ["A", "B", 2], ["A", "D", 7], ["B", "C", 1],
["B", "D", 4], ["B", "E", 3], ["D", "E", 1], ["D", "T", 5], ["E", "T", 7], ["C", "E", 4]]

def arc(i): #lists the arc related to node i
    arc_i = []
    for j in arcs:
        if j[0] == i or j[1] == i:
            arc_i.append(j)
    return arc_i

current_node = random.sample(cnk, 1)[0] #Initialize with random node
cn.append(current_node) #add that point to connected nodes array

def getKey(item):
    return item[2]

while len(cnk)> 0:
    #find the minimum weighted arcs between each node
    #to find minimum weight so to list weights based arc list
    weights = []
    for i in cn:
        #take the minimum weighted arc of item
        try:
            selected_arc = sorted(arc(i), key=getKey)[0]
            weights.append(selected_arc)
            #Get the minimum of minimum weighted arc
            selected_arc = sorted(weights, key=getKey)[0]
        except:
            pass

    if selected_arc[0] in cn and selected_arc[1] in cn:
        arcs.remove(selected_arc)
    else:
        #add other node to the cn list
        #Connected-Unconnected Nodes Lists Organizer Code Block
        if selected_arc[0] not in cn:
            cn.append(selected_arc[0])
            cnk.remove(selected_arc[0])
        if selected_arc[1] not in cn:
            cn.append(selected_arc[1])
            cnk.remove(selected_arc[1])
        print("arc:", selected_arc[0], selected_arc[1])
        arcs.remove(selected_arc)
        n = n-1
        if n == 1:
            break
finish_time = time.time()

print("Execution time: ", str(finish_time - start_time), "second") #average time: 0.00067 second on 1.6gHz processor and 4gb ram
