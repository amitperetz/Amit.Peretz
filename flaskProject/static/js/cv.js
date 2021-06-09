
let txt= "hello! welcome to my page:)";
let i=0;
let speed=100;
function MovingTXT(){
    document.getElementById("movingText").innerHTML+=txt.substring(i,i+1);
    i=i+1;
    setTimeout(MovingTXT,speed)
}


function updateBackground() {
    let hr = (new Date()).getHours(),
        body = document.body,
        bstyle = body.style,
        hello = document.querySelector(".hello");
    if (hr < 10) {
    bstyle.backgroundColor = "yellow";
    bstyle.color = "black";
    hello.innerText = "Have a good morning";
  } else if (hr < 20) {
    bstyle.backgroundColor = "green";
    bstyle.color = "white";
    hello.innerText ="Have a good day!";
  } else {
    bstyle.backgroundColor = "black";
    bstyle.color = "white";
    hello.innerText = "Have a good night!";
  }
}

