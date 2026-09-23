# 🎮 Pac-Man BFS Agent

A Python-based Pac-Man agent that uses **Breadth-First Search (BFS)** to find the shortest path to the food in a grid-based environment. Developed as a university Artificial Intelligence course project.

---

## ✨ Features

- 🧠 **BFS Pathfinding** — Finds the shortest path to the food
- 🗺️ **Grid-based Environment** — Reads the map from a text file
- 🎲 **Random Map Generator** — Can generate random maps with walls and food
- 🚧 **Obstacle Avoidance** — Walls (`*`) are detected and avoided
- 📍 **Path Tracking** — Records the full path with directions (U, R, D, L)
- 📊 **Game History** — Keeps track of all visited cells

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Libraries:**
  - `random` — for random map generation
  - `queue` — for the frontier data structure
- **Concepts:** BFS, Search Algorithms, State Space, Agent-Environment Model

---

## 📂 Project Structure

- `pacman.py` — Main program (agent, environment, BFS logic)
- `input1.txt` — Input map file
- `README.md` — Project documentation

---

## 🧩 Core Components

| Component | Responsibility |
|-----------|----------------|
| `Node` | Represents a node in the search tree (state, parent, action) |
| `QueueFrontier` | FIFO queue used by BFS to manage the frontier |
| `game_agent()` | Main agent that performs BFS to find the food |
| `environment_action()` | Simulates the environment's response to an action |
| `read_file()` | Loads the map and agent position from a text file |
| `set_random()` | Generates a random map with walls, food, and agent |
| `food_path()` | Reconstructs the path from the goal node back to the start |

---

## 🗺️ Map Symbols

| Symbol | Meaning |
|--------|---------|
| `a` | Agent (Pac-Man) |
| `f` | Food |
| `*` | Wall |
| `-` | Empty space |
| `?` | Unknown (not yet visited) |

---

## 🚀 How to Run

### 1. Clone the repository:
```bash
git clone https://github.com/FatemehPaksima/Pacman-BFS-Search.git
```

### 2. Navigate into the folder:
```bash
cd Pacman-BFS-Search
```

### 3. Run the program:
```bash
python pacman.py
```

> ⚠️ Make sure `input1.txt` is in the same directory as the Python file.

---

## 📄 Input File Format

The `input1.txt` file should contain:

```
<rows>,<cols>
<agent_row>,<agent_col>

<map lines...>
```

Example:
```
5,5
1,1

*****
*a--*
*---*
*-f-*
*****
```

---

## 📊 Sample Output

```
(1, 1)
(3, 3)
6
[(1, 1), 2, (1, 2), 2, (1, 3), 3, (2, 3), 3, (3, 3)]
[['-', '?', '?', '?', '?'],
 ['?', '-', '-', '-', '?'],
 ['?', '?', '?', '-', '?'],
 ['?', '?', '?', 'f', '?'],
 ['?', '?', '?', '?', '?']]
```

- **Start position** — Agent's initial coordinates
- **Goal position** — Food coordinates
- **Path length** — Number of steps
- **Path** — List of positions and directions (1=U, 2=R, 3=D, 4=L)
- **Game history** — Grid of visited cells

---

## 🧠 How BFS Works Here

1. Start from the agent's position
2. Add all valid neighboring states to the frontier
3. Explore states in **FIFO order** (Breadth-First)
4. Stop when the food (`f`) is found
5. Reconstruct the path from the goal back to the start

BFS guarantees the **shortest path** in terms of number of steps.

---

## 📜 License

This project was developed as part of a university Artificial Intelligence course.  
Free to use for learning purposes.

---

## 👨‍💻 Author

**Fatemeh Paksima**
GitHub: [@FatemehPaksima](https://github.com/FatemehPaksima)
