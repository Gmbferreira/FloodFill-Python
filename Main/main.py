from FloodFill import FloodFiller
from user_input import get_user_grid 

def print_grid(grid, title):
    """Função auxiliar para imprimir o grid formatado."""
    print(f"\n{title}:")
    for row in grid:
        print(' '.join(map(str, row)))

def run_example(example_name, initial_grid_data, start_coords, expected_output=None):
    """Executa um caso de teste e imprime os resultados."""
    print(f"\n==========================================")
    print(f"### {example_name} ###")
    grid_copy = [row[:] for row in initial_grid_data]

    print_grid(initial_grid_data, "Entrada: Grid inicial")
    print(f"Coordenadas iniciais (Linha, Coluna): {start_coords}")
    start_r, start_c = start_coords
    rows = len(grid_copy)
    cols = len(grid_copy[0])
    
    if not (0 <= start_r < rows and 0 <= start_c < cols and grid_copy[start_r][start_c] == 0):
        print("\n A célula inicial não é navegável (0) ou está fora dos limites. O mapeamento começará automaticamente no próximo 0 encontrado.")
    filler = FloodFiller(grid_copy)
    final_grid = filler.map_all_regions(initial_start_coords=start_coords)

    print_grid(final_grid, "Saída: Grid preenchido")
    
    if expected_output:
        print("\nSaída Esperada (Para referência, a ordem das cores pode variar):")
        for row in expected_output:
            print(' '.join(map(str, row)))
            
    print("==========================================")

def run_standard_tests():
    """Define e executa todos os exemplos fixos."""
    
    # Exemplo 1
    grid_ex1 = [
        [0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 1, 1, 1],
        [1, 1, 0, 0, 0]
    ]
    start_coords_ex1 = (0, 0)
    expected_ex1 = [
        [2, 2, 1, 3, 3],
        [2, 1, 1, 3, 3],
        [2, 2, 1, 1, 1],
        [1, 1, 4, 4, 4]
    ]
    run_example("Exemplo 1: Simples (Imagens)", grid_ex1, start_coords_ex1, expected_ex1)

    # Exemplo 2
    grid_ex2 = [
        [0, 1, 0, 0, 1],
        [0, 1, 0, 0, 1],
        [0, 1, 1, 1, 1],
        [0, 0, 1, 0, 0]
    ]
    start_coords_ex2 = (0, 2)
    expected_ex2 = [
        [3, 1, 2, 2, 1],
        [3, 1, 2, 2, 1],
        [3, 1, 1, 1, 1],
        [3, 3, 1, 4, 4]
    ]
    run_example("Exemplo 2: Início Deslocado (Imagens)", grid_ex2, start_coords_ex2, expected_ex2)

    # Exemplo 3
    grid_ex3 = [
        [0, 0 ,1, 1, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 0],
        [0, 0, 1, 0, 1, 1],
        [0, 1, 1, 0, 1, 1],
        [0, 0, 0, 1, 1, 0]
    ]
    start_coords_ex3 = (0, 0)
    expected_ex3 = [
        [2, 2, 1, 1, 3, 3],
        [2, 1, 1, 1, 1, 3],
        [1, 1, 1, 1, 1, 3],
        [4, 4, 1, 5, 1, 1],
        [4, 1, 1, 5, 1, 1],
        [4, 4, 4, 1, 1, 6]
    ]
    run_example("Exemplo 3: Problemático (Múltiplas Regiões Isoladas)", grid_ex3, start_coords_ex3, expected_ex3)

# ------------------------------------------------------------------------------
# Função Principal (Main)
# ------------------------------------------------------------------------------

def main():
    """Gerencia a escolha do usuário e executa a operação."""
    while True:
        print("\n##########################################")
        print("### Algoritmo Flood Fill (Mapeamento) ###")
        print("##########################################")
        print("\nEscolha uma opção:")
        print("1. Rodar Testes Padrões (Exemplos Fixos)")
        print("2. Inserir uma Matriz Nova")
        print("3. Sair")
        
        choice = input("Digite 1, 2 ou 3: ")

        if choice == '1':
            run_standard_tests()
        elif choice == '2':
            try:
                grid, coords = get_user_grid()
                if grid: 
                    run_example("Teste Personalizado do Usuário", grid, coords)
            except Exception as e:
                print(f"\n Ocorreu um erro inesperado durante a execução do teste: {e}")
        elif choice == '3':
            print("\nEncerrando o programa. Até mais!")
            break
        else:
            print("\nOpção inválida. Por favor, digite 1, 2 ou 3.")

if __name__ == "__main__":
    main()