"use strict";
$(document).ready(function() {
    /* -- Scrollspy -- */
    $(".documention-menu ul").scrollspy({ 
        offset: -80,
        animate: true
    });
    /* -- Back to Top -- */
	$(window).scroll(function(){
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn();
        } else {
            $('.back-to-top').fadeOut();
        }
    });
    $("body").on("click", ".back-to-top", function() {  
        $("html, body").animate({ scrollTop: 0 }, 1000);
        return false;
    });
    /* -- Popover  --*/
    $('[data-toggle="popover"]').popover();
    /* -- Tooltip --*/
    $('[data-toggle="tooltip"]').tooltip(); 
});