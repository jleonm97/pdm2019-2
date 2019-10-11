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

//datos = {"Slider1":slider1.value/*, "Slider2":slider2.value, "Slider3":slider3.value, "Slider4":slider4.value, "Slider5":slider5.value, "Slider6":slider6.value)*/};
// Update the current slider value (each time you drag the slider handle)
//var Slider1 = [slider1.value]

slider1.oninput = function() {
  output1.innerHTML = this.value;
 // Slider1 = this.value;
 // maxHue = {Slider1:Slider1};
  //alert(JSON.stringify(maxHue))
 /* 
  $.ajax({
       url: "http://10.101.58.62:3000/John",
       type: "POST",
       dataType:"json",
       data: {"Slider1":1, "Slider2":2},
       success: function() {
           alert("NP");
       }
                   
  });*/
  //var mmm = {"nnn":"ppp"};
  //nnn = /*JSON.parse(*/'nel'/*)*/
  datos = {"Slider1":slider1.value, "Slider2":slider2.value, "Slider3":slider3.value, "Slider4":slider4.value, "Slider5":slider5.value, "Slider6":slider6.value};
  $.post("http://10.100.187.13:3000/John", datos , function(){});
  //var sendjson=$.post( "http://10.100.187.13:3000/John", { Slider1: 1 } );
   // console.log(datos)
//  },"json" );
}

slider2.oninput = function() {
  output2.innerHTML = this.value;
  datos = {"Slider1":slider1.value, "Slider2":slider2.value, "Slider3":slider3.value, "Slider4":slider4.value, "Slider5":slider5.value, "Slider6":slider6.value};
  $.post("http://10.100.187.13:3000/John", datos , function(){});
}

slider3.oninput = function() {
  output3.innerHTML = this.value;
  datos = {"Slider1":slider1.value, "Slider2":slider2.value, "Slider3":slider3.value, "Slider4":slider4.value, "Slider5":slider5.value, "Slider6":slider6.value};
  $.post("http://10.100.187.13:3000/John", datos , function(){});
}

slider4.oninput = function() {
  output4.innerHTML = this.value;
  datos = {"Slider1":slider1.value, "Slider2":slider2.value, "Slider3":slider3.value, "Slider4":slider4.value, "Slider5":slider5.value, "Slider6":slider6.value};
  $.post("http://10.100.187.13:3000/John", datos , function(){});
}

slider5.oninput = function() {
  output5.innerHTML = this.value;
  datos = {"Slider1":slider1.value, "Slider2":slider2.value, "Slider3":slider3.value, "Slider4":slider4.value, "Slider5":slider5.value, "Slider6":slider6.value};
  $.post("http://10.100.187.13:3000/John", datos , function(){});
}

slider6.oninput = function() {
  output6.innerHTML = this.value;
  datos = {"Slider1":slider1.value, "Slider2":slider2.value, "Slider3":slider3.value, "Slider4":slider4.value, "Slider5":slider5.value, "Slider6":slider6.value};
  $.post("http://10.100.187.13:3000/John", datos , function(){});
}
