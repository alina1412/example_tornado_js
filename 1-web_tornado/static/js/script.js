$(document).ready(function () {
    function handleSubmit(event) {
        event.preventDefault();
        const data = new FormData(event.target);
        const message1 = data.get('message');
        console.log(message1);

        let body = JSON.stringify({
            "message1": message1,
            "dictionary": {
                "inner_key": 1
            }
        });
        $.post("/", body )
        .done(function(data) { console.log(data) })
        return true;
    }

    $('form').on('submit', handleSubmit);
})