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
        else if($(this).hasClass('Demo')){
            $('html, body').animate({
                scrollTop: $('body').offset().top = 950
            }, 800, function() {
                // if you need a callback function
            });
        }
    });
    $(".loginBtnSubmit").on("click", function(e){
        if($('input[name="loginEmail"]').val() != '' & $('input[name="loginPassword"]').val() != ''){
            location.href = "http://127.0.0.1:5500/Website%20Frontend/login.html";
        }
        
    })

    $( ".getDemoBtn" ).on( "click", function() {
        console.log( "click" );
    });

    $('.getDemoBtn').on("click", function(){
        $(".form-popup")[0].style.display = "block";
    })
    $('.getAppointBtn').on("click",function(){
        $(".form-popup")[0].style.display = "block";
    })
    $('.btn-login').on("click",function(){
        $("#loginForm")[0].style.display = "block";
    })
    $('.getDemoBtn').on("click",function(){
        $("#myForm")[0].style.display = "block";
    })
    $('.btn-logout').on("click",function(){
        location.href = "index.html";
    })
    $('.cancel').on('click',function(){
        $(".form-popup")[0].style.display = "none";
    })
    function onSignIn(googleUser) {
        var id_token = googleUser.getAuthResponse().id_token;
        // Send the ID token to your server to authenticate the user
      }

    
}
