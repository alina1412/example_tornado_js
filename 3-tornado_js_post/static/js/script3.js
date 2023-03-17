$(document).ready(function () {
    
    function handleSubmit(event) {
        // const data = new FormData(event.target);
        const message = $('#message').val()

        console.log("here1");
        console.log("will be val message");
        console.log("here2");
        console.log(message);
        console.log("here3");


        if (!message) {
            console.log("no value");
            return false;
        }

        let body = JSON.stringify({
            "message": message
        });
        $.post("/form/", body)
            .done(function (data) {
                console.log(data)
            });
        console.log('posted');
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
