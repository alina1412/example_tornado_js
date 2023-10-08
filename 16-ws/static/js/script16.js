$(document).ready(function () {


    var socket = $.simpleWebSocket(
        {
            url: 'ws://' + location.host + '/main/', // ,   'ws://127.0.0.1:8888/main/'
            timeout: 0, // optional, default timeout between connection attempts
            // dataType: 'json', // optional (xml, json, text), default json
        }
    );

    socket.connect();
        
    // socket.isConnected(); // or: socket.isConnected(function(connected) {});

    $('#button1').on('click', (event) => {
        event.preventDefault();
        $.post("/", 
            { 'message': $('#message').val() } // 
            
            ).done(function (data) {
                // console.log(data);
                socket.send({'message': $('#message').val() });
            });
    })
    

    socket.listen(function (message) {
        console.log('listen');
        // console.log(message);
        if (message && message['event']) {
            alert(message['event'])
        }
    })

})
 

