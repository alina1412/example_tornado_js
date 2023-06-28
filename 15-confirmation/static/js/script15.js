

let deleteIt = function (event, btn) {
  event.preventDefault();
  let newVal = $("#message").val();

  $('.popover').removeClass('show');      // if other confirmation window  - hide it
  let selected = $(btn).data('selected'); // list of dictionaries

  let html_content = ('accepted:<br/>' + 
                      selected.map(x => '<span> ' + x.login + ' ' + x.when + '</span>')
                      .join(',<br/>'));

  $(btn).confirmation(
    {
      rootSelector: '[data-toggle=confirmation]', 
      singleton: true,
      title: 'Delete?',
      html: true,
      content: html_content,
      btnOkLabel: 'Yes',
      btnCancelLabel: 'No',
      customClass: 'popover-success',
      onConfirm: function () {
        $.ajax({
          url: '/',
          type: 'POST',
          data: { "message": newVal }
        }
        )
          .done(function (result) {
            alert('Success');
          })
          .fail(function (result) {
            alert('error');
          })
      }
    });
  $(btn).confirmation('show');
}