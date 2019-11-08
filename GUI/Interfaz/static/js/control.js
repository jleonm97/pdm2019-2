/*var modo = 0;
var forward=0;
var turn=0;
var height=0;
var grip=0;*/
var control = {"m":0,"f":0,"t":0,"h":0,"g":0};
var url0 = "http://10.100.186.125:3000/Control";

function auto() {
    document.getElementById("wasd").style.display = "none";
    control.m = 0;
}

function manual() {
    document.getElementById("wasd").style.display = "inline";
    control.m = 1;
}
$(document).keypress(function(){
    console.log(event.which)
      if( control.m == 0){  //mode
        console.log("auto-mode")
      };
      if( control.m == 1){  //mode
        console.log("manual-mode")
      };
      if(event.which == 119 && control.m == 1){  //w
        console.log("forward");
        control.f=1;
      };
      if(event.which == 97 && control.m == 1){  //a
        console.log("left");
        control.t=-1;
      };
      if(event.which == 115 && control.m == 1){  //s
        console.log("back");
        control.f=-1;
      };
      if(event.which == 100 && control.m == 1){  //d
        console.log("right");
        control.t=1;
      };
      if(event.which == 99 && control.m == 1){  //c
        console.log("down");
        control.h=-1;
      };
      if(event.which == 32 && control.m == 1){  //space
        console.log("up");
        control.h=1;
      };
      if(event.which == 101 && control.m == 1){  //e
        console.log("grip");
        control.g=1;
    };
    $.post(url0, control , function(){});
});
$(document).keyup(function(){
  control.f=0;
  control.t=0;
  control.h=0;
  control.g=0;
  $.post(url0, control , function(){});
});