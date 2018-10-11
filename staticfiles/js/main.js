
$(document).ready(function() {
    $('[data-fancybox="gallery"]').fancybox({
        animationEffect: "zoom-in-out",
        transitionEffect: "zoom-in-out",
        buttons: [
            "fullScreen",
            "zoom",
            "slideShow",
            "close",
            "thumbs"
        ],
        protect: true
    });
});


// ===== Scroll to Top ====
$(window).scroll(function() {
    if ($(this).scrollTop() >= 50) {        // If page is scrolled more than 50px
        $('#return-to-top').fadeIn(200);    // Fade in the arrow
    } else {
        $('#return-to-top').fadeOut(200);   // Else fade out the arrow
    }
});
$('#return-to-top').click(function() {      // When arrow is clicked
    $('body,html').animate({
        scrollTop : 0                       // Scroll to top of body
    }, 500);
});

$(window).on('load', function () {
      $(".bg_gallery").fadeIn(3000).show();
      $(".spinner-wrapper").hide();
      $("footer").fadeIn(3000);
      $(".navbar-default").fadeIn(3000);
      $(".site-wrapper").fadeIn(3000);
      $(".alert").fadeOut(9000);
 });

