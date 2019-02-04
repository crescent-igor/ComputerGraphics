

var butterfly = [];
function setup() {
  createCanvas(600, 600);
  for (let i = 0; i < 15; i++)
    butterfly[i] = new Butterfly(random(30, 250), round(random(50, 200)));
}

function draw() {
  background(50);
  for (let i = 0; i < 15; i++)
    butterfly[i].render();

}


var Butterfly = function (x, y) {
  this.posX = x;
  this.posY = y;
  this.initialPosX = x;
  this.initialPosY = y;
  this.z = 0;
  this.x = 0;
  this.phase = random(1, 100);
  this.colorBut = color(random(50, 200), random(50, 200), random(50, 200));

  this.render = function () {
    push();
    translate(this.posX, this.posY);
    fill(this.colorBut);
    noStroke();


    ellipse(this.posX, this.posY, 30 + this.z, 50);
    ellipse(this.posX + 20, this.posY, 30 + this.z, 50);
    this.updateZ();
    this.updatePos();
    pop();
  }

  this.updateZ = function () {
    this.z = sin(frameCount / 10) * 10;
  }

  this.updatePos = function () {
    this.posX = this.initialPosX + sin(frameCount / 40 + this.phase) * 50;
    this.posY = this.initialPosY + cos(frameCount / 30 + this.phase) * 40;
  }

}

