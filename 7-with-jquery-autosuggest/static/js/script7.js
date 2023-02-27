$(document).ready(function () {
    $('#message').change(function() {
        console.log("on change");
        $("#message").attr('value', $("#message").val());
        autocomplete_suggest("#message");
    });

    $("#button1").on("click", function(e) {
        e.preventDefault();
        console.log("submit");
        let newVal = $("#message").attr('value') || $("#message").val();
        let newId = $("#message").attr('data-id');

        $.ajax({
            url: '/form?message=' + newVal + '&id=' + newId,
            type: 'GET',
            success: function (data) {
              console.log(data);
            }
          });
    })
})

  
// Suggest-подстановка
var autocomplete_suggest = function(fieldName) {
    $(fieldName).attr('data-id' , '');

    $(fieldName).autocomplete({
      delay: 300,
      minLength: 1,
      source: [{"label": 'One', "id": 1}, {"label": 'Two', "id": 2}],
      select: function(event, ui) {
        $(fieldName).attr('value' , ui.item.label);
        $(fieldName).attr('data-id', ui.item.id);
      }
    });
    $(fieldName).autocomplete( "option", "appendTo", ".ui-front" );
  }




  