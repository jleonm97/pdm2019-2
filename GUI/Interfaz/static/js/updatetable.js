
var rx = document.getElementById("rotx");
var ry = document.getElementById("roty");

var intervalID = setInterval(
function(){
 var angulo = $.getJSON( "http://10.100.186.188:3000/Prueba", function() {
   rx.innerHTML=angulo.responseJSON.X;
   ry.innerHTML=angulo.responseJSON.Y;
})
  .fail(function() {
    console.log( "error: no se recibe angulos" );
  });
  },1000);

