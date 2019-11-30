$(document).ready(function() {
  $(".owl-carousel").owlCarousel({
    loop: true,
    margin: 10,
    autoplay: true,
    autoplayTimeout: 1000,
    autoplayHoverPause: true,
    responsiveClass: true,
    responsive: {
      0: {
        items: 0,
        loop: true
      },
      600: {
        items: 2
      },
      1000: {
        items: 4
      }
    }
  });
});
