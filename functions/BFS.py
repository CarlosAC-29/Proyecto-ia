from classes.hash_table import HashTable
from classes.node import Node
 
def solve_game_BFS(startingState, map):
    

    operations = [[-1,0],[1,0],[0,-1],[0,1]]
    hash_table = HashTable(50)

    def isValid(state):
        if len(state) > 2:
            if ((map[state[0][0]][state[0][1]])=='W'):
                return False
            if ((map[state[1][0]][state[1][1]])=='W'):
                return False
            if ((map[state[2][0]][state[2][1]])=='W'):
                return False
            if (state[1] == state[2]):
                return False
            return True
        else:
            if ((map[state[0][0]][state[0][1]])=='W'):
                return False
            if ((map[state[1][0]][state[1][1]])=='W'):
                return False
            return True

    #Función que determina si un estado es meta, lo hace evaluando si quedan cajas en el estado
    def isSolution(state):
        if len(state) > 2:
            if ((map[state[1][0]][state[1][1]] == "X") and (map[state[2][0]][state[2][1]] == "X")):
                return True
            else:
                return False
        else:
            if (map[state[1][0]][state[1][1]] == "X") :
                return True
            else:
                return False


    #A esta funcion le entra un estado y un movimiento a ejecutar y tiene que retornar el nuevo estado
    def newState (state, movement):
        if len(state) > 2 : 
            newPositionP = [state[0][0]+movement[0], state[0][1]+movement[1]]
            newPositionB1 =state[1]
            newPositionB2 = state[2]
            if (newPositionP == state[1]): 
                newPositionB1 = [state[1][0]+movement[0], state[1][1]+movement[1]]
            if (newPositionP == state[2]):
                newPositionB2 = [state[2][0]+movement[0], state[2][1]+movement[1]]
            finalState = [newPositionP, newPositionB1, newPositionB2]
            return finalState
        else:
            newPositionP = [state[0][0]+movement[0], state[0][1]+movement[1]]
            newPositionB1 =state[1]
            if (newPositionP == state[1]): 
                newPositionB1 = [state[1][0]+movement[0], state[1][1]+movement[1]]
            finalState = [newPositionP, newPositionB1]
            return finalState

    def makeString (state):
        mystate=""
        for data in state:
            for num in data:
                mystate += str(num)
        return mystate

    #Retorna False si Un valor ya esta en la tabla hash y True si no esta
    def noHash (state):
        stateStr= makeString(state)
        if hash_table.get_val(stateStr):
            return False
        else:
            return True

    def setHash (state):
        stateStr= makeString(state)
        hash_table.set_val(stateStr, 'A')

    def path(world):
        if world.parent != None :
                if world.madeBy == operations[0] :
                    Solution.append('U')
                    path(world.parent)
                if world.madeBy == operations[1] :    
                    Solution.append('D')
                    path(world.parent)
                if world.madeBy == operations[2] :
                    Solution.append('L')
                    path(world.parent)
                if world.madeBy == operations[3] :
                    Solution.append('R')
                    path(world.parent)

    #Creacion del nodo Raiz
    firstdic = {"state": startingState, "parent":None, "applied":None, "depth":0}
    Solution = []

    firstNode = Node(firstdic)
    pile = [firstNode]

#Este es el while que va recorriendo el arbol
    while True:
        if len(pile) == 0:
            print("Fallo no se halló solucion")
            break
        else:
            theNode=pile.pop((len(pile)-1))
            if isSolution(theNode.state):
                path(theNode)
                Solution.reverse()
                palabra =""
                for i in Solution:        
                    palabra += i
                return palabra

            else:
                firstOpe = newState(theNode.state, operations[3])
                secondOpe = newState(theNode.state, operations[2])
                thirdOpe = newState(theNode.state, operations[1])
                fourthOpe = newState(theNode.state, operations[0])
                if(noHash(firstOpe) and isValid(firstOpe)):
                    oneDic = {"state": firstOpe, "parent":theNode, "applied":operations[3], "depth":theNode.depth+1}
                    setHash(firstOpe)
                    firsNode = Node(oneDic)
                    if firsNode.depth <= 64:
                        pile.append(firsNode)
                if(noHash(secondOpe) and isValid(secondOpe)):      
                    oneDic = {"state": secondOpe, "parent":theNode, "applied":operations[2], "depth":theNode.depth+1}
                    setHash(secondOpe)
                    secondNode = Node(oneDic)
                    if secondNode.depth <= 64:
                        pile.append(secondNode) 
                if(noHash(thirdOpe) and isValid(thirdOpe)): 
                    oneDic = {"state": thirdOpe, "parent":theNode, "applied":operations[1], "depth":theNode.depth+1}
                    setHash(thirdOpe)
                    thirdNode = Node(oneDic)
                    if thirdNode.depth <= 64:
                        pile.append(thirdNode) 
                if(noHash(fourthOpe) and isValid(fourthOpe)):
                    oneDic = {"state": fourthOpe, "parent":theNode, "applied":operations[0], "depth":theNode.depth+1}
                    setHash(fourthOpe)
                    fourthNode = Node(oneDic)
                    if fourthNode.depth <= 64:        
                        pile.append(fourthNode)
