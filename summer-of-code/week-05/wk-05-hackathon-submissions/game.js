function generate_random_board(n, m) {
  m = m || n;

  var world = [];

  if (+n && +m) {
     for (var i=0; i<m; i++){
        world[i] = []
        for (var j=0; j<n; j++) {
          world[i][j] = Math.round(Math.random());
        }
     }
  } else {
    console.log('error');
  }

  return world;
}

var ciao = generate_random_board(5);
console.log('log', ciao);

function continent_counter(world, x, y) {
  console.log(world, x, y, world.length, world[0].length);
  if (y >= 0 && y < world.length && x >= 0 && x < world[0].length) {
    console.log('if');
    if (world[y][x] !== 1) {
      return 0;
    }

    var size = 1;

    // flag that land as counted
    world[y][x] = -1;

    // row above left column
    console.log("1 continent_counter", x - 1, y - 1);
    size += continent_counter(world, x - 1, y - 1);

    // row above above column
    console.log("2 continent_counter");
    size += continent_counter(world, x, y - 1);

    // row above right column
    console.log("3 continent_counter");
    size += continent_counter(world, x + 1, y - 1);

    // same row left column
    console.log("4 continent_counter");
    size += continent_counter(world, x - 1, y);

    // same row right column
    console.log("5 continent_counter");
    size += continent_counter(world, x + 1, y);

    // row below left column
    console.log("6 continent_counter");
    size += continent_counter(world, x - 1, y + 1);

    // row below below column
    console.log("7 continent_counter");
    size += continent_counter(world, x, y + 1);

    // row below right column
    console.log("8 continent_counter");
    size += continent_counter(world, x + 1, y + 1);

    return size;
  }
  else {
    console.log('else');
    return 0;
  }
}



var ciao_2 = ciao.slice(0);
console.log("PROGRAMMMMMM", ciao_2);


var a = continent_counter(ciao_2, 0, 0);

console.log(a);
