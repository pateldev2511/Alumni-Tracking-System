var f_name = "";
var l_name = "";
var email = "";
var country = "";
var country_code = "";
var mobile_no = "";
var password = "";
var c_password = "";
function initialize_form() {
  document.getElementById('form-part-1').style.display = "block";
}

function next_btn(x,y) {


  if(x == "form-part-1" && y == "form-part-2")
  {
    // alert();
    var regName = /^[a-zA-Z]+$/;
    f_name = document.getElementById('first_name').value;
    if(!regName.test(f_name)){
      document.getElementById('first_name').focus();
      Swal.fire({
        icon: 'error',
        title: 'Please Enter Valid First Name.',
      });
    }
    else{
      l_name = document.getElementById('last_name').value;
      if(!regName.test(l_name)){
        document.getElementById('last_name').focus();
        Swal.fire({
          icon: 'error',
          title: 'Please Enter Valid Last Name.',
        });
      }
      else{
        var regName = /^[A-Z0-9._%+-]+@([A-Z0-9-]+\.)+[A-Z]{2,6}$/i;
        email = document.getElementById('email').value;
        if(!regName.test(email)){
          document.getElementById('email').focus();
          Swal.fire({
            icon: 'error',
            title: 'Please Enter Valid Email Address.',
          });
        }
        else {
          country = document.getElementById('country').value;
          country_code = document.getElementById('country_code').value;
          if(country == "" || country.length == 0){
            document.getElementById('mobile_number').focus();
            Swal.fire({
              icon: 'error',
              title: 'Please Select Valid Country.',
            });
          }
          else {
            var regName = /^[0-9]{9,12}$/i;
            mobile_no = document.getElementById('mobile_number').value;
            if(!regName.test(mobile_no)){
              document.getElementById('mobile_number').focus();
              Swal.fire({
                icon: 'error',
                title: 'Please Enter Valid Mobile Number.',
              });
            }
            else {
              var regName = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,20}$/;
              password = document.getElementById('password').value;
              if(!regName.test(password)){
                document.getElementById('password').focus();
                Swal.fire({
                  icon: 'error',
                  title: 'Please Enter Valid Passoword.',
                });
              }
              else {
                c_password = document.getElementById('c_password').value;
                if(password != c_password)
                {
                  Swal.fire({
                    icon: 'error',
                    title: 'Both Password Doesn\'t Match.',
                  });
                }
                else {
                      document.getElementById(x).style.display = "none";
                      document.getElementById(y).style.display = "block";
                }
              }
            } 
          }
        }    
      }  
    }

  }
  

//   first_name
// last_name
// email
// country
// country_code
// mobile_number
// password
// c_password

// mv-form-2-btn

}

// college
// degree
// enrollment_no
// enter_year
// passout_year
// grecaptcha.getResponse(widgetId1)
// box-1

function signup()
{
  var regName = /^[a-zA-Z]+$/;
    var college = document.getElementById('college').value;
    if(college == "" || college.length == 0){
      document.getElementById('college').focus();
      Swal.fire({
        icon: 'error',
        title: 'Please Select College.',
      });
    }
    else {
      var degree = document.getElementById('degree').value;
      if(degree == "" || degree.length == 0){
        document.getElementById('degree').focus();
        Swal.fire({
          icon: 'error',
          title: 'Please Select Degree.',
        });
      }
      else {
        regName = /^[0-9]{6,15}$/;
        var enrollment_no = document.getElementById('enrollment_no').value;
        if(!regName.test(enrollment_no)){
          document.getElementById('enrollment_no').focus();
          Swal.fire({
            icon: 'error',
            title: 'Please Enter Valid Enrollment Nunber.',
          });
        }
        else {

          var d = new Date();
          var year = d.getFullYear();
          // alert(year);
          regName = /^[0-9]{4}$/;
          var e_year = document.getElementById('enter_year').value;
          
          if(e_year < 2000 || e_year > year)
          {
            document.getElementById('enter_year').focus();
            Swal.fire({
              icon: 'error',
              title: 'Please Enter Valid Entry Year.',
            });
          }
          else {
            var p_year = document.getElementById('passout_year').value;
            if(p_year < 2000 || p_year > (year+6))
            {
              document.getElementById('passout_year').focus();
              Swal.fire({
                icon: 'error',
                title: 'Please Enter Valid Passout Year.',
              });
            }
            else {
                if(p_year < e_year)
                {
                  document.getElementById('passout_year').focus();
                  Swal.fire({
                    icon: 'error',
                    title: 'Passout Year Must Be Less Than Entry Year.',
                  });
                }
                else {
                  var res = grecaptcha.getResponse(widgetId1);
                  // var r = document.getElementById('recaptcha-anchor').
                  if(res == "" || res.length == 0)
                  {
                    // document.getElementsByClassName('recaptcha-checkbox-border')[0].focus();
                    Swal.fire({
                    icon: 'error',
                    title: 'Please Solve reCaptcha.',
                  }); 
                  }
                  else {
                    if(!document.getElementById('box-1').checked)
                    {
                      document.getElementById('box-1').focus();
                      Swal.fire({
                        icon: 'error',
                        title: 'Please Accept Terms and Conditions as well as the Privacy Policy.',
                      });
                    }
                    else {
                      document.getElementById('loader_container').style.display = "block";
                      if(document.getElementById('loader_container').style.display == "block")
                      {

                        var x = setInterval(function()
                        {
                          var xmlhttp = new XMLHttpRequest();
                          xmlhttp.open("GET", "/alumni/signup?mode=1&f_name=" +f_name+"&l_name="+l_name+"&email="+email+"&country_code="+country_code.toString()+"&mobile_number="+mobile_no.toString()+"&password="+password+"&college="+college+"&degree="+degree+"&enrollment_number="+enrollment_no.toString()+"&entry_year="+e_year.toString()+"&passout_year="+p_year.toString(), false);
                          xmlhttp.send(null);
                          var res = xmlhttp.responseText;
                          var obj = JSON.parse(res);
                        
                          if(obj.res == 1)
                          {
                            document.getElementById('loader_container').style.display = "none";
                            window.location = "/alumni/welcome_email";
                          }
                          else {
                            document.getElementById('loader_container').style.display = "none";
                            Swal.fire({
                              icon: 'error',
                              title: obj.msg,
                            });
                          }
                          clearInterval(x);
                        },1000);
                        
                      }
                    }
                  }    
                }
            }
          }
        }
      }
    }
}

function prev_btn(x,y)
{
  document.getElementById(x).style.display = "none";
  document.getElementById(y).style.display = "block";
}


function change_college(x)
{
    v = x;
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/alumni/signup?mode=3&v=" +v, false);
    xmlhttp.send(null);
    var res = xmlhttp.responseText;
    var obj = JSON.parse(res);
    // alert(obj.degrees);
    var code = "";
    for (var i = 0; i < obj.degrees.length; i++) {
      code += "<option value='" + obj.degrees[i] + "'>" + obj.degrees[i] + "</option>"
    }
    document.getElementById('degree').innerHTML = code;
}
change_college(1);

function change_country(x)
{
    v = x;
    // alert(v);
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/alumni/signup?mode=2&v=" +v, false);
    xmlhttp.send(null);
    var res = xmlhttp.responseText;
    // alert(res)
    document.getElementById('country_code').value = "+"+res;
}
change_country("India");



