class SnakeGame {
  constructor(canvasId) {
    this.cell = 20;
    this.canvas = document.getElementById(canvasId);
    this.ctx = this.canvas.getContext('2d');
    this.cols = this.canvas.width / this.cell;
    this.rows = this.canvas.height / this.cell;

    this.clockWise = [ [1,0], [0,1], [-1,0], [0,-1] ]; // scaled later by cell
    this.reset();
    this.fps = 12;
    this.timer = null;
    this.auto = true;

    window.addEventListener('keydown', (e) => this.onKey(e));
    this.draw();
  }

  reset() {
    this.dir = [1, 0];
    this.snake = [ [5,5], [4,5], [3,5] ];
    this.placeFood();
    this.score = 0;
    this.frameIter = 0;
    this.updateScore();
  }

  setFps(fps) { this.fps = Math.max(2, Math.min(60, fps)); if (this.timer) { this.start(this.fps); } }
  setAuto(v) { this.auto = v; }

  start(fps) {
    this.setFps(fps || this.fps);
    this.pause();
    this.timer = setInterval(() => this.step(), Math.floor(1000 / this.fps));
  }

  pause() { if (this.timer) { clearInterval(this.timer); this.timer = null; } }

  placeFood() {
    while (true) {
      const x = Math.floor(Math.random() * this.cols);
      const y = Math.floor(Math.random() * this.rows);
      if (!this.snake.some(p => p[0] === x && p[1] === y)) {
        this.food = [x, y];
        break;
      }
    }
  }

  onKey(e) {
    const map = { ArrowUp:[0,-1], ArrowDown:[0,1], ArrowLeft:[-1,0], ArrowRight:[1,0] };
    if (!this.auto && map[e.key]) {
      const nd = map[e.key];
      // prevent 180 turns
      if (nd[0] === -this.dir[0] && nd[1] === -this.dir[1]) return;
      this.dir = nd;
    }
  }

  step() {
    this.frameIter++;
    if (this.auto) {
      const action = this.getAutoAction();
      this.applyAction(action);
    }

    const head = this.snake[0];
    const nx = head[0] + this.dir[0];
    const ny = head[1] + this.dir[1];
    const newHead = [nx, ny];

    if (this.isCollision(newHead)) {
      this.reset();
      this.draw();
      return;
    }

    this.snake.unshift(newHead);
    if (newHead[0] === this.food[0] && newHead[1] === this.food[1]) {
      this.score += 1;
      this.updateScore();
      this.placeFood();
    } else {
      this.snake.pop();
    }

    this.draw();
  }

  applyAction(action) {
    // action: [straight, right, left]
    const idx = this.clockWise.findIndex(d => d[0] === this.dir[0] && d[1] === this.dir[1]);
    if (action[0] === 1) {
      // straight
      this.dir = this.clockWise[idx];
    } else if (action[1] === 1) {
      this.dir = this.clockWise[(idx + 1) % 4];
    } else {
      this.dir = this.clockWise[(idx + 3) % 4];
    }
  }

  isCollision(pt) {
    if (pt[0] < 0 || pt[0] >= this.cols || pt[1] < 0 || pt[1] >= this.rows) return true;
    // body check
    for (let i = 1; i < this.snake.length; i++) {
      if (this.snake[i][0] === pt[0] && this.snake[i][1] === pt[1]) return true;
    }
    return false;
  }

  getAutoAction() {
    // BFS to food; avoid body except tail
    const start = this.snake[0];
    const goal = this.food;
    const occupied = new Set(this.snake.slice(0, this.snake.length - 1).map(p => `${p[0]},${p[1]}`));

    const q = [start];
    const came = new Map();
    const seen = new Set([`${start[0]},${start[1]}`]);

    const neigh = (c) => [[c[0]+1,c[1]],[c[0]-1,c[1]],[c[0],c[1]+1],[c[0],c[1]-1]];
    const inb = (c) => c[0] >= 0 && c[0] < this.cols && c[1] >= 0 && c[1] < this.rows;

    let found = false;
    while (q.length) {
      const cur = q.shift();
      if (cur[0] === goal[0] && cur[1] === goal[1]) { found = true; break; }
      for (const n of neigh(cur)) {
        const k = `${n[0]},${n[1]}`;
        if (!inb(n)) continue;
        if (seen.has(k)) continue;
        if (occupied.has(k) && !(n[0] === goal[0] && n[1] === goal[1])) continue;
        seen.add(k);
        came.set(k, cur);
        q.push(n);
      }
    }

    if (found) {
      // reconstruct
      let cur = goal;
      const startKey = `${start[0]},${start[1]}`;
      const path = [];
      while (`${cur[0]},${cur[1]}` !== startKey) {
        path.push(cur);
        const prev = came.get(`${cur[0]},${cur[1]}`);
        if (!prev) break;
        cur = prev;
      }
      path.reverse();
      if (path.length > 0) {
        const nxt = path[0];
        return this.actionFromNextPoint(start, nxt);
      }
    }

    // fallback: straight, right, left
    const candidates = [[1,0,0],[0,1,0],[0,0,1]];
    for (const a of candidates) {
      const idx = this.clockWise.findIndex(d => d[0] === this.dir[0] && d[1] === this.dir[1]);
      let nd;
      if (a[0] === 1) nd = this.clockWise[idx];
      else if (a[1] === 1) nd = this.clockWise[(idx + 1) % 4];
      else nd = this.clockWise[(idx + 3) % 4];
      const head = this.snake[0];
      const nxt = [head[0] + nd[0], head[1] + nd[1]];
      if (!this.isCollision(nxt)) return a;
    }
    return [1,0,0];
  }

  actionFromNextPoint(head, nextPt) {
    const desired = [nextPt[0] - head[0], nextPt[1] - head[1]];
    const idx = this.clockWise.findIndex(d => d[0] === this.dir[0] && d[1] === this.dir[1]);
    const didx = this.clockWise.findIndex(d => d[0] === desired[0] && d[1] === desired[1]);
    if (didx === idx) return [1,0,0];
    if (didx === (idx + 1) % 4) return [0,1,0];
    return [0,0,1];
  }

  draw() {
    const c = this.ctx;
    c.clearRect(0,0,this.canvas.width,this.canvas.height);
    // background
    c.fillStyle = '#0b0f18';
    c.fillRect(0,0,this.canvas.width,this.canvas.height);
    // snake
    for (let i = 0; i < this.snake.length; i++) {
      const [x,y] = this.snake[i];
      c.fillStyle = i === 0 ? '#34d399' : '#10b981';
      c.fillRect(x*this.cell, y*this.cell, this.cell, this.cell);
    }
    // food
    this.ctx.fillStyle = '#ef4444';
    this.ctx.fillRect(this.food[0]*this.cell, this.food[1]*this.cell, this.cell, this.cell);
  }

  updateScore() {
    const el = document.getElementById('score');
    if (el) el.textContent = String(this.score);
  }
}


