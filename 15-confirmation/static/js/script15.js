

let deleteIt = function (event, btn) {
  event.preventDefault();
  let newVal = $("#message").val();

  $('.popover').removeClass('show'); // if confirmation - hide
  let selected = $(btn).data('selected');

  $(btn).confirmation(
    {
      rootSelector: '[data-toggle=confirmation]', singleton: true,
      title: 'Delete?',
      content: 'accepted: ' + selected, //+ selected.map(x => '<span>'+x.login+'</span>').filter((x,y,z) => z.indexOf(x) == y).join(', '),
      btnOkLabel: 'Yes',
      btnCancelLabel: 'No',
      customClass: 'popover-success',
      onConfirm: function () {
        $.ajax({
          url: '/',
          type: 'POST',
          data: { "message": newVal }
        }).done(function (result) {
          alert('Success');
        }).fail(function (result) {
          alert('error');
        })
      }
    });
  $(btn).confirmation('show');
}