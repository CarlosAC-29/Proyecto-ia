import streamlit as st
from functions.DFS import solve_game_BFS
from functions.BFS import solve_game_DFS
from functions.BFSI import solve_game_BFSI

def main():
    st.title("Sokoban")

    # Widget para seleccionar el archivo de entrada
    input_file = st.file_uploader("Seleccionar archivo de entrada")
    if input_file is not None:

        lines = input_file.readlines()

        # print(file_name)
        startingState=[]
        map = []
        # print(len(lines))
        # print(len(lines[8]))
        for i in range(len(lines),0,-1):
            if(len(lines[i-1]) == 4):
                state = lines[i-1].decode('utf-8').strip()
                state_arr = state.split(',')
                array_states = [int(x) for x in state_arr]
                startingState.append(array_states)
            elif(len(lines[i-1])>1):
                tile = lines[i-1].decode('utf-8').strip()
                #tile_arr = tile.split(',')
                array_tiles = []
                for char in tile:
                    array_tiles.append(char)
                map.append(array_tiles)

        startingState = list(reversed(startingState))
        gameMap = list(reversed(map))

        st.write(f"Estado inicial de los elementos del nivel: {startingState}")
        st.write(f"Mapa: {map}")

        resolver_nivel = st.button("Resolver nivel")
        
        if(resolver_nivel):
            st.write(f"Ruta Busqueda por Amplitud: "+"\n"+ solve_game_BFS(startingState, gameMap))
            st.write(f"Ruta Busqueda por Profundidad: " +solve_game_DFS(startingState, gameMap))
            st.write(f"Ruta Busqueda por Profundidad Iterativa: " +solve_game_BFSI(gameMap,startingState))

if __name__ == "__main__":
    main()