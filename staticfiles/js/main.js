setTimeout(fade_out, 5000);

function fade_out() {
  $("#alert_contact").fadeOut().empty();
  $(".alert-danger").fadeOut().empty();
}

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
