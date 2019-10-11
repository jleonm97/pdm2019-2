
var css;
var intervalID = setInterval(
function(){
    var angulo = $.getJSON( "http://10.101.58.62:3000/Prueba", function() {
x=angulo.responseJSON.X + 45;
y=angulo.responseJSON.Y;
if (!css) {
        css = document.createElement('style');
        document.body.appendChild(css);
      }
      let cssText = `x-model {
         transform: rotateX(${x}deg) rotateY(${y}deg) rotateZ(225deg);
      }`;
      css.textContent = cssText;
})
  .fail(function() {
    alert( "error: no se recibe angulos" );
  });
 },1000);
