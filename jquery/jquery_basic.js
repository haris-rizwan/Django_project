$('li').click(function () {
  $(this).toggleClass('turnRed');
});
$('h1').click(function () {
  $(this).toggleClass('turnBlue').text('I have been clicked');
})

$('input').eq(0).keypress(function (event) {
  console.log(event);
  if (event.which === 13) {
    $('h1').toggleClass('turnBlue');

  }
})
