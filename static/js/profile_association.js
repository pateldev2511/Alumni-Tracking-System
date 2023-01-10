function readURL(input) {
    if (input.files && input.files[0]) {
      var reader = new FileReader();
      
      reader.onload = function(e) {
        $('#p_img').attr('src', e.target.result);
      }
      
      reader.readAsDataURL(input.files[0]);
    }
  }
  
  $("#file1").change(function() {
    readURL(this);
  });
  
  
  function open_tab_e(x)
  {
      var tabs = ['t1','t2','t3','t4','t5']
      var t = 0;
      var tab = "";
      if(x == 1)
      {
          document.getElementById("content_container").innerHTML = document.getElementById('personal_details_container').innerHTML;
          t = 1;
          tab = tabs[0];
      }
      else if(x == 2)
      {
          document.getElementById("content_container").innerHTML = document.getElementById('account_details_container').innerHTML;
          t = 2;
          tab = tabs[1];
      }
      else if(x == 3)
      {
          document.getElementById("content_container").innerHTML = document.getElementById('contact_details_container').innerHTML;
          t = 3;
          tab = tabs[2];
      }
      else if(x == 4)
      {
          document.getElementById("content_container").innerHTML = document.getElementById('my_products_container').innerHTML;
          t = 4;
          tab = tabs[3];
      }
      else if(x == 5)
      {
          document.getElementById("content_container").innerHTML = document.getElementById('settings_container').innerHTML;
          t = 5;
          tab = tabs[4];
      }
      for(var i=1;i<=tabs.length;i++)
      {
              if(i == t)
              {
                  document.getElementById(tab).classList.add("active");
              }
              else {
                  document.getElementById(tabs[i-1]).classList.remove("active");
              }
      }
  }
  open_tab_e(1);
  
  function change_gender(x)
  {
      document.getElementById('gender').value = x;
      if(x==1 || document.getElementById('gender').value == "Male")
      {
          document.getElementById('MaleCB').click();
      }
      if(x==2 || document.getElementById('gender').value == "Female")
      {
          document.getElementById('FemaleCB').click();
      }
  }
  change_gender(document.getElementById('gender').value);
  
    $(document).ready(function() {
        
      var autoplaySlider = $('#lightSlider').lightSlider({
          item:2,
          controls:true,
          speed:1000,
          pause:3000,
          auto:true,
          loop:true,
          pauseOnHover: true,
          onBeforeSlide: function (el) {
              $('#current').text(el.getCurrentSlideCount());
          } 
      });
  
      $('#total').text(autoplaySlider.getTotalSlideCount()); 
      var autoplaySlider2 = $('#lightSlider2').lightSlider({
          item:2,
          controls:true,
          speed:1000,
          pause:3000,
          auto:true,
          loop:true,
          pauseOnHover: true,
          onBeforeSlide: function (el) {
              $('#current').text(el.getCurrentSlideCount());
          } 
      });
  
      $('#total').text(autoplaySlider.getTotalSlideCount()); 
      }); 
      
            
  
          function click_left(ind)
      {
          var x = document.getElementsByClassName('lSPrev');
          x[ind].click();
      }
      function click_right(ind)
      {
          var x = document.getElementsByClassName('lSNext');
          x[ind].click();   
      }
  
  