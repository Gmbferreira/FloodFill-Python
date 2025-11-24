import tkinter as tk
from Main.FloodFill import FloodFiller
from Main.user_input import get_user_grid

# Tamanho de cada quadradinho (em pixels)
CELL_SIZE = 40

# Mapeamento de valores do grid para cores
COLOR_MAP = {
    0: "#FFFFFF",  # Branco - terreno navegável
    1: "#000000",  # Preto  - obstáculo
    2: "#FF0000",  # Vermelho
    3: "#FFA500",  # Laranja
    4: "#FFFF00",  # Amarelo
}

DEFAULT_REGION_COLOR = "#00BFFF"  # Cor padrão para valores >= 5


class FloodFill_InterfaceGrafica:
    def __init__(self, root, grid):
        self.root = root
        self.root.title("Flood Fill - Interface Gráfica")

        # Guarda a matriz original e uma cópia que será modificada
        self.original_grid = [row[:] for row in grid]
        self.grid = [row[:] for row in grid]

        self.rows = len(self.grid)
        self.cols = len(self.grid[0]) if self.rows > 0 else 0

        # Canvas onde vamos desenhar os quadradinhos
        width = self.cols * CELL_SIZE
        height = self.rows * CELL_SIZE
        self.canvas = tk.Canvas(self.root, width=width, height=height)
        self.canvas.pack(padx=10, pady=10)

        # Label de informações
        self.info_label = tk.Label(
            self.root,
            text="Clique em uma célula branca (0) para iniciar o preenchimento."
        )
        self.info_label.pack(pady=5)

        # Botão de reset
        self.reset_button = tk.Button(
            self.root,
            text="Resetar grid",
            command=self.reset_grid
        )
        self.reset_button.pack(pady=5)

        # Associa clique do mouse ao handler
        self.canvas.bind("<Button-1>", self.on_canvas_click)

        # Desenha a matriz inicial
        self.draw_grid()

    def reset_grid(self):
        """Volta o grid ao estado original e redesenha."""
        self.grid = [row[:] for row in self.original_grid]
        self.info_label.config(
            text="Clique em uma célula branca (0) para iniciar o preenchimento."
        )
        self.draw_grid()

    def draw_grid(self):
        """Desenha o grid atual no canvas."""
        self.canvas.delete("all")

        for r in range(self.rows):
            for c in range(self.cols):
                x1 = c * CELL_SIZE
                y1 = r * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE

                value = self.grid[r][c]
                color = COLOR_MAP.get(value, DEFAULT_REGION_COLOR)

                self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=color,
                    outline="#CCCCCC"
                )

    def on_canvas_click(self, event):
        """Handler para clique do mouse: roda o Flood Fill a partir da célula clicada."""
        col = event.x // CELL_SIZE
        row = event.y // CELL_SIZE

        # Verifica se está dentro do grid
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            return

        # Só deixa iniciar em célula navegável (0)
        if self.original_grid[row][col] != 0:
            self.info_label.config(
                text=f"Célula ({row}, {col}) não é navegável (0). Escolha outra célula branca."
            )
            return

        # Sempre começamos de uma cópia do grid original
        grid_copy = [r[:] for r in self.original_grid]

        # Usa a classe que vocês já fizeram
        filler = FloodFiller(grid_copy)
        filler.map_all_regions(initial_start_coords=(row, col))

        # Atualiza o grid atual e redesenha
        self.grid = filler.grid
        self.draw_grid()
        self.info_label.config(
            text=f"Preenchimento iniciado em ({row}, {col})."
        )


def main():
    
    grid, coords = get_user_grid()

    root = tk.Tk()
    app = FloodFill_InterfaceGrafica(root, grid)
    root.mainloop()


if __name__ == "__main__":
    main()
