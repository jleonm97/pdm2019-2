
    var css;
	var rotateX;
	var rotateY;
rotateX.value=0;
rotateY.value=0;
    const updateStyles = () => {
      if (!css) {
        css = document.createElement('style');
        document.body.appendChild(css);
      }
      let cssText = `x-model {
        transform: rotateX(${rotateX.value +45}deg) rotateY(${rotateY.value}deg) rotateZ(225deg);
      }`;
      css.textContent = cssText;
    }
  

    updateStyles()
    
  //.wrap {
  //      perspective: ${perspective.value}px;
  //      perspective-origin: ${perspectiveOriginX.value}% ${perspectiveOriginY.value}%;
  //    }*/
  
  //http://192.168.10.10:3000