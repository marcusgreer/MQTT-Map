let gl, noctaves, c, song, analyzer, fft, spectrum, renderBuffer;
let points;
let font, fontSize = 140;

function setup() {
    createCanvas(700, 700);
    background(200, 200 , 200);

    points = [];
    for (var i=0;i<22;i++){
        points[i] = {
            x: random(100, 600),
            y: random(100, 600)
        };
    }
}

// pip3 instal paho/mqhtt

function draw() {
    stroke(1000);
    // fill()
    for (var i=0;i<22;i++){
        points[i].x = 100 * 
        points[i].y += -2 * points[i].x / (2 * (points[i].y-1));
        circle(points[i].x, points[i].y, 3);
    }

}
