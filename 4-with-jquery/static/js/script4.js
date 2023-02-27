$(document).ready(function () {

    function handleSubmit(event) {
        const myMessage = $('#message').val()

        console.log("will be val message");
        console.log(myMessage);
     
        if (!myMessage) {
            console.log("no value");
            return false;
        }

        let body = JSON.stringify({"message": myMessage});
        $.post("/form/", body)
            .done(function (data) {
                console.log(data)
            });
        console.log('posted');

        showAlert($('#success-alert'));
        return true;
    }

    $('#button1').on('click', (event) => {
        event.preventDefault();

        if (handleSubmit(event)) {
            return true;
        }
        return false;
    });

})

  

// Show alert and return Alert back
var showAlert = function (allert_window) {
    allert_window.addClass('myAlert');
    $("#success-alert").show().animate({
        opacity: 1,
        top: "100px",
      }, 500, function () {
        allert_window.delay(2000).animate({
          opacity: 0,
          top: "200px",
        }, 500, function () {
          allert_window.removeClass('myAlert');
        });
      });
}