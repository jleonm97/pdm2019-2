
var css;
var intervalID = setInterval(
function(){
    var angulo = $.getJSON( "http://10.100.186.125:3000/Prueba", function() {
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
    console.log( "error: no se recibe angulos" );
    if (!css) {
        css = document.createElement('style');
        document.body.appendChild(css);
      }
      let cssText = `x-model {
         transform: rotateX(45deg) rotateY(0deg) rotateZ(225deg);
      }`;
      css.textContent = cssText;
  });
 },1000);
/*    const updateStyles = () => {
      if (!css) {
        css = document.createElement('style');
        document.body.appendChild(css);
      }
      let cssText = `x-model {
         transform: rotateX(${X.value}deg) rotateY(${Y.value}deg) rotateZ(225deg);
      }`;
      css.textContent = cssText;
    }
  

    updateStyles()
 */   
  //.wrap {
  //      perspective: ${perspective.value}px;
  //      perspective-origin: ${perspectiveOriginX.value}% ${perspectiveOriginY.value}%;
  //    }*/
  // transform: rotateX(${rotateX.value +45}deg) rotateY(${rotateY.value}deg) rotateZ(225deg);
  //http://192.168.10.10:3000