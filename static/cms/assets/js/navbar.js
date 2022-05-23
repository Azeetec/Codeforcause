window.onload = function () {
    $('nav').toggleClass('solid', $(this).scrollTop() > 50);
}
$(window).scroll(function(){
    $('nav').toggleClass('solid', $(this).scrollTop() > 50);
});

$(document).click(function (event) {
    const click = $(event.target);
    const _open = $(".navbar-collapse").hasClass("show");
    if (_open === true && !click.hasClass("navbar-toggler")) {
        $(".navbar-toggler").click();
    }
});
