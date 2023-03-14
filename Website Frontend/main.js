$(document).ready(function(){
    clickEvents();
    $('html, body').animate({
        scrollTop: $('body').offset().top - 70
    }, 800, function() {
        // if you need a callback function
    });
})
function clickEvents(){
      
    $( ".lowHead ul li" ).on( "click", function(e) {
        if(!$(this).hasClass('pageSelected')){
            $('.pageSelected').removeClass('pageSelected')
            $(this).addClass('pageSelected')
        }
        if($(this).hasClass('Home')){
            $('html, body').animate({
                scrollTop: $('body').offset().top - 70
            }, 800, function() {
                // if you need a callback function
            });
        }
        else if($(this).hasClass('About')){
            $('html, body').animate({
                scrollTop: $('body').offset().top = 390
            }, 800, function() {
                // if you need a callback function
            });
        }
        else if($(this).hasClass('Services')){
            $('html, body').animate({
                scrollTop: $('body').offset().top = 630
            }, 800, function() {
                // if you need a callback function
            });
        }
    });
  

    $( ".getDemoBtn" ).on( "click", function() {
        console.log( "click" );
    });
    
}