$(document).ready(function () {

    $('.slideshow-container').slick(
      {
        dots: false,
        centerPadding: '30px',
      }
    );


    $("a.colorbox").colorbox({
      maxWidth:"90%",
      maxHeight:"90%",
      opacity:"0.7",
      close: "Закрыть",
      transition: "fade",
  })
  // ↻

}
);



var angleImg = 0;

function rotateImageClockWise() {
  console.log(angleImg);
  angleImg += 90;
  $(this).rotate(angleImg);
}
 

