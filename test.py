def parse_map(map_str):
    """Parse the map string into a 2D grid."""
    return [list(row) for row in map_str.strip().split('\n')]

def find_guard_start(grid):
    """Find the starting position and direction of the guard."""
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell in '^v<>':
                return x, y, cell
    return None

def get_next_direction(current_dir):
    """Rotate right 90 degrees."""
    rotation = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    return rotation[current_dir]

def is_valid_move(grid, x, y):
    """Check if the position is within grid and not an obstacle."""
    return (0 <= y < len(grid) and 
            0 <= x < len(grid[0]) and 
            grid[y][x] != '#')

def simulate_guard_patrol(grid, max_iterations=1000):
    """Simulate the guard's patrol and track visited positions."""
    # Find start position
    start_x, start_y, start_dir = find_guard_start(grid)
    
    # Create a copy of the grid to modify
    working_grid = [row.copy() for row in grid]
    
    # Reset start position to its direction marker
    working_grid[start_y][start_x] = start_dir
    
    visited = set([(start_x, start_y)])
    x, y = start_x, start_y
    direction = start_dir
    iterations = 0
    
    while iterations < max_iterations:
        # Determine next position based on current direction
        next_x, next_y = x, y
        if direction == '^': next_y -= 1
        elif direction == 'v': next_y += 1
        elif direction == '<': next_x -= 1
        elif direction == '>': next_x += 1
        
        # If next position is invalid, turn right
        if not is_valid_move(working_grid, next_x, next_y):
            direction = get_next_direction(direction)
            iterations += 1
            continue
        
        # Move to next position
        x, y = next_x, next_y
        visited.add((x, y))
        
        # Update grid to show current direction
        working_grid[y][x] = direction
        
        # Check if guard has left the mapped area
        if (x == 0 or x == len(working_grid[0])-1 or 
            y == 0 or y == len(working_grid)-1):
            break
        
        iterations += 1
    
    return visited

def find_loop_obstruction_positions(grid):
    """Find positions where a new obstruction would trap the guard."""
    # Original patrol path
    original_path = simulate_guard_patrol(grid)
    
    loop_positions = set()
    
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            # Skip starting position and existing obstacles
            if grid[y][x] == '#' or (x, y) == find_guard_start(grid)[:2]:
                continue
            
            # Create a temporary grid with new obstacle
            temp_grid = [row.copy() for row in grid]
            temp_grid[y][x] = '#'
            
            # Simulate patrol with new obstacle
            try:
                patrol_path = simulate_guard_patrol(temp_grid)
                
                # If patrol doesn't leave the grid and visits same number of positions, it's a loop
                if len(patrol_path) == len(original_path):
                    loop_positions.add((x, y))
            except Exception:
                continue
    
    return loop_positions

def solve_part_two(map_str):
    """Solve Part 2 by finding number of possible loop obstruction positions."""
    grid = parse_map(map_str)
    loop_positions = find_loop_obstruction_positions(grid)
    return len(loop_positions)

# If this script is run directly, allow input from file or direct paste
if __name__ == "__main__":
    import sys
    
    # Check if a file is provided as an argument
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as file:
            puzzle_input = file.read()
    else:
        # If no file, prompt for input
        print("Paste your puzzle input (press Ctrl+D or Ctrl+Z when done):")
        puzzle_input = sys.stdin.read()
    
    # Solve and print the result
    result = solve_part_two(puzzle_input)
    print(f"Number of possible obstruction positions: {result}")