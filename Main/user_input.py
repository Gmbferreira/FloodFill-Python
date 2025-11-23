def get_user_grid():
    """
    Lê o grid e as coordenadas iniciais fornecidas pelo usuário.
    
    Returns:
        tuple: Uma tupla contendo (user_grid, start_coords).
    """
    print("\n--- Inserir Nova Matriz ---")
    
    while True:
        try:
            print("Insira o número de linhas (N) e colunas (M), separados por espaço (Ex: 4 5):")
            input_line = input()
            if not input_line.strip():
                print("Entrada não pode ser vazia.")
                continue
                
            n, m = map(int, input_line.split())
            if n <= 0 or m <= 0:
                print("As dimensões devem ser números inteiros positivos.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Use apenas números inteiros e um espaço.")
        except EOFError:
            
            print("Erro de leitura de entrada.")
            return [], (0, 0)
    user_grid = []
    print("\nInsira cada linha do grid, separando os valores (0 ou 1) por espaço:")
    for i in range(n):
        while True:
            try:
                row_str = input(f"Linha {i} ({m} valores): ").split()
                if len(row_str) != m:
                    print(f"Você deve inserir exatamente {m} valores.")
                    continue
                row = [int(x) for x in row_str]
                if not all(x in [0, 1] for x in row):
                    print("A matriz deve conter apenas os valores 0 (navegável) ou 1 (obstáculo).")
                    continue
                user_grid.append(row)
                break
            except ValueError:
                print("Entrada inválida. Use apenas 0s e 1s separados por espaço.")
            except EOFError:
                return [], (0, 0)
    while True:
        try:
            print(f"\nInsira as Coordenadas Iniciais (Linha, Coluna), separadas por espaço (Ex: 0 0). Linha de 0 a {n-1}, Coluna de 0 a {m-1}:")
            input_line = input()
            if not input_line.strip():
                print("Entrada não pode ser vazia.")
                continue
                
            start_r, start_c = map(int, input_line.split())
            if not (0 <= start_r < n and 0 <= start_c < m):
                 print(f"Coordenadas fora do limite. A Linha deve ser de 0 a {n-1} e a Coluna de 0 a {m-1}.")
                 continue
            break
        except ValueError:
            print("Entrada inválida. Use apenas números inteiros e um espaço.")
        except EOFError:
            return user_grid, (0, 0)
    
    return user_grid, (start_r, start_c)