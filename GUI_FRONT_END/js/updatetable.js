
var rx = document.getElementById("rotx");
var ry = document.getElementById("roty");

var intervalID = setInterval(
function(){
 var angulo = $.getJSON( "http://10.101.58.62:3000/Prueba", function() {
   rx.innerHTML=angulo.responseJSON.X;
   ry.innerHTML=angulo.responseJSON.Y;
})
  .fail(function() {
    alert( "error: no se recibe angulos" );
  });
  },1000);

