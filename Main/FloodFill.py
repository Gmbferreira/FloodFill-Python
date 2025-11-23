class FloodFiller:
    """
    Implementa o algoritmo Flood Fill para mapear e colorir regiões
    navegáveis (valor 0) em um grid bidimensional, respeitando obstáculos (valor 1).
    As cores são representadas por inteiros começando de 2 em diante.
    """

    def __init__(self, grid):
        """
        Inicializa o FloodFiller com o grid.
        
        Args:
            grid (list[list[int]]): O grid 2D a ser processado.
        """
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def _is_valid(self, r, c, target_value):
        """
        Verifica se as coordenadas (r, c) estão dentro dos limites do grid
        e se o valor da célula é igual ao valor alvo (terreno navegável não preenchido).
        
        Args:
            r (int): Índice da linha.
            c (int): Índice da coluna.
            target_value (int): O valor que a célula deve ter para ser preenchida (sempre 0).
            
        Returns:
            bool: True se a célula for válida para preenchimento, False caso contrário.
        """
        return (0 <= r < self.rows and 
                0 <= c < self.cols and 
                self.grid[r][c] == target_value)

    def flood_fill(self, start_r, start_c, new_color):
        """
        Executa o algoritmo Flood Fill a partir de uma célula inicial,
        preenchendo a região conectada com a nova cor.
        
        Args:
            start_r (int): Linha inicial.
            start_c (int): Coluna inicial.
            new_color (int): O novo valor de cor para o preenchimento (2, 3, 4, ...).
        
        Returns:
            bool: True se uma região foi preenchida, False caso contrário.
        """
        if not self._is_valid(start_r, start_c, 0):
            return False
        queue = [(start_r, start_c)]
        target_value = 0
        self.grid[start_r][start_c] = new_color
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            r, c = queue.pop(0) 
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if self._is_valid(nr, nc, target_value):
                    self.grid[nr][nc] = new_color
                    queue.append((nr, nc))
        
        return True

    def map_all_regions(self, initial_start_coords=None):
        """
        Mapeia e colore todas as regiões navegáveis (0) do grid.
        
        Args:
            initial_start_coords (tuple[int, int], optional): Coordenadas (r, c)
                para iniciar o primeiro preenchimento, se fornecidas.
        
        Returns:
            list[list[int]]: O grid preenchido final.
        """
        current_color = 2
        if initial_start_coords:
            start_r, start_c = initial_start_coords
            if self.flood_fill(start_r, start_c, current_color):
                current_color += 1
        
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == 0:
                    if self.flood_fill(r, c, current_color):
                        current_color += 1
                        
        return self.grid