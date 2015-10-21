console.log('i am here');

// Search feature
var foundmessage = $("#shopsfound"),
    filterInput = $('#filter'),
    merchantSelector = $('#shop-list > div > div');

function filterShops(selector, query) {
    query =   $.trim(query); //trim white space
    // query = query.replace(/ /gi, '|'); //add OR for regex query REMOVED BECAUSE I DON'T REALLY WANT AN OR SEARCH

    $(selector).each(function() {
        var self = $(this);
        (self.text().search(new RegExp(query, "i")) < 0) 
            ? 
            self
                .hide().removeClass('visible') : 
            self
                .show()
                .addClass('visible');
    });
}

// On keyup inside search box, callback will initiate search function
filterInput.keyup(function (event) {
    var self = $(this);
    console.log('keyup:' + event.keyCode);
    //if esc is pressed or nothing is entered
    if (event.keyCode == 27 || self.val() == '') {
        //if esc is pressed we want to clear the value of search box
        self.val('');

        // we want each row to be visible because if nothing
        // is entered then all rows are matched.
        merchantSelector
            .removeClass('visible')
            .show()
            .addClass('visible');
        foundmessage.hide();
        
    } else {
        // If there is text filter
        // Find shop items and pass their value to the filterShops function
        filterShops('#shop-list > div > div', self.val());
        
        // Display number of shops found
        var numfound = $("#shop-list > div > div:visible").length,
            foundtext;
        if (numfound === 1) {
            foundtext = " shop found";
        } else { foundtext = " shops found" }
        
        foundmessage
            .show()
            .text(numfound + foundtext);
    }
});