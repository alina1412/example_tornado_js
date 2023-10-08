
$("#button1").on("click", function (e) {
  e.preventDefault();
  let newVal = $("#message").val();

  $.ajax({
    url: '/f1?message=' + newVal,
    type: 'POST'
  });
})


$("#button2").on("click", function (e) {
  e.preventDefault();
  let newVal = $("#message2").val();
  let data_to_send = { 'message': newVal }
  $.ajax({
    url: '/f2',
    type: 'POST',
    contentType: 'application/json; charset=utf-8',
    data: JSON.stringify(data_to_send),
    headers: { 'Content-Type': 'application/json; charset=utf-8' }
    // dataType: 'json'
  });
})


$("#button3").on("click", function (e) {
  e.preventDefault();
  let newVal = $("#message3").val();
  let data_to_send = { 'message': newVal };

  $.post({
    url: '/f3',
    data: JSON.stringify(data_to_send),
  });

})


$("#button4").on("click", function (e) {
  e.preventDefault();
  let newVal = $("#message4").val();
  let data_to_send = { 'message': newVal };

  $.post({
    url: '/f4',
    data: { options: JSON.stringify(data_to_send) },    // not stringified as a whole, but argument
  });
})


