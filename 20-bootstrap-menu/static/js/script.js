$(document).ready(function () {
    $('#sub-toggle').click(function(e) {
        e.stopPropagation();
        $("#collapseExample0").toggleClass("d-block", "d-none");
    });
        
})

