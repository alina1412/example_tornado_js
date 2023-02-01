$(document).ready(function () {

    function handleSubmit(event) {
        // event.preventDefault();
        // const data = new FormData(event.target);
        // const message = data.get('message');
        const message = $('#message').val()

        console.log("here1");
        console.log("will be val message");
        console.log("here2");
        console.log(message);
        console.log("here3");



        if (!message) {
            // event.preventDefault();
            console.log("no value");
            return false;
        }

        let body = JSON.stringify({
            "message": message
        });
        $.post("http://localhost:8888/form/", body)
            .done(function (data) {
                console.log(data)
            });
        console.log('posted');

        showAlert();
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


var returnAlert = async function () {
    await sleep(1000);
    $("#success-alert").hide();
    $("#success-alert").animate({
        opacity: 0,
        top: "+=120"
    }, 1);
}
// Показ alerta "Сохранено" с анимацией и возврат returnAlert на место
var showAlert = async function () {
    $("#success-alert").show();
    $("#success-alert").animate({
        opacity: 1,
        top: "-=120"
    }, 2100, returnAlert);
}