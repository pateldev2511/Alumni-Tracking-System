// Facebook JS

window.fbAsyncInit = function() {
    FB.init({
      appId      : '197993864634313',
      cookie     : true,
      xfbml      : true,
      version    : 'v6.0'
    });

    FB.getLoginStatus(function(response) {
        statusChangeCallback(response);
    });
  };

  (function(d, s, id){
     var js, fjs = d.getElementsByTagName(s)[0];
     if (d.getElementById(id)) {return;}
     js = d.createElement(s); js.id = id;
     js.src = "//connect.facebook.net/en_US/sdk.js";
     fjs.parentNode.insertBefore(js, fjs);
   }(document, 'script', 'facebook-jssdk'));

   function statusChangeCallback(response){
     if(response.status === 'connected'){
       console.log('Logged in and authenticated');
       setElements(true);
       document.getElementById('facebook-response').style.display = "block";

       testAPI();
     } else {
       console.log('Not authenticated');
       document.getElementById('facebook-response').style.display = "none";
       setElements(false);
     }
   }

  function checkLoginState() {
    FB.getLoginStatus(function(response) {
      statusChangeCallback(response);
    });
  }

  function testAPI(){
    FB.api('/me?fields=name,email,birthday,location', function(response){
      if(response && !response.error){
        console.log(response);
        buildProfile(response);
      }
    })
  }

  function buildProfile(user){
    //  console.log(user);
    document.getElementById('facebook-response').style.display = "block";

    let profile = `
      <h3>${user.name}</h3>
     
        <p>User ID: ${user.id}</p>
        <p>Email: ${user.email}</p>
        <p>Birthday: ${user.birthday}</p>
        <p>User Location: ${user.location.name}</p>
    `;

    document.getElementById('profile').innerHTML = profile;
  }


  function setElements(isLoggedIn){
    if(isLoggedIn){
      document.getElementById('logout').style.display = 'block';
      document.getElementById('profile').style.display = 'block';
      document.getElementById('fb-btn').style.display = 'none';
      document.getElementById('heading').style.display = 'none';
      document.getElementById('facebook-response').style.display = "block";

    } else {
      document.getElementById('logout').style.display = 'none';
      document.getElementById('profile').style.display = 'none';

      document.getElementById('fb-btn').style.display = 'block';
      document.getElementById('heading').style.display = 'block';
      document.getElementById('facebook-response').style.display = "none";

    }
  }

  function logout(){
    FB.logout(function(response){
      setElements(false);
    //   FB.Auth.setAuthResponse(null, 'unknown');
      window.location.reload();
      document.getElementById('facebook-response').style.display = "none";

    });
  }



  // Captch JS

  
  var code;
function createCaptcha() {
  //clear the contents of captcha div first 
  document.getElementById('captcha').innerHTML = "";
  var charsArray =
  "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
  var lengthOtp = 6;
  var captcha = [];
  for (var i = 0; i < lengthOtp; i++) {
    //below code will not allow Repetition of Characters
    var index = Math.floor(Math.random() * charsArray.length + 1); //get the next character from the array
    if (captcha.indexOf(charsArray[index]) == -1)
      captcha.push(charsArray[index]);
    else i--;
  }
  var canv = document.createElement("canvas");
  canv.id = "captcha";
  canv.width = 100;
  canv.height = 50;
  
  var ctx = canv.getContext("2d");
  ctx.font = "25px Georgia";
  ctx.strokeText(captcha.join(""), 0, 30);
  //storing captcha so that can validate you can save it somewhere else according to your specific requirements
  code = captcha.join("");
  document.getElementById("captcha").appendChild(canv); // adds the canvas to the body element
}

function validateCaptcha() {
  event.preventDefault();


  var email = document.getElementById('email').value;
  var password = document.getElementById('password').value;

  if(email.length == 0 || email == "")
  {
    Swal.fire({
      icon: 'error',
      title: 'Please Enter Email.',
    });
  }
  else {
    if(password.length == 0 || password == "")
    {
      Swal.fire({
        icon: 'error',
        title: 'Please Enter Password.',
      });
    }
    else {
      if (document.getElementById("cpatchaTextBox").value == code) {
    
        document.getElementById('loader_container').style.display = "block";
                          if(document.getElementById('loader_container').style.display == "block")
                          {
    
                            
                              var xmlhttp = new XMLHttpRequest();
                              xmlhttp.open("GET", "/college/login?mode=1&email=" +email+"&password="+password, false);
                              xmlhttp.send(null);
                              var res = xmlhttp.responseText;
                              var obj = JSON.parse(res);
                            
                              if(obj.res == 1)
                              {
                                document.getElementById('loader_container').style.display = "none";
                                window.location = "/college/home";
                              }
                              else {
                                document.getElementById('loader_container').style.display = "none";
                                Swal.fire({
                                  icon: 'error',
                                  title: obj.msg,
                                });
                              }
                              
                            
                          }
      }else{
        Swal.fire({
          icon: 'error',
          title: 'Invalid Captcha\nPlease Try Again.',
        });
        createCaptcha();
      }
    }
  }
}


createCaptcha();