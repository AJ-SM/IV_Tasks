from pyamaze import maze,agent
import tkinter as tk


mz=maze(10,10)
mz.CreateMaze(loopPercent=50)
a=agent(mz,shape='square',footprints=True,color='red')



def Mv_east (p):
    p = list(p)
    p[1] = p[1] + 1
    return tuple(p)

def M_west (p):
    p = list(p)
    p[1] = p[1] - 1
    return tuple(p)

def M_north (p):
    p = list(p)
    p[0] = p[0] - 1
    return tuple(p)
                         
def M_south (p):
    p = list(p)
    p[0] = p[0] + 1
    return tuple(p)

    
   
def DFS(m):


    begin = (10,10)
    current_node = [begin]
    visted = [begin]
    rvpath = {}

    pix = m.maze_map.keys()
    direction_info = m.maze_map.values()



    while len(current_node)>0:   
        fstnode = current_node.pop(0)
        if fstnode == (1,1):
            break

        for j in "ESNW":
                if (m.maze_map[fstnode][j]):
                    if j == "E":
                        node = Mv_east(fstnode)
                    
                
            
                    elif j == "W":
                        node = M_west(fstnode)
                    

                    elif j == "N":
                        node = M_north(fstnode)
                    

                    elif j == "S":
                        node = M_south(fstnode)
                   

                    if node in current_node:
                        continue
                    current_node.append(node)
                    visted.append(node)
                    rvpath[node] = fstnode
                    
                   

    fvpath = {}
    cell = (1,1)
    while cell != begin:
        fvpath[rvpath[cell]] = cell
        cell = rvpath[cell]
    return fvpath
path = DFS(mz)
mz.tracePath({a:path})






mz.run()







