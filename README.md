🐍 Snake AI (Web)

A browser-based AI Snake Game built using Flask and BFS (Breadth-First Search) algorithm for intelligent pathfinding.
The system automatically navigates the snake towards food while avoiding collisions, demonstrating AI pathfinding techniques in a dynamic environment.

🧠 Project Overview

This mini-project showcases AI pathfinding in real time, where the Snake autonomously finds the optimal route to reach food using the BFS (Breadth-First Search) algorithm.

The user can toggle between manual control and AI autopilot, adjust the game speed, and visualize how BFS explores possible paths.

This project also serves as a great example of AI in games, integrating Flask for web serving and JavaScript Canvas for real-time rendering.

⚙️ Requirements

Python 3.8+

pip

Install dependencies:

pip install flask

▶️ How to Run

Clone or download this repository

Navigate to the project folder

Run the following command:

python app.py


Open your browser and go to:
👉 http://127.0.0.1:5000/

🎮 Game Controls
Action	Description
▶️ Start / Pause	Control the main game loop
⚡ Speed Slider	Adjust FPS (2–60)
🤖 Pathfinding Toggle	Switch between BFS Autopilot and Manual Control
⬆️⬇️⬅️➡️ Arrow Keys	Control snake manually when AI is off
🧩 Technical Details

Algorithm: Breadth-First Search (BFS)

Grid Cell Size: 20px

Canvas Resolution: 640 × 480

Pathfinding Logic:

The snake uses BFS to find the shortest path to the nearest food.

The snake’s tail is treated as a temporary safe space, since it moves unless the food is eaten.

BFS ensures the snake takes the shortest collision-free route.

💡 Features

✅ Interactive Web Interface (HTML + JS + Flask)
✅ BFS Algorithm Visualization
✅ Autopilot (AI Mode) + Manual Mode
✅ Adjustable Game Speed
✅ Simple and Clean UI
✅ Educational AI demonstration

📘 Learning Outcomes

Implemented AI pathfinding in a real-time environment

Learned Flask web serving with client-side game logic

Understood how BFS explores and finds shortest paths

Practiced integrating Python backend with JavaScript frontend

👨‍💻 Developer Credit

Project By:
🧑‍💻 Devaprakash J
📘 Register No: 2117240030025
🏫 Department: CSE (AI & ML) - A
📅 Semester: III (3rd Semester)
🏛️ RIT College

🏁 Conclusion

This Snake AI (Web) project demonstrates how classical search algorithms like BFS can be applied in game environments to create intelligent autonomous agents. It’s a fun and interactive way to understand the fundamentals of AI pathfinding and game-based problem-solving.
