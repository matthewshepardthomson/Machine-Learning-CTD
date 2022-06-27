

def b2(x):
    return int(str(bin(x))[2:])

def b02(x,z=8):
    ans = str(b2(x))
    if len(str(ans)) < z:
        return "0"*(z-len(str(ans))) + str(ans)
    return ans

def b10(x):
    digits = str(x)
    total = 0
    for num in range(len(digits)):
        total += (2**(len(digits)-num-1) * (int(digits[num])))
    return total

#def init_state(wid):
#    return list("0"*(int((wid/2)-0.5)) + "1" + "0"*(int((wid/2)-0.5)))

def init_state(wid):
    newL = [0 for i in range(wid)]
    newL[int(wid/2)] = 1
    return newL

def next_state(row,method):
    ret = []
    ret.append(row[0])
    for num in range(len(row)-2):
        inp = "".join([str(row[num]),str(row[num+1]),str(row[num+2])])
        ret.append(method[inp])
    ret.append(row[-1])
    return ret



def list_to_string(state,a=". ",b="O "):
    return "".join([a if x == 0 else b for x in state])



zero7 = ("000","001","010","011","100","101","110","111")

def oneDconway(width,rule,gens):

    #Dictionary
    
    key = tuple(b02(rule))
    method = {}
    for num in range(8):
        method[zero7[num]] = int(key[num])

    print(method)

    #Rows
        
    state = init_state(width)
    print(list_to_string(state))
    for gen in range(gens):
        new = next_state(state,method)
        print(list_to_string(new))
        state = new

#oneDconway(121,90,300)

#Conway's game of life


def conRule(state,neighbors):
    if neighbors == 3:
        return 1
    elif neighbors == 2:
        return state
    else:
        return 0

def croprint(grid):
    for row in grid[1:-1]:
        print(row[1:-1])

def display(grid,z=". ",o="O "):
    for row in grid:
        print(list_to_string(row,z,o))
    print("\n")

pos = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))

def zerofy(grid):
    new = []
    new.append([0 for num in grid[0]] + [0,0])
    for row in grid:
        n = []
        n.append(0)
        for e in row:
            n.append(e)
        n.append(0)
        new.append(n)
    new.append([0 for num in grid[0]] + [0,0])
    return new

def dezero(grid):
    new = []
    for row in grid[1:-1]:
        new.append(row[1:-1])
    return new

def conRow(start):    
    starter = zerofy(start)
    
    new = []
    for row in range(len(starter)):
        nRow = []
        for column in range(len(starter[0])):
            n = 0
            for tup in pos:
                try:
                    #print(":",row,column,starter[row+(tup[0])][column+(tup[1])])
                    n += starter[row+(tup[0])][column+(tup[1])]
                except:
                    pass
            nRow.append(conRule(starter[row][column],n))
        new.append(nRow)
    return dezero(new)


def census(grid):
	total = 0
	for row in grid:
		for num in row:
			total += num
	return total
	
import subprocess
import time
def conway(start,gens,pause=0.2,z="x ",o="O "):
    m = census(start)
    display(start,z,o)
    counts = []
    cur = start
    for g in range(gens):
        counts.append(census(cur))
	new = conRow(cur)
	if new != cur:
	    cur = new
	else:
            print("Start:",m,"Max:",max(counts),"Min:",min(counts),"End:",census(cur),"Chars:",z,o)
	    return counts
	time.sleep(pause)
	subprocess.call("clear")
        display(cur,z,o)
    print("Start:",m,"Max:",max(counts),"Min:",min(counts),"End:",census(cur),"Chars:",z,o)
    return counts

##s = [[0,0,0,0,0,0,0,0,0],
##     [0,0,0,0,1,0,0,0,0],
##     [0,0,0,0,1,0,0,0,0],
##     [0,0,0,0,0,0,0,0,0],
##     [1,1,1,0,0,0,1,1,1],
##     [0,0,0,0,0,0,0,0,0],
##     [0,0,0,0,1,0,0,0,0],
##     [0,0,0,0,1,0,0,0,0],
##     [0,0,0,0,1,0,0,0,0]]

butterfly =["..................................................",
            "..................................................",
            "..................................................",
            "..................................................",
            "..................................................",
            "......................o.o.........................",
            "....................ooo.ooo.......................",
            "...................o...o...o......................",
            "...................o.o...o.o......................",
            "....................oo.o.oo.......................",
            "..................................................",
            "....................oo.o.oo.......................",
            "...................o.o...o.o......................",
            "...................o...o...o......................",
            "....................ooo.ooo.......................",
            "..................................................",
            "..................................................",
            "..................................................",
            "..................................................",
            "..................................................",
            "..................................................",
            "..................................................",
            "..................................................",
            "..................................................",
            "..................................................",
            "..................................................",
            "..................................................",
            "..................................................",
            "..................................................",
            "..................................................",
            "..................................................",
            ".................................................."]

def chart(nums):
    for num in nums:
        print("."*int(num/5)  + "|")
        

def toList(lofstrings):
    ret = []
    for row in lofstrings:
        ret.append([0 if x == "." else 1 for x in row])
    return ret


import random
def randomField(width,height,prob):
    new = []
    for row in range(height):
        new.append([0 if random.random() < prob else 1 for x in range(width)])
    return new

#s = randomField(40,40,.5)
s = toList(butterfly)

#conway(s,70,0.1,"x ","o ")
print("works!")








    


