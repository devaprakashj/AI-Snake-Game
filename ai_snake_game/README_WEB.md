Snake AI (Web)

A browser-based Snake game with BFS pathfinding, served via a minimal Flask app.

Requirements
- Python 3.8+
- pip

Install
```bash
pip install flask
```

Run
```bash
python app.py
```
Then open `http://127.0.0.1:5000/` in your browser.

Controls
- Start/Pause buttons control the loop
- Speed controls FPS (2–60)
- Pathfinding toggle switches between BFS autopilot and manual
- Arrow keys to control the snake when Pathfinding is off

Notes
- Grid cell size is 20px on a 640x480 canvas
- BFS treats the snake tail as safe for the next move (tail moves unless food is eaten)

