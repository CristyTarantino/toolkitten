if (typeof Game === 'undefined') {
  var Game = {};
}

Game.model = {
  generateRandomBoard: function (n, m) {
    m = m || n;

    var world = [];

    if (+n && +m) {
      for (var i=0; i<m; i++){
        world[i] = [];
        for (var j=0; j<n; j++) {
          world[i][j] = Math.round(Math.random());
        }
      }
    }

    return world;
  },

  continentCounter: function (world, x, y) {
    if (y >= 0 &&
        y < world.length &&
        x >= 0 &&
        x < world[0].length &&
        world[y][x] === 1) {

      var size = 1;

      // flag that land as counted
      world[y][x] = -1;

      // row above left column
      size += this.continentCounter(world, x - 1, y - 1);

      // row above above column
      size += this.continentCounter(world, x, y - 1);


      // row above right column
      size += this.continentCounter(world, x + 1, y - 1);

      // same row left column
      size += this.continentCounter(world, x - 1, y);

      // same row right column
      size += this.continentCounter(world, x + 1, y);


      // row below left column
      size += this.continentCounter(world, x - 1, y + 1);

      // row below below column
      size += this.continentCounter(world, x, y + 1);

      // row below right column
      size += this.continentCounter(world, x + 1, y + 1);

      return size;
    }

    return 0;
  },

  findContinets: function (world) {
    var continents = [];

    for(var i=0; i<world.length; i++){
      for(var j=0; j<world[0].length; j++) {
        var curr_cont_size = this.continentCounter(world, j, i);

        if(curr_cont_size){
          continents.push({
            x: j,
            y: i,
            size : curr_cont_size
          });
        }
      }
    }

    continents.sort(function (prev, next) {
      return next.size - prev.size;
    });

    return continents;
  },

  findNLargestContinentsFromWorld: function (world, n) {
    var continents = this.findContinets(world);
    console.log(continents);

    this.findNLargestContinentsFromContinents(continents, n);
  },

  findNLargestContinentsFromContinents: function (continents, n) {
    n = continents.length > n ? n : continents.length;

    return continents.slice(0, n);
  }
};

Game.view = {
  // initialisation
  init: function (document) {
    var worldArray = [];

    console.log('init');

    // Access the form element...
    var form = document.querySelector("#worldSize");

    var counterButton = document.querySelector("#continents_counter");

    counterButton.addEventListener("click", function (event) {
      event.preventDefault();
      var continents = Game.model.findContinets(worldArray);

      var top2Continents = Game.model.findNLargestContinentsFromContinents(continents, 2);

      var fragment1 = document.createDocumentFragment();
      var fragment2 = document.createDocumentFragment();

      var continentsElem = document.querySelector('#country_list');
      var top2ContinentsElem = document.querySelector('#top_2');

      continents.forEach(function (continent) {
        var liElem = document.createElement('li');
        liElem.innerHTML = 'x: ' + continent.x + " y: " + continent.y + " size: " + continent.size;
        fragment1.appendChild(liElem);
      });

      top2Continents.forEach(function (continent) {
        var liElem = document.createElement('li');
        liElem.innerHTML = 'x: ' + continent.x + " y: " + continent.y + " size: " + continent.size;
        fragment2.appendChild(liElem);
      });

      continentsElem.appendChild(fragment1);
      top2ContinentsElem.appendChild(fragment2);
    });

    // Attach the event listener
    form.addEventListener("submit", function (event) {
      event.preventDefault();

      // Bind the FormData object and the form element
      var formData = new FormData(form);

      var width = formData.get('x');
      var height = formData.get('y');

      form.classList.toggle('hide');
      form.reset();

      worldArray = Game.model.generateRandomBoard(width, height);

      generateWorldElemFromArray(worldArray);

      document.getElementById('continents_counter').classList.toggle("hide");

      console.log(worldArray);

      function generateWorldElemFromArray(worldArray) {
        // invisible DOM so you don't interact with the DOM too much
        // because every DOM interaction is a performace hit
        var fragment = document.createDocumentFragment();

        worldArray.forEach(function (row, y) {
          var rowElem = document.createElement('tr');

          row.forEach(function (column, x) {
            var cellElem = document.createElement('td');
            var checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.id = 'y' + y + "x" + x;
            checkbox.coordinates = {
              y: y,
              x: x
            };
            checkbox.checked = !!column;
            cellElem.appendChild(checkbox);
            rowElem.appendChild(cellElem);
          });

          fragment.appendChild(rowElem);
        });

        document.querySelector('#world').appendChild(fragment);
      }
    });
  }
};

Game.view.init(window.document);