var slider1 = document.getElementById("shmax");
var output1 = document.getElementById("vhmax");

var slider2 = document.getElementById("shmin");
var output2 = document.getElementById("vhmin");

var slider3 = document.getElementById("ssmax");
var output3 = document.getElementById("vsmax");

var slider4 = document.getElementById("ssmin");
var output4 = document.getElementById("vsmin");

var slider5 = document.getElementById("svmax");
var output5 = document.getElementById("vvmax");

var slider6 = document.getElementById("svmin");
var output6 = document.getElementById("vvmin");

// Display the default slider value

output1.innerHTML = slider1.value; 
output2.innerHTML = slider2.value;
output3.innerHTML = slider3.value;
output4.innerHTML = slider4.value;
output5.innerHTML = slider5.value;
output6.innerHTML = slider6.value;

// Update the current slider value (each time you drag the slider handle)

//Cada vez que se mueve los sliders se debe mostrar el valor del mismo en la interfaz y además enviar
//los valores de todos los sliders a la página que lo rececpciona y envía al programa de calibración.
slider1.oninput = function() {
  output1.innerHTML = this.value;
 
  datos = {"Slider1":slider1.value, "Slider2":slider2.value, "Slider3":slider3.value, "Slider4":slider4.value, "Slider5":slider5.value, "Slider6":slider6.value};
  $.post("http://10.100.187.13:3000/Prueba2", datos , function(){});
}

slider2.oninput = function() {
  output2.innerHTML = this.value;
  datos = {"Slider1":slider1.value, "Slider2":slider2.value, "Slider3":slider3.value, "Slider4":slider4.value, "Slider5":slider5.value, "Slider6":slider6.value};
  $.post("http://10.100.187.13:3000/Prueba2", datos , function(){});
}

slider3.oninput = function() {
  output3.innerHTML = this.value;
  datos = {"Slider1":slider1.value, "Slider2":slider2.value, "Slider3":slider3.value, "Slider4":slider4.value, "Slider5":slider5.value, "Slider6":slider6.value};
  $.post("http://10.100.187.13:3000/Prueba2", datos , function(){});
}

slider4.oninput = function() {
  output4.innerHTML = this.value;
  datos = {"Slider1":slider1.value, "Slider2":slider2.value, "Slider3":slider3.value, "Slider4":slider4.value, "Slider5":slider5.value, "Slider6":slider6.value};
  $.post("http://10.100.187.13:3000/Prueba2", datos , function(){});
}

slider5.oninput = function() {
  output5.innerHTML = this.value;
  datos = {"Slider1":slider1.value, "Slider2":slider2.value, "Slider3":slider3.value, "Slider4":slider4.value, "Slider5":slider5.value, "Slider6":slider6.value};
  $.post("http://10.100.187.13:3000/Prueba2", datos , function(){});
}

slider6.oninput = function() {
  output6.innerHTML = this.value;
  datos = {"Slider1":slider1.value, "Slider2":slider2.value, "Slider3":slider3.value, "Slider4":slider4.value, "Slider5":slider5.value, "Slider6":slider6.value};
  $.post("http://10.100.187.13:3000/Prueba2", datos , function(){});
}
