import json
import random

# Copia aquí el JSON que me proporcionaste anteriormente
# Se espera que el archivo 'data.json' tenga la estructura: {"ground": [...], "wall": [...], "nature": [...]}

def load_data(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def generate_random_map(width, height, catalog):
    """
    Crea un mapa 2D sencillo llenando el piso y añadiendo bordes de pared.
    """
    map_grid = []
    
    # Seleccionar un piso base y una pared base de tu catálogo
    ground_base = random.choice(catalog['ground'])
    wall_base = random.choice(catalog['wall'])
    
    for y in range(height):
        row = []
        for x in range(width):
            # Lógica básica: Bordes son paredes, centro es piso
            if x == 0 or x == width - 1 or y == 0 or y == height - 1:
                row.append({"type": "wall", "id": wall_base['id'], "name": wall_base['name']})
            else:
                row.append({"type": "ground", "id": ground_base['id'], "name": ground_base['name']})
        map_grid.append(row)
    
    return map_grid

def add_nature(map_grid, catalog, density=0.05):
    """
    Añade elementos de naturaleza aleatorios en el mapa.
    """
    height = len(map_grid)
    width = len(map_grid[0])
    
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            if random.random() < density:
                nature_item = random.choice(catalog['nature'])
                map_grid[y][x] = {"type": "nature", "id": nature_item['id'], "name": nature_item['name']}
    return map_grid

def save_map(map_grid, output_filename):
    with open(output_filename, 'w') as f:
        json.dump(map_grid, f, indent=4)
    print(f"Mapa generado exitosamente en {output_filename}")

if __name__ == "__main__":
    # 1. Asegúrate de tener tu data en 'items.json'
    try:
        catalog = load_data('items.json')
        
        # 2. Generar mapa de 20x20
        print("Generando mapa...")
        my_map = generate_random_map(20, 20, catalog)
        my_map = add_nature(my_map, catalog, density=0.1)
        
        # 3. Guardar
        save_map(my_map, 'generated_map.json')
        
    except FileNotFoundError:
        print("Error: No se encontró 'items.json'. Asegúrate de guardarlo en la misma carpeta.")