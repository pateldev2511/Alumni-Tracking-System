//  alert();
  $(document).ready(function() {
    $(".level-0-li").addClass("fade-in"); 
    });

  $(document).ready(function(){ 
    var touch 	= $('#resp-menu');
    var menu 	= $('.menu');
   
    $(touch).on('click', function(e) {
      e.preventDefault();
      menu.slideToggle();
    });
    
    $(window).resize(function(){
      var w = $(window).width();
      if(w > 767 && menu.is(':hidden')) {
        menu.removeAttr('style');
      }
    });
    
  });

  

  $(document).ready(function() {
    $('.main-slider-container').lightSlider({
      item: 1,
      controls: true,
      speed: 1000,
      pause: 3000,
      auto: true,
      loop: true,
      pauseOnHover: true,
        onSliderLoad: function() {
            $('#slider-container').removeClass('main-slider-container');
        } 
    });  
  });
  $(document).ready(function() {
    $('.events-slider').lightSlider({
      item: 3,
      controls: true,
      speed: 1000,
      pause: 3000,
      auto: true,
      loop: true,
      pauseOnHover: true,
        onSliderLoad: function() {
            $('.events-slider').removeClass('.events-slider');
        } 
    });  
  });
  $(document).ready(function() {
    $('.notable-alumni-slider').lightSlider({
      item: 4,
      controls: true,
      speed: 1000,
      pause: 3000,
      auto: true,
      loop: true,
      pauseOnHover: true,
        onSliderLoad: function() {
            $('.notable-alumni-slider').removeClass('.notable-alumni-slider');
        } 
    });  
  });
  // Fund Raising Slider
  
  $(document).ready(function() {
    $('.fund-raising-slider').lightSlider({
      item: 4,
      controls: true,
      speed: 1000,
      pause: 3000,
      auto: true,
      loop: true,
      pauseOnHover: true,
        onSliderLoad: function() {
            $('.fund-raising-slider').removeClass('.fund-raising-slider');
        } 
    });  
  });

  // News & Notices Tab JS
  var TabBlock = {
    s: {
      animLen: 200
    },
    
    init: function() {
      TabBlock.bindUIActions();
      TabBlock.hideInactive();
    },
    
    bindUIActions: function() {
      $('.tabBlock-tabs').on('click', '.tabBlock-tab', function(){
        TabBlock.switchTab($(this));
      });
    },
    
    hideInactive: function() {
      var $tabBlocks = $('.tabBlock');
      
      $tabBlocks.each(function(i) {
        var 
          $tabBlock = $($tabBlocks[i]),
          $panes = $tabBlock.find('.tabBlock-pane'),
          $activeTab = $tabBlock.find('.tabBlock-tab.is-active');
        
        $panes.hide();
        $($panes[$activeTab.index()]).show();
      });
    },
    
    switchTab: function($tab) {
      var $context = $tab.closest('.tabBlock');
      
      if (!$tab.hasClass('is-active')) {
        $tab.siblings().removeClass('is-active');
        $tab.addClass('is-active');
     
        TabBlock.showPane($tab.index(), $context);
      }
     },
    
    showPane: function(i, $context) {
      var $panes = $context.find('.tabBlock-pane');
     
      // Normally I'd frown at using jQuery over CSS animations, but we can't transition between unspecified variable heights, right? If you know a better way, I'd love a read it in the comments or on Twitter @johndjameson
      $panes.slideUp(TabBlock.s.animLen);
      $($panes[i]).slideDown(TabBlock.s.animLen);
    }
  };
  
  $(function() {
    TabBlock.init();
  });

    /* Demo purposes only */
$(".hover").mouseleave(
function () {
$(this).removeClass("hover");
}
);


// Success Stories JS

var	testim = document.getElementById("testim"),
testimDots = Array.prototype.slice.call(document.getElementById("testim-dots").children),
testimContent = Array.prototype.slice.call(document.getElementById("testim-content").children),
testimLeftArrow = document.getElementById("left-arrow"),
testimRightArrow = document.getElementById("right-arrow"),
testimSpeed = 4500,
currentSlide = 0,
currentActive = 0,
testimTimer,
touchStartPos,
touchEndPos,
touchPosDiff,
ignoreTouch = 30;
;

window.onload = function() {

// Testim Script
function playSlide(slide) {
  for (var k = 0; k < testimDots.length; k++) {
      testimContent[k].classList.remove("active");
      testimContent[k].classList.remove("inactive");
      testimDots[k].classList.remove("active");
  }

  if (slide < 0) {
      slide = currentSlide = testimContent.length-1;
  }

  if (slide > testimContent.length - 1) {
      slide = currentSlide = 0;
  }

  if (currentActive != currentSlide) {
      testimContent[currentActive].classList.add("inactive");            
  }
  testimContent[slide].classList.add("active");
  testimDots[slide].classList.add("active");

  currentActive = currentSlide;

  clearTimeout(testimTimer);
  testimTimer = setTimeout(function() {
      playSlide(currentSlide += 1);
  }, testimSpeed)
}

testimLeftArrow.addEventListener("click", function() {
  playSlide(currentSlide -= 1);
})

testimRightArrow.addEventListener("click", function() {
  playSlide(currentSlide += 1);
})    

for (var l = 0; l < testimDots.length; l++) {
  testimDots[l].addEventListener("click", function() {
      playSlide(currentSlide = testimDots.indexOf(this));
  })
}

playSlide(currentSlide);

// keyboard shortcuts
document.addEventListener("keyup", function(e) {
  switch (e.keyCode) {
      case 37:
          testimLeftArrow.click();
          break;
          
      case 39:
          testimRightArrow.click();
          break;

      case 39:
          testimRightArrow.click();
          break;

      default:
          break;
  }
})

testim.addEventListener("touchstart", function(e) {
  touchStartPos = e.changedTouches[0].clientX;
})

testim.addEventListener("touchend", function(e) {
  touchEndPos = e.changedTouches[0].clientX;

  touchPosDiff = touchStartPos - touchEndPos;




  if (touchPosDiff > 0 + ignoreTouch) {
      testimLeftArrow.click();
  } else if (touchPosDiff < 0 - ignoreTouch) {
      testimRightArrow.click();
  } else {
    return;
  }

})
}
