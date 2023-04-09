$(document).ready(function () {
    clickEvents();
    $('html, body').animate({
        scrollTop: $('body').offset().top - 70
    }, 800, function () {
        // if you need a callback function
    });
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
        if ($('input[name="loginEmail"]').val() != '' & $('input[name="loginPassword"]').val() != '') {
            window.location.href = "login.html";
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
        location.href = "index.html";
    })
    $('.cancel').on('click', function () {
        $(".form-demo")[0].style.display = "none";
        $(".form-appointment")[0].style.display = "none";
        $(".form-login")[0].style.display = "none";
    })
    $('.btn-demoSubmit').on("click", function (event) {
        event.preventDefault();
        $(".DemoScreen").removeClass('hide')
        goPython()
    })

    function goPython(){
        uploadtoS3().then(function(resp){
            console.log(resp)
            // window.location.href="http://127.0.0.1:5000/"
        });
       
    }

    

    // console.log(uploadedImage.Location)
}

async function uploadtoS3(){
    toDataUrl($('input')[7].files[0], function(base64Img) {
        console.log(base64Img);
    });
    // loadXHR($('input')[7].files[0])
    // const s3 = new AWS.S3({
    //     accessKeyId: "AKIAYYI7C6SJFZEPVLW4",
    //     secretAccessKey: "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",
    // })

    // const uploadedImage = await s3.upload({
    //     Bucket: 'dcproject123456',
    //     Key: $('input').files[0].originalFilename,
    //     Body: blob,
    // }).promise()
    

    // e.preventDefault();
    // debugger;
	// the_file = $('input')[7].files[0]; //get the file element
	// var filename = Date.now() + '.' + the_file.name.split('.').pop(); //make file name unique using current time (milliseconds)
	// $(this).find("input[name=key]").val(filename); //key name 
	// $(this).find("input[name=Content-Type]").val(the_file.type); //content type
	
    // var post_url = $(this).attr("action"); //get form action url
    // var form_data = new FormData(); //Creates new FormData object
    // $.ajax({
    //     url : 'https://www.google.com',
    //     type: 'post',
	// 	datatype: 'xml',
    //     data : form_data,
	// 	contentType: false,
    //     processData:false,
	// 	xhr: function(){
	// 		var xhr = $.ajaxSettings.xhr();
    //         debugger;
	// 		if (xhr.upload){
	// 			var progressbar = $("<div>", { style: "background:#607D8B;height:10px;margin:10px 0;" }).appendTo("#results"); //create progressbar
	// 			xhr.upload.addEventListener('progress', function(event){
	// 					var percent = 0;
	// 					var position = event.loaded || event.position;
	// 					var total = event.total;
	// 					if (event.lengthComputable) {
	// 						percent = Math.ceil(position / total * 100);
	// 						progressbar.css("width", + percent +"%");
	// 					}
	// 			}, true);
	// 		}
	// 		return xhr;
	// 	}
    // }).done(function(response){
    //     debugger;
	// 	var url = $(response).find("Location").text(); //get file location
	// 	var the_file_name = $(response).find("Key").text(); //get uploaded file name
    //     $("#results").html("<span>File has been uploaded, Here's your file <a href=" + url + ">" + the_file_name + "</a></span>"); //response
    // });
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
 debugger;


   


};

function toDataUrl(url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.onload = function() {
        var reader = new FileReader();
        reader.onloadend = function() {
            callback(reader.result);
        }
        reader.readAsDataURL(xhr.response);
    };
    xhr.open('GET', url);
    xhr.responseType = 'blob';
    xhr.send();
}
