$( document ).ready(function() {
/*var slider1 = document.getElementById("shmax");
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
var output6 = document.getElementById("vvmin");*/
var init = $.getJSON( "http://10.100.186.188:3000/Prueba3", function(){console.log( init.responseJSON );
slider1.value=init.responseJSON.Slider1;
output1.innerHTML=init.responseJSON.Slider1;

slider2.value=init.responseJSON.Slider2;
output2.innerHTML=init.responseJSON.Slider2;

slider3.value=init.responseJSON.Slider3;
output3.innerHTML=init.responseJSON.Slider3;

slider4.value=init.responseJSON.Slider4;
output4.innerHTML=init.responseJSON.Slider4;

slider5.value=init.responseJSON.Slider5;
output5.innerHTML=init.responseJSON.Slider5;

slider6.value=init.responseJSON.Slider6;
output6.innerHTML=init.responseJSON.Slider6;});


console.log("ready!");
});