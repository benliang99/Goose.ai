/*
 * Globals
 */
let colorChoices = [
  "aliceblue",
  "azure",
  "blueviolet",
  "cadetblue",
  "coral",
  "cornsilk",
  "darkmagenta",
  "darksalmon",
  "darkslateblue",
  "darkslategrey",
  "deepskyblue",
  "floralwhite",
  "gold",
  "honeydew",
  "hotpink",
  "lavendarblush",
  "lightblue",
  "lightgrey",
  "lightsteelblue",
  "mediumpurple",
  "mistyrose",
  "navy",
  "olivedrab",
  "palevioletred",
  "royalblue",
  "seagreen",
  "seashell",
  "thistle",
];
let backgroundColor, color1, color2, color3, color4;
let plexMono;

/*
 * Preload
 * Load any assets we need for the sketch
 */
function preload() {
  plexMono = loadFont("fonts/IBMPlexMono-Regular.ttf");
}

/*
 * Setup
 */
function setup() {
  createCanvas(windowWidth, windowHeight);
  colorMode(HSB, 360, 100, 100, 1);
  noLoop();
  frameRate(60);
  pixelDensity(2);

  // Choose colors
  backgroundColor = hl.randomElement(colorChoices);
  color1 = hl.randomElement(colorChoices);
  color2 = hl.randomElement(colorChoices);
  color3 = hl.randomElement(colorChoices);
  color4 = hl.randomElement(colorChoices);

  // Set attributes
  hl.token.setAttributes({
    "Background Color": backgroundColor,
    "Color 1": color1,
    "Color 2": color2,
    "Color 3": color3,
    "Color 4": color4,
  });
}

let img;

function preload() {
  img = loadImage('goose.png'); // Replace 'path/to/your/image.jpg' with the actual path to your image
}

/*
 * Draw
 */
function draw() {
  noStroke();
  background(backgroundColor);
  translate(width / 2, height / 2);
  fill(color1);
  ellipse(0, 0, width * 0.8, width * 0.8);
  fill(color2);
  ellipse(0, 0, width * 0.6, width * 0.6);
  fill(color3);
  ellipse(0, 0, width * 0.4, width * 0.4);
  fill(color4);
  ellipse(0, 0, width * 0.2, width * 0.2);
  image(img, -img.width / 2, -img.height / 2); // Display the image at the center of the sketch

  hl.token.capturePreview();
}

/*
 * Window resize
 */
function windowResized() {
  resizeCanvas(windowWidth, windowHeight);
}

/*
 * Keyboard shortcuts for saving, redrawing, etc.
 */
function keyTyped() {
  switch (key) {
    case "s":
      saveCanvas();
      break;
    case "r":
      redraw();
      break;
  }
}
