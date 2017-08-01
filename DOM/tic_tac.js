var box = document.querySelectorAll('td')

// box.addEventListener("click",function () {
//   var text = box.textContent;
//
// switch (text) {
//   case "":
//   box.textContent = "X";
//     break;
//   case "X":
//   box.textContent = "O";
//    break;
//   case "O":
//   box.textContent = ""
//   break;
// }
// })
// document.querySelectorAll('td')

box.forEach.call(box, function(box) {
  box.addEventListener('click', function() {
    // code…
    switch (box.textContent) {
      case "":
      box.textContent = "X";
        break;
      case "X":
      box.textContent = "O";
       break;
      case "O":
      box.textContent = ""
      break;
    }
  })
})

$('a').click(function () {
  for (var i = 0; i < box.length; i++) {
    box[i].textContent= ""
  }

})









// $('td').click(function () {
//   // var text = box.textContent;
//
// switch ($(this).text()) {
//   case "":
//   $(this).text("X");
//     break;
//   case "X":
//   $(this).text("O");
//    break;
//   case "O":
//   $(this).text("");
//   break;
// }
// })
