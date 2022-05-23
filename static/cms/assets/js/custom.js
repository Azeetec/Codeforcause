
/*$(window).on("load",function(){

    //Fade Out
    //$(".loader").delay(1500).fadeOut(500);

    //Slide Left
    $(".loader").delay(1000).animate({width:'toggle'},1000);

});*/


$(document).ready(function() {
    // Users can skip the loading process if they want.
    $('.skip').click(function() {
        $('.overlayer, body').addClass('loaded');
    })

    // Will wait for everything on the page to load.
    $(window).bind('load', function() {
        $('.overlayer, body').addClass('loaded');
        setTimeout(function() {
            $('.overlayer').css({'display':'none'})
        }, 2000)
    });

    // Will remove overlay after 1min for users cannnot load properly.
    setTimeout(function() {
        $('.overlayer, body').addClass('loaded');
    }, 60000);
})


$(document).ready(function(){
    const demovalue = $('.radio-button').val();
    $("#show"+demovalue).show();
    $('.radio-button').click(function(){
        const demovalue = $(this).val();
        $("div.myDiv").hide();
        $("#show"+demovalue).show();
    });
});

