$(document).ready(function () {
    function handleSubmit(event) {
        event.preventDefault();
        const data = new FormData(event.target);
        const value = data.get('message');
        console.log({
            value
        });

        let body = JSON.stringify({
            "message": value,
            "d": {
                "a": 1
            }
        });
        $.post("http://localhost:8888", {"options": body} )
        .done(function(data) { console.log(data) })
        
    }

    const form = document.querySelector('form');
    form.addEventListener('submit', handleSubmit);
})