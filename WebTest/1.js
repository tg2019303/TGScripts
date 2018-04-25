// JavaScript Document
var a=1;
document.write(a);

function pr(){
	var b=new Date();
	var p=document.getElementById("pp");
	p.innerHTML=b;
	var d=document.getElementById("di");
	//document.write(d);
	//d.height="300px"
	//document.write(p);
}
function yyy(){
	alert($("a").html())
	setInterval(pr,1000);
}
window.onload=yyy;