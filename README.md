# AI-Snake-Game
🐍 AI Snake Game using Deep Q-Learning (DQN) — built with Python, PyTorch, and Pygame. The AI learns to play the classic snake game through reinforcement learning.
🎯 Objective:

The objective of this project is to design and develop an AI-powered Snake Game that runs in a web browser and can automatically play using the Breadth-First Search (BFS) pathfinding algorithm.
The project demonstrates how search algorithms from Artificial Intelligence can be applied to real-time decision-making in games.

🧩 Project Overview:

Snake AI (Web) is an interactive web-based implementation of the classic Snake game enhanced with an AI autopilot system.
It uses BFS (Breadth-First Search) to calculate the shortest path between the snake’s head and the food, allowing it to navigate intelligently through the grid while avoiding collisions.

The application is built using Flask (Python) as a lightweight backend web server and HTML5 Canvas + JavaScript for rendering the game interface.

Users can toggle between manual and AI-controlled modes, visualize how the pathfinding algorithm works in real-time, and control the game speed and play state directly in the browser.

⚙️ Key Features:

🧭 BFS Pathfinding Algorithm: Finds the shortest path from snake head to food in real-time.

🕹️ Dual Play Modes:

Manual Mode: Controlled via arrow keys.

AI Mode: Automatically plays using BFS logic.

⏱️ Adjustable Speed: Slider to change the FPS (2–60).

🧱 Safe Tail Logic: The AI considers the tail as a safe path when planning its next move.

🌐 Web-Based Interface: Runs smoothly on any modern browser using Flask.

📱 Responsive Canvas: 640×480 grid with 20px cell size for clean visuals.

🧮 Algorithm Used:

Breadth-First Search (BFS):
BFS is a fundamental search algorithm that explores all possible paths level by level until the shortest path to the goal (food) is found.
In this game, BFS helps the AI find an optimal and collision-free path dynamically as the snake and food positions change.

🏗️ System Requirements:

Programming Language: Python 3.8+

Framework: Flask

Frontend: HTML, CSS, JavaScript (Canvas)

Libraries:

flask for backend

built-in Python modules (no heavy dependencies)

💻 Installation & Execution:
pip install flask
python app.py


Then open your browser and visit:
👉 http://127.0.0.1:5000/

🎮 Controls:
Control	Description
▶️ Start/Pause	Start or stop the game loop
⚡ Speed Slider	Adjust game FPS (2–60)
🤖 Pathfinding Toggle	Switch between manual and BFS autopilot
⬆️⬇️⬅️➡️ Arrow Keys	Control snake movement manually
🧠 Applications:

Demonstrates AI Search Algorithms (BFS) in a fun, visual context.

Useful for learning AI game agent logic, pathfinding, and Flask web deployment.

Can be extended to use A*, DFS, or Dijkstra’s algorithm for comparative study.

🚀 Future Enhancements:

Add A* and Greedy Best-First Search modes.

Implement score tracking and leaderboard system.

Include maze generation for complex environments.

Deploy on GitHub Pages + Flask API for public access.

🏁 Conclusion:

This mini project successfully combines Artificial Intelligence, Web Technologies, and Game Design to create a dynamic, browser-based application that visually demonstrates how pathfinding algorithms like BFS can make intelligent decisions in real-time gaming environments.
