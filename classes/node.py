#Clase nodo, esta clase se encarga de crear los nodos, 
#Recibe un estado del problema,
#Una referencia al nodo padre  
#La operacion con la que fue creado,
#Con la profundidad del nodo padre le sumo 1 a la profundidad del nodo actual

class Node:
    def __init__(self, values):
        self.state = values["state"]
        self.parent = values["parent"]
        self.madeBy = values["applied"]
        self.depth = values["depth"]


#Función que determina si una operación es válida si el jugador no chocaría con una pared
