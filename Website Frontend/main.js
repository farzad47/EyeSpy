$(document).ready(function () {
    clickEvents();
    $('html, body').animate({
        scrollTop: $('body').offset().top - 70
    }, 800, function () {
        // if you need a callback function
    });
    if(localStorage.getItem("customer_id") != null){
        getHistoryData();
    }
})
function clickEvents() {
    $(".lowHead ul li").on("click", function (e) {
        if (!$(this).hasClass('pageSelected')) {
            $('.pageSelected').removeClass('pageSelected')
            $(this).addClass('pageSelected')
        }
        if ($(this).hasClass('Home')) {
            $('html, body').animate({
                scrollTop: $('body').offset().top - 70
            }, 800, function () {
                // if you need a callback function
            });
        }
        else if ($(this).hasClass('About')) {
            $('html, body').animate({
                scrollTop: $('body').offset().top = 390
            }, 800, function () {
                // if you need a callback function
            });
        }
        else if ($(this).hasClass('Services')) {
            $('html, body').animate({
                scrollTop: $('body').offset().top = 630
            }, 800, function () {
                // if you need a callback function
            });
        }
        else if ($(this).hasClass('Demo')) {
            $('html, body').animate({
                scrollTop: $('body').offset().top = 950
            }, 800, function () {
                // if you need a callback function
            });
        }
    });
    $(".loginBtnSubmit").on("click", function (e) {
        email = $('input[name="loginEmail"]').val()
        pass = $('input[name="loginPassword"]').val()
        if (email != '' & pass != '') {
            $(".error").addClass('hide')
            checkLogin(email,pass)
            
        }
        
    })
    $('.getDemoBtn').on("click", function () {
        $(".form-demo")[0].style.display = "block";
    })
    $('.getAppointBtn').on("click", function () {
        $(".form-appointment")[0].style.display = "block";
    })
    $('.btn-login').on("click", function () {
        $(".form-login")[0].style.display = "block";
    })
    $('.getDemoBtn').on("click", function () {
        $(".form-demo")[0].style.display = "block";
    })
    $('.btn-logout').on("click", function () {
        localStorage.clear()
        location.href = "index.html";
    })
    $('.cancel').on('click', function () {
        $(".form-demo")[0].style.display = "none";
        $(".form-appointment")[0].style.display = "none";
        $(".form-login")[0].style.display = "none";
    })
    $('.btn-demoSubmit').on("click", function (event) {
        event.preventDefault();
        $(".DemoScreen").removeClass('hide');
        // var theFormFile = $('#theFile').get()[0].files[0];
        var nameTemp = $("input[name='name']").val()
       var email= $("input[name='email']").val()
  var phone= $("input[name='phone']").val()
  var photos= "configAWS"
  var carrier= $("select[name='carrier']").val()
  var address = $("input[name='Address']").val()
  $(".error").addClass('hide')
        submitDemoDetails(nameTemp,email,phone,photos,carrier,address)
    })

    function goPython(){
        uploadtoS3().then(function(resp){
            console.log(resp)
            // window.location.href="http://127.0.0.1:5000/"
        });
       
    }

    

    // console.log(uploadedImage.Location)
}



function loadXHR(url) {

    // var fs = require('fs'); 
    // var imagedata = $('input')[7].files[0] // get imagedata from POST request 
    // //find path to store
    // // fs.writeFile("../Auth_Individuals/NewAnu", imagedata, 'binary', function(err) { 
    // //     console.log("The file was saved!"); 
     
    // // });  
    
    // writeFile( "../Auth_Individuals/NewAnu", null, imagedata )
    const fileInput = $('input')[7] ;


  const file = fileInput.files[0];
  const imageData = file.arrayBuffer();

//   const imageUrl = uploadImage(imageData);
  const url12 = 'https://example.com/upload';
  const formData = new FormData();
  formData.append('image', imageData);

  const response = fetch(url12, {
    method: 'POST',
    body: formData
  });


   


};

function checkLogin(email,pass){
    $.ajax({
        contentType: 'application/json',
        data: JSON.stringify({"user_email":email}),
        dataType: 'json',
        success: function(data){
            if(data.length == 0){
                $(".email-not").removeClass('hide')
            }else{
                if(data[0][3] == pass ){
                    localStorage.setItem("customer_id",data[0][0])
                    window.location.href = "login.html";
                }else{
                    $(".pass-not").removeClass('hide')
                }
            }
        },
        error: function(){
            app.log("Device control failed");
        },
        processData: false,
        type: 'POST',
        url: 'http://localhost:8888/getUserLogin'
    });
}

function getHistoryData(){
    $.ajax({
        contentType: 'application/json',
        data: JSON.stringify({"cust_id":localStorage.getItem("customer_id")}),
        dataType: 'json',
        success: function(data){
                const table = document.getElementById("historyTable");
               
                headings = ["Sr No.", "Name", "Alert Sent","Date and Time","Access Type"]
                for(var i=0; i < data.length ; i++){
                    let row = table.insertRow();
                    for(var j=0 ; j < headings.length ; j++){
                       var temp =  row.insertCell(j);
                       temp.innerHTML = data[i][j];
                    }
                }
              
        },
        error: function(xhr){
            app.log("Device control failed");
        },
        processData: false,
        type: 'POST',
        url: 'http://localhost:8888/getHistory'
    })
}

function submitDemoDetails(name,email,phone,photo,carrier,address){
    $.ajax({
        contentType: 'application/json',
        data: JSON.stringify({"user_name":name,"email_id": email ,"phone_no":phone,"photos_link":photo,"carrier":carrier,"address":address}),
        dataType: 'json',
        success: function(data){
            window.location.href = "login.html";
           
        },
        error: function(xhr){

            if(xhr.readyState == 4){
                $(".email-exist").removeClass("hide")
            }else{
                $(".some-other-error").removeClass("hide")
            }
        },
        processData: false,
        type: 'POST',
        url: 'http://localhost:8888/submitDemoDetails'
    });

    // $.ajax({
    //     type: 'PUT',
    //     url: uploadPreSignedUrl,
    //     // Content type must much with the parameter you signed your URL with
    //     contentType: 'binary/octet-stream',
    //     // this flag is important, if not set, it will try to send data as a form
    //     processData: false,
    //     // the actual file is sent raw
    //     data: theFormFile
    //   })
    //   .success(function() {
    //     alert('File uploaded');
    //   })
    //   .error(function() {
    //     alert('File NOT uploaded');
    //     console.log( arguments);
    //   });
}



var s3 = new AWS.S3({
    accessKeyId: 'AKIAYYI7C6SJKZZZKZUO',
    secretAccessKey: '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'
  });
  
  var uploadPreSignedUrl = s3.getSignedUrl('putObject', {
      Bucket: 'dcproject123456',
      Key: '482905.jpg',
      ACL: 'authenticated-read',
      // This must match with your ajax contentType parameter
      ContentType: 'binary/octet-stream'
  
      /* then add all the rest of your parameters to AWS puttObect here */
  });
  
  var downloadPreSignedUrl = s3.getSignedUrl('getObject', {
      Bucket: 'dcproject123456',
      Key: '482905.jpg',
      /* set a fixed type, or calculate your mime type from the file extension */
      ResponseContentType: 'image/jpeg'
      /* and all the rest of your parameters to AWS getObect here */
  });
  
  // now you have both urls
  console.log( uploadPreSignedUrl, downloadPreSignedUrl ); 
 
