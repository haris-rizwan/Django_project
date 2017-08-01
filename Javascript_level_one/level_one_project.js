var fn = prompt("Welcome !!!! Please Enter you First Name");
var ln = prompt("Please Enter your Last Name");
var age = prompt("Please enter your age");
var height = prompt("Please enter your height in centimeters");
var pet = prompt("what is your Pet's name");

var x = fn.charAt(0);
// console.log(x);
var y = ln.charAt(0);

var z = age>20&&age<30

var f = height>170

var w = pet.charAt(pet.length-1) === "y"

if (x==y && z && (height>170) && w) {
  console.log("Welcome Agent 007. Nice to have you back");
}
// if (age>20&&age<30) {
// console.log("age right");
// }
