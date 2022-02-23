import sys


def processinp(fn):

    with open(fn,'r') as f:
        data=f.readline()
    grid=[]
    data=data.split()
    cnt=0
    for i in range(3):
        x=[]
        for j in range(3):
            x.append(data[cnt])
            cnt+=1
        grid.append(x)

    return grid

fname=sys.argv[2]
data=processinp(fname)
grid=[list(map(int,i)) for i in data]

GOAL=[[1,2,3],[8,0,4],[7,6,5]]



def getzero(grid):
    return [(i,j) for j in range(3) for i in range(3) if grid[i][j]==0]

def convert(state):
    res=[]
    for i in state:
        res.append(tuple(i))
    return res

def reinit():
    fname=sys.argv[2]
    data=processinp(fname)
    grid=[list(map(int,i)) for i in data]
    return grid

def show(state):
    for i in range(3):
        for j in range(3):
            if state[i][j]==0:
                print(' ',end=' ')
            else:
                print(state[i][j],end=' ')
            
        print()
    print()

def dfs(depth):

    parent_mapping={}

    # states variable has (state,depth)
    states=[[grid,0]]
    visited=set()
    sol=[]
    l=1
   
    current_depth=0
    while states:
        if current_depth==depth:
            if states[-1]!=GOAL:
                states.pop()
                sol.pop()
            

        if len(states)==0:
            # print("NO SOL FOUND")
            return visited,current_depth,sol,states,False,parent_mapping
            
        q=states.pop()       
        state,current_depth=q[0],q[1]
        
        
        coor=getzero(state)
        x,y=coor[0][0],coor[0][1]
        z=tuple(convert(state))
        visited.add(z)
        if z not in sol:
            sol.append((z,current_depth))
        s=list(map(list,state))
        


        if x-1>=0: #move up
            temp=list(map(list,state))
            
            state[x][y],state[x-1][y] = state[x-1][y],state[x][y] 
            w=tuple(convert(state))
            
                

            if w==tuple(convert(reinit())):
                parent_mapping[w]=None
            else:
                if w not in parent_mapping:
                    parent_mapping[w]=tuple(convert(temp))
                
            if tuple(convert(state)) not in visited:
                
                if state==GOAL:
                    states.append(state)
                    l+=1          
                    sol.append((tuple(convert(state)),current_depth+1))
                    visited.add(tuple(convert(state)))
                    return visited,current_depth+1,sol,states,True,parent_mapping
                if current_depth+1<=depth:
                    states.append([state,current_depth+1])
                l+=1
            
            state=list(map(list,s))


        if x+1<3:   #move down

            temp=list(map(list,state))

            state[x][y],state[x+1][y] = state[x+1][y],state[x][y]

            w=tuple(convert(state))
           
                

            if w==tuple(convert(reinit())):
                parent_mapping[w]=None
            else:
                if w not in parent_mapping:
                    parent_mapping[w]=tuple(convert(temp))
                

            if tuple(convert(state)) not in visited:
                
                
                if state==GOAL:
                    
                    
                    
                    states.append(state)
                    l+=1
                    
                    sol.append((tuple(convert(state)),current_depth+1))
                    visited.add(tuple(convert(state)))
                    
                    return visited,current_depth+1,sol,states,True,parent_mapping

                if current_depth+1<=depth:
                    states.append([state,current_depth+1])
                l+=1
            state=list(map(list,s))


        if y+1<3:   #move right

            temp=list(map(list,state))

            state[x][y],state[x][y+1] = state[x][y+1],state[x][y]

            w=tuple(convert(state))
            
                

            if w==tuple(convert(reinit())):
                parent_mapping[w]=None
            else:
                if w not in parent_mapping:
                    parent_mapping[w]=tuple(convert(temp))

                

            if tuple(convert(state)) not in visited:
                
                if state==GOAL:
                    states.append(state)
                    l+=1
                    sol.append((tuple(convert(state)),current_depth+1))
                    visited.add(tuple(convert(state)))
                    return visited,current_depth+1,sol,states,True,parent_mapping
                if current_depth+1<=depth:
                    states.append([state,current_depth+1])
                l+=1
            state=list(map(list,s))
        
        if y-1>=0:   #move left

            temp=list(map(list,state))

            state[x][y],state[x][y-1] = state[x][y-1],state[x][y]

            w=tuple(convert(state))
            
            if w==tuple(convert(reinit())):
                parent_mapping[w]=None
            else:
                if w not in parent_mapping:
                    parent_mapping[w]=tuple(convert(temp))

            if tuple(convert(state)) not in visited:
                
                if state==GOAL:                   
                    states.append(state)
                    l+=1
                    sol.append((tuple(convert(state)),current_depth+1))
                    visited.add(tuple(convert(state)))
                    return visited,current_depth+1,sol,states,True,parent_mapping
                if current_depth+1<=depth:
                    states.append([state,current_depth+1])
                l+=1
            state=list(map(list,s))
        
    return visited,current_depth,sol,states,False,parent_mapping



def fulldfs():
    global grid
    grid=reinit()
    v,d,p,alls,reach,m=dfs(15)
    if reach:

        print("GOAL REACHED AT DEPTH",d,"AND THE NUMBER OF STATES ENQUEUED",len(p))
        print("NUMBER OF MOVES IS",d)
    
        start=((1,2,3), (8,0,4), (7,6,5))

        rev_path=[start]
        while m[start]:
            nn=m[start]
            rev_path.append(nn)
            start=nn
  
        rev_path.reverse()
        for i in rev_path:
            show(i)
        
    else:
        print("GOAL NOT FOUND AND THE NUMBER OF STATES ENQUEUED IS",len(p))

    



def ids():
    global grid
    for i in range(1,16):
        grid=reinit()
        v,d,p,alls,reach,m=dfs(i)

        if reach:

            print("GOAL REACHED AT DEPTH",d,"AND THE NUMBER OF STATES ENQUEUED",len(p))
            print("NUMBER OF MOVES IS",d)
            # print(m)
            start=((1,2,3), (8,0,4), (7,6,5))

            rev_path=[start]
            while m[start]:
                nn=m[start]
                rev_path.append(nn)
                start=nn
  
            rev_path.reverse()
            for i in rev_path:
                show(i)
            break
        else:
            print("GOAL NOT FOUND AT DEPTH",i)













def ASTAR(START_STATE):
    #Define Variables to store Number of nodes Possible
    global State_Tracker
    State_Tracker = 0


    #Store the Value of the Huristic Choosen over here
    global algo


    #Store Visited list, To make sure same states are not visited Again
    global Frontier

    # Initialize visited Node
    Frontier = []

    #Store the Initial and Final States in a Variable

    global Initial
    global Final

    #Initialize the matrices to the given Dimensions
    Initial = [[0 for j in range(3)] for i in range(3)]
    Final = [[0 for j in range(3)] for i in range(3)]

    A_TILE_INIT_BOARD = Initial
    A_TILE_GOAL_STATE = Final


    #Define the function that calculates the Manhattan Distance between the tiles in the Initial and Final State
    def Calc_Huristic1(States):
    
        Huristic_Cost = []

        for M in States:
            target = {}
            state = {}

            sum = 0
            
            #Create a dictionary that contains, index and value pairs for easy computation. 
            for i in range(len(M)):
                for j in range(len(M[0])):
                    
                    target[A_TILE_GOAL_STATE[i][j]] = [i,j]
                    state[M[i][j]] = [i,j]
            # Calculate the Distance between the tiles in the Final and Initial Position
            for i in range(1,9):

                x = target[i]
                y = state[i]

                sum = sum + abs(x[0]-y[0]) + abs(x[1]-y[1])


            #Sum is for each state
            Huristic_Cost.append(sum)
        
        #return an array, that gives us huristic of each state, given an array of states.
        return Huristic_Cost

    #Define the Function that calculates the number of misplaced
    def Calc_Huristic2(States):

        Huristic_Cost = []

        for M in States:

            sum = 0
            
            #Calculate the number of misplaced tiles in each state
            for i in range(len(M)):
                for j in range(len(M[0])):

                    if(M[i][j]!=A_TILE_GOAL_STATE[i][j] and M[i][j]!=0):
                        sum+=1
                
            #Sum is for each state
            Huristic_Cost.append(sum)
        #return an array, that gives us huristic of each state, given an array of states.
        return Huristic_Cost


    #Definition of Tree Structure that is used to store the states
    class Tree:
        def __init__(self,State, d):
            self.val = State
            self.depth = d
            self.parent = "NONE"
            

    #Show function that lets us print a matrix in a presentable manner
    def show(M):
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j]==0:
                    print(' ',end=' ')
                else:
                    print(M[i][j], end= " ")
            print()   
        print()



    #Definition of Function that Finds the path based on Huristics to given optimal possible path
    def FindPath(Node,final = A_TILE_GOAL_STATE):
        global Frontier
        global State_Tracker


        while len(Frontier) > 0:

            #To store the values of the list elements in each class
            List_VAl = []
            for N in Frontier:
                List_VAl.append(N.val)


            #list that will have all the cost metrics per state
            costs = []
            
            global algo
            #check what Huristic was choosen
            if (algo == 'astar1'):
                costs = Calc_Huristic1(List_VAl)
            if (algo == 'astar2'):
                costs = Calc_Huristic2(List_VAl)

            
            #Add Depth to each of the cost functions that is compute f(n) + g(n): 

            for i in range(len(costs)):
                costs[i] = costs[i] + Frontier[i].depth

            #find Min cost
            x = min(costs)

            # Get the index corresponding to that move
            x1 = costs.index(x)
            
            # Get that possible next state
        
            Current_Node = Frontier.pop(x1)

            #Initialize Temp array so that given a state, you can find all possible next states that are admissible through manipulation
            temp =[[0 for j in range(len(A_TILE_GOAL_STATE[0]))] for i in range(len(A_TILE_GOAL_STATE))]

            #Current State 
            state = Current_Node.val

            #All possible next states stored here
            possible_states = []

            row_len = len(A_TILE_GOAL_STATE)
            col_len = len(A_TILE_GOAL_STATE[0])
            

            #Get the Value of 0 in the given state
            for i in range(len(state)):
                for j in range(len(state[0])):
                    if state[i][j] == 0:
                        x,y = i,j  

            #Set the Value of Temp to the state that you are currently in
            for i in range(len(state)):
                for j in range(len(state[0])):
                    temp[i][j] = state[i][j] 

            #Move left        
            if (y > 0):               
                temp[x][y], temp[x][y-1] = temp[x][y-1], temp[x][y]
                    
                    
                d = [[0 for i in range(len(temp[i]))] for j in range(len(temp))]
                for i in range(len(temp)):
                    for j in range(len(temp[0])):
                        d[i][j] = temp[i][j]
                        
                Node1 = Tree(d, Current_Node.depth + 1)
                Node1.parent = Current_Node
                possible_states.append(Node1)
                    
                    
                temp[x][y], temp[x][y-1] = temp[x][y-1], temp[x][y]

            #Move right
            if(y != col_len - 1):

                temp[x][y], temp[x][y+1] = temp[x][y+1], temp[x][y]
                
                
                b = [[0 for i in range(len(temp[i]))] for j in range(len(temp))]
                for i in range(len(temp)):
                    for j in range(len(temp[0])):
                        b[i][j] = temp[i][j] 
                Node2 = Tree(b, Current_Node.depth + 1)
                Node2.parent = Current_Node
                possible_states.append(Node2)
                
                
                temp[x][y], temp[x][y+1] = temp[x][y+1], temp[x][y]

                
            #Move up
            if (x > 0):             
                temp[x][y],temp[x-1][y] = temp[x-1][y], temp[x][y]
                
                
                c = [[0 for i in range(len(temp[i]))] for j in range(len(temp))]
                for i in range(len(temp)):
                    for j in range(len(temp[0])):
                        c[i][j] = temp[i][j] 
                Node3 = Tree(c, Current_Node.depth + 1)
                Node3.parent = Current_Node
                possible_states.append(Node3)
                
                
                temp[x][y],temp[x-1][y] = temp[x-1][y], temp[x][y]

            #Move down
            if(x != row_len -1):
                temp[x][y], temp[x+1][y] = temp[x+1][y], temp[x][y]
                
                

                a = [[0 for i in range(len(temp[i]))] for j in range(len(temp))]
                for i in range(len(temp)):
                    for j in range(len(temp[0])):
                        a[i][j] = temp[i][j] 
                Node4 = Tree(a, Current_Node.depth + 1)
                Node4.parent = Current_Node
                possible_states.append(Node4)

                temp[x][y], temp[x+1][y] = temp[x+1][y], temp[x][y]
    
            #Increase the State_Tracker, to depict all the states that have been enqueued:
            #check for the number of possible states that can be enqued
            if(x != row_len -1):
                State_Tracker+= 1

            if(y != col_len -1):
                State_Tracker+= 1

            if(x > 0):
                State_Tracker+= 1

            if(y > 0):
                State_Tracker+= 1

            #Stopping Conditions for Reccursion
            if(Current_Node.depth >= 15):
                pass
            #Check if you reached the goal Node
            elif(Current_Node.val == final):
                print("Goal State Reached")
                return Current_Node
            else:

                #Append New frontier Nodes
                for i in possible_states:
                    if(Frontier.count(i) == 0 ):

                        Frontier.append(i)

    #Define Main Funtion That controls the Process Flow
    def astar():
        #Set the Scope for all the global variables that were defined
        global algo
        global Initial
        global Final
        global Frontier

        algo=sys.argv[1]


        I = START_STATE
        for i in range(3):
            for j in range(3):
                Initial[i][j] = I[i][j]

        F = [[1,2,3],[8,0,4],[7,6,5]]
        for i in range(3):
            for j in range(3):
                Final[i][j] = F[i][j]


        #Initialize Tree 
        Node = Tree(A_TILE_INIT_BOARD, 0)

        #Add the Node to visited :
        Frontier.append(Node)

        Node = FindPath(Node)


        depth_node = Node.depth

        if(Node == None):
            print("No solution Found")
        else:
            print()
            print("Solution Found")
            print()
           
            res = []
            while(Node!= "NONE"):
                res.append(Node.val)
                Node = Node.parent
            
            res.reverse()
            for i in res:
                show(i)
                

        # print("Total Number of States that are Possible : ", State_Tracker)
        print("depth of the Tree or number of moves required: ", depth_node)
        print("No of States that are enqued : " , depth_node + 1)

    astar()


# GET THE COMMAND LINE ARGUMENTS AND START THE PROGRAM
algo=sys.argv[1]
if algo=='dfs':
    fulldfs()
if algo=='ids':
    ids()
if algo=='astar1':
    ASTAR(grid)
if algo=='astar2':
    ASTAR(grid)