// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []

// Create the functions for the tasks

// ADD A NEW STUDENT

function new_student(name) {
  roster.push(name);
}

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array


// REMOVE STUDENT


function remove_student(name) {
//   var indexes = [];
//   var index = roster.indexOf(name);
//   while (index != -1) {
//   indexes.push(index);
//   index = roster.indexOf(name, index + 1);
// }
//   console.log(indexes);
//   roster.splice(indexes,1);
//   for (var i = 0; i < indexes.length; i++) {
//     value = indexes[i];
//     roster.splice(value,1);
//   }
//

while (roster.indexOf(name)!=-1) {
   var index = roster.indexOf(name);
   roster.splice(index,1)
}
console.log(roster);
 }

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//

// DISPLAY ROSTER
function roster_display() {
  console.log(roster);
}

// Create a function called display that prints out the orster to the console.


// Start by asking if they want to use the web app
var app_start = prompt("Do you want to start the web application y/n");
console.log(app_start);
// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.
while (app_start==="y") {
user_req =prompt("Please select the following option add , remove , display or quit");

if (user_req === "quit") {
  alert("Thank you for using our web application");
  break;
}
else if (user_req === "add") {
   _student = prompt("Please enter student name");
   new_student(_student);

}
else if (user_req === "remove") {
  _remove = prompt("Please provide the student name to be removed");
  remove_student(_remove);

}
else if (user_req === "display") {
  roster_display();

}

}
if (app_start==="n") {
  alert("Thank you for checking out the app")
}
