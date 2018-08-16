function generate_random_board(n, m) {
  m = m || n;

  var world = [];

  if (+n && +m) {
     for (var i=0; i<m; i++){
        world[i] = [];
        for (var j=0; j<n; j++) {
          world[i][j] = Math.round(Math.random());
        }
     }
  } else {
    console.log('error');
  }

  return world;
}

var ciao = generate_random_board(5, 10);
console.log("log", ciao);

function continent_counter(world, x, y) {
  if (y >= 0 &&
      y < world.length &&
      x >= 0 &&
      x < world[0].length &&
      world[y][x] === 1) {
    
    var size = 1;

    // flag that land as counted
    world[y][x] = -1;

    // row above left column
    size += continent_counter(world, x - 1, y - 1);

    // row above above column
    size += continent_counter(world, x, y - 1);


    // row above right column
    size += continent_counter(world, x + 1, y - 1);

    // same row left column
    size += continent_counter(world, x - 1, y);

    // same row right column
    size += continent_counter(world, x + 1, y);


    // row below left column
    size += continent_counter(world, x - 1, y + 1);

    // row below below column
    size += continent_counter(world, x, y + 1);

    // row below right column
    size += continent_counter(world, x + 1, y + 1);

    return size;
  }
  
  return 0;
}


function find_continets(world) {
  console.log(world);
  var continents = {};
  
  for(var i=0; i<world.length; i++){
    for(var j=0; i<world[0].length; j++) {
      var curr_cont_size = continent_counter(world, j, i);
      
      if(curr_cont_size){
        continents["continent-row-" + i + "-column-" + j] = curr_cont_size;
      }
    }
  }
  
  return continents;
}


var ciao_2 = ciao.slice(0);
console.log("PROGRAMMMMMM", ciao_2);


var a = continent_counter(ciao_2, 0, 0);

console.log(a);
