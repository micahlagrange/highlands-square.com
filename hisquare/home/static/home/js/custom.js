// // IIFE - Immediately Invoked Function Expression
// (function(yourcode) {
// 	// // Pre IIFE
    
//     // The global jQuery object is passed as a parameter
//     yourcode(window.jQuery, window, document);
//     }(function($, window, document) { 
//     	/* The $ is now locally scoped. Listen for the jQuery ready event on the document */
//         $(function() { /* The DOM is ready!*/ });
//         // The rest of the code goes here!
        
        // Define some variables
        var jWindow = $(window),
            sidebar = $('#sidebar'),
            mobside = $('#sidebar-mobile'),
            catname = $('#getActiveTab').text();
            
        // Style active tab on click after 300 miliseconds
        setTimeout(function() {
            var selector = '#' + catname + '-tab';
            $(selector).addClass('active-sidebar-item')
            // When a tab is clicked set it to active
            // var tabs = $('#category-tabs > .list-group-item');
            // console.log(tabs);
            // tabs.click(function(){
            //     $('.active-sidebar-item').removeClass('active-sidebar-item');
            //     $(this).addClass('active-sidebar-item');
            // });
        }, 300);
        
        // No animations, load the sidebar on page load
        function swapSideBar(platform) {
            if (platform === 'mobile') {
                sidebar
                    .hide();
                mobside.show();
            } else {
                if (platform === 'desktop')  {
                    mobside.hide();
                    sidebar.show(function(){});
                    fixSidebarWidth();
                }
            }
        }
        // Animate swapping between mobile and Desktop menus
        function animateSidebarSwap(platform) {
            if (platform === 'mobile') {
                sidebar
                    .hide();
                mobside.show("slow");
            } else {
                if (platform === 'desktop')  {
                    mobside.hide(500);
                    sidebar.show("slow", function(){fixSidebarWidth()});
                }
            }
        }
        
        // Switch between mobile and desktop views
        function getNavBar() {
            if (jWindow.width() <= 767){
                swapSideBar('mobile');
                
            } 
            else {
                if (jWindow.width() >= 768){
                    swapSideBar('desktop');
                } 
            }
        }
        
        // Set the navbar to the current display size on page load
        getNavBar();
        
        // Bootstrap affix to make the sidebar stay at the top after scrolling down
        
        function fixSidebarWidth() {
            // function to fix the width of the sidebar
                sidebar.width(sidebar.parent().width());
            }
        
        // On page load
        fixSidebarWidth();

        function turnOnAffix() {
            // Code to do the affix stuff
            sidebar.affix({
                  offset: {
                    top: 400,
                    bottom: 200
                  }
            });
        }
        
        // On pageload
        turnOnAffix();
        
        
        // If window resized, fix sidebar width again, and check again 
        // to see if window is mobile sized, and turn off affix stuff.
        jWindow.resize(function() {
            fixSidebarWidth();
            if (jWindow.width() <= 767){
                animateSidebarSwap('mobile');
                
            } 
            else {
                if (jWindow.width() >= 768){
                    animateSidebarSwap('desktop');
                } 
            }
        });
        
        // Capture affix event
        sidebar
            .on( 'affixed.bs.affix', function () {
                fixSidebarWidth();
            })
            .on( 'affixed-top.bs.affix', function () {

                fixSidebarWidth();
            })
            .on( 'affixed-bottom.bs.affix', function () {
                fixSidebarWidth();
            });
// }));
        