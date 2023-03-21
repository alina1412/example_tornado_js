$(document).ready(function () {

  $('.slideshow-container').slick(
    {
      dots: false,
      centerPadding: '30px',
    }
  );

  // zoom image in separate window
  $("#example").colorbox({
    maxWidth: "90%",
    maxHeight: "90%",
    opacity: "0.7",
    close: "Закрыть",
    transition: "fade",
  })

}
);


