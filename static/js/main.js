var link = "http://127.0.0.1:5000/api/v1.0/hbo-data";

// Getting our GeoJSON data
d3.json(link).then(function(data) {
  let index_vals = [];
  for(i in data.index){
    index_vals.push(Number(data.index[i]))
  }
  console.log()
  var xy = [
    {
      x: [1,2,3,4,5],
      y: index_vals.sort(),
      type: 'bar'
    }
  ];
  
  Plotly.newPlot('myDiv', data);
  for(i in data){
    for(j in i){
      console.log("Here is i: " + i + " | Here is j: " + j)
    }
  }
});


