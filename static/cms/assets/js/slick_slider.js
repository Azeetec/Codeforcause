$('.slider').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 3000,
    // arrows: false
});

$('.blog-slider').slick({
    slidesToShow: 4,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 3000,
    // arrows: false
    responsive: [
     {
     breakpoint: 1023,
     settings: {
     slidesToShow: 3,
     slidesToScroll: 1,
     dots: false,
     arrows: false
     }
     },
     {
     breakpoint: 767,
     settings: {
     slidesToShow: 1,
     slidesToScroll: 1,
     dots: false,
     arrows: false
     }
     }
    ]
});
