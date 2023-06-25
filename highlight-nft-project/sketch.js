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
let img;
let count;

/*
 * Preload
 * Load any assets we need for the sketch
 */
function preload() {
  plexMono = loadFont("fonts/IBMPlexMono-Regular.ttf");
  img = loadImage('images/goose.png'); // Replace 'path/to/your/image.jpg' with the actual path to your image

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

  count = 0;

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




function draw() {
  noStroke();
  background(backgroundColor);

  translate(width / 2, height / 2);

  // Draw random shapes
  for (let i = 0; i < 50; i++) {
    let shapeColor = hl.randomElement(colorChoices);
    let shapeSize = random(50, width * 0.5);

    fill(shapeColor);
    ellipse(
      random(-width / 2, width / 2),
      random(-height / 2, height / 2),
      shapeSize,
      shapeSize
    );
  }

  rotate(radians(Math.random() * 365)); // Rotate the image by the specified angle
  image(img, -img.width / 2, -img.height / 2); // Display the image at the center of the sketch

  hl.token.capturePreview();

  count = count + 1;
}

function gradientBackground(color1, color2, color3, color4) {
  for (let y = 0; y < height; y++) {
    const inter = map(y, 0, height, 0, 1);
    const gradientColor = lerpColor(color1, color4, inter);
    stroke(gradientColor);
    line(0, y, width, y);
  }
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
