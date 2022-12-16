let minx = 500;
let miny = 0;
let maxx = 0;
let maxy = 0;

let width, height;
let board = [];

let grain = [500, 0];
let done = false;

function makeboard() {
  for (let i = 0; i < width * height; i++) {
    board.push(" ");
  }
  return board;
}

function boardSetValue(x, y, v) {
  if (x < minx || x > maxx || y < miny || y > maxy) {
    console.error("Bad value: ", x, y, minx, maxx, miny, maxy);
  }
  x -= minx;
  y -= miny;
  let idx = y * width + x;
  board[idx] = v;
}

function boardGetValue(x, y) {
  x -= minx;
  y -= miny;
  let idx = y * width + x;
  return board[idx];
}

function boardLine(x1, y1, x2, y2) {
  if (x1 == x2) {
    for (let y = y1; y <= y2; y++) {
      boardSetValue(x1, y, "#");
    }
  } else if (y1 == y2) {
    for (let x = min(x1, x2); x <= max(x1, x2); x++) {
      boardSetValue(x, y1, "#");
    }
  } else {
    console.error("non-straight lines not allowed");
  }
}

function setup() {
  let features = data;
  features.forEach((feature) => {
    coordinates = feature.split("->");
    coordinates.forEach((coordinate) => {
      let [x, y] = coordinate.split(",");
      x = int(x);
      y = int(y);
      if (x > 600 || y > 600) {
        console.log(coordinates, coordinate, x, y);
      }
      minx = Math.min(minx, x);
      miny = Math.min(miny, y);
      maxx = Math.max(maxx, x);
      maxy = Math.max(maxy, y);
    });
  });

  minx -= 5;
  maxx += 5;
  maxy += 5;

  console.log(minx, miny, maxx, maxy);

  width = maxx - minx + 1;
  height = maxy - miny + 1;
  board = makeboard();

  features.forEach((feature) => {
    let prevx = undefined;
    let prevy = undefined;
    coordinates = feature.split("->");
    coordinates.forEach((coordinate) => {
      let [x, y] = coordinate.split(",");
      x = int(x);
      y = int(y);
      if (prevx && prevy) {
        boardLine(prevx, prevy, x, y);
      }
      prevx = x;
      prevy = y;
    });
  });
  console.log(minx, miny, maxx, maxy);

  createCanvas(1024, 1024);
}

let grainCount = 0;
function processGrain() {
  if (done) {
    return;
  }
  grain = [500, 0];
  path = [];
  do {
    if (boardGetValue(grain[0], grain[1] + 1) === " ") {
      grain[1] += 1;
    } else if (boardGetValue(grain[0] - 1, grain[1] + 1) === " ") {
      grain[0] -= 1;
      grain[1] += 1;
    } else if (boardGetValue(grain[0] + 1, grain[1] + 1) === " ") {
      grain[0] += 1;
      grain[1] += 1;
    } else {
      boardSetValue(grain[0], grain[1], grainCount);
      grainCount += 1;
      break;
    }
    path.push([grain[0], grain[1]]);
    if (grain[1] >= maxy) {
      console.log("Exceeded: ", grain, minx, maxx, miny, maxy);
      done = true;
      noLoop();
      let rs = 1024 / max(width, height);
      path.forEach((g) => {
        fill("red");
        rect((g[0] - minx) * rs, (g[1] - miny) * rs, rs - 2, rs - 2);
      });
      console.log("Grains dropped: ", grainCount);
      break;
    }
  } while (true);
}

function keyPressed() {
  if (keyCode === LEFT_ARROW) loop();
}

function draw() {
  background(220);
  let rs = 1024 / max(width, height);
  for (let x = 0; x < width; x++) {
    for (let y = 0; y < height; y++) {
      let v = boardGetValue(x + minx, y + miny);
      if (v === "#") {
        fill("black");
      } else if (v === " ") {
        continue;
      } else {
        fill(v % 256, v / 256, 255);
      }
      rect(x * rs, y * rs, rs - 2, rs - 2);
    }
  }

  fill("green");
  rect((grain[0] - minx) * rs, (grain[1] - miny) * rs, rs - 2, rs - 2);
  processGrain();
}
