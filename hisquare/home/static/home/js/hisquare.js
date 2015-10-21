(function(){

    var app = angular.module(
        'hisquareApp', 
        ['ngAnimate', 'ui.bootstrap', 'ngResource', 'ngRoute', 
         'angularModalService', 'ngTouch', 'ngSanitize']
    );
    
    app.config(
        function($interpolateProvider, $routeProvider, $sceDelegateProvider) {
            $interpolateProvider.startSymbol('{$');
            $interpolateProvider.endSymbol('$}');
            
            // Routes
            $routeProvider
                // Events route
                .when('/events', {
                    templateUrl: '/pages/events',
                    controller: 'eventsController as events',
                    activeTab: 'events',
                    resolve: {
                        eventData: function (getService) {
                            getService.setUrl('/get/events/');
                            return getService.getData()
                                .then(function(response){
                                    return response.data;
                                });
                        }
                    }
                })
                .when('/about', {
                    templateUrl: '/pages/about',
                    controller: 'aboutController as a',
                    activeTab: 'about',
                    resolve: {
                        aboutPage: function (getService) {
                            getService.setUrl('/get/about/');
                            return sendGetRequest(getService);
                        }
                    }
                })
                .when('/merchants/:category', {
                    templateUrl: '/pages/merchants',
                    controller: 'merchantsController as merch',
                    resolve: {
                        merchantData: function ($route, getService) {
                            var catName = $route.current.params.category;
                            getService.setUrl('/get/merchants/' + catName);
                            return sendGetRequest(getService);
                        }
                    }
                })
                .otherwise({
                    redirectTo: "/"
                });
            
            $sceDelegateProvider.resourceUrlWhitelist([
                // Allow same origin resource loads.
                'self',
                // Allow loading from our assets domain.  Notice the difference between * and **.
                'https://www.google.com/maps/**']);
        });
    
    // Get all categories    
    app.controller('catsController', ['$resource', function($resource) {
    	this.categories = getData($resource, "/get/categories/", true);
    	
    	this.setActiveTab = function (name) {
    	    this.activeTab = name;
    	};
    }]);
    
    // Events page
    app.controller('eventsController', ['$rootScope', 'eventData', '$location', '$anchorScroll', '$route', 
    function($rootScope, eventData, $location, $anchorScroll, $route) {    
        $rootScope.$route = $route;
        
        this.events = eventData;
        this.harvestFestivalAnchor = '';
        this.streetFairAnchor = '';

        this.linkTo = function(lid) {
            $location.hash(lid);
            $anchorScroll();
        };
        
        
        this.harvestFestivalExists = function(){
            var e = angular.fromJson(angular.toJson(this.events));
            e.futureEvents.forEach(function (event) {
                if (event.title.toLowerCase().indexOf("harvest festival") > -1) {
                    this.harvestFestivalAnchor = event.concat;
                    return true;
                }
            });
        };
        
        this.streetFairExists = function(){
            var e = angular.fromJson(this.events);
            e.forEach(function (event) {
                if (event.title.toLowerCase().indexOf("street fair") > -1) {
                    this.streetFairAnchor = event.concat;
                    return true;
                }
            });
        };
    }]);
    
    // About page
    app.controller('aboutController', ['$rootScope', '$route', 'aboutPage', 
    function ($rootScope, $route, aboutPage) {
        $rootScope.$route = $route;
        
        // GET about page content
        if (aboutPage.text) {
            this.about = aboutPage;  
        } else { 
            if (aboutPage.error) {
                console.log(aboutPage.error);
            } else {
                console.log(aboutPage);
            }
        } 
    }]);
    
    
    // Merchant page
    app.controller('merchantsController', ['$scope', '$resource', '$routeParams', '$modal', 'merchantData', 
    function ($scope, $resource, $routeParams, $modal, merchantData) {
        this.query = '';
        // load custom filter method
        // $scope.$on('$viewContentLoaded', filterMerchantList);
        
        // Set active tab
        this.activeMerch = '';
        this.setActiveMerch = function (m) {
            this.activeMerch = m;
        };
        
        this.clearSearch = function (event) {
            console.log(event.keyCode);
            if (event.keyCode == 27) {
                this.query = '';
            } 
        };

        // var categoryName = $routeParams.category;

        // Get all merchants
        // console.log('getting merchants');
        // this.merchants = getData($resource, "get/merchants/" + categoryName, false);
        if (merchantData.merchants) {
            this.merchants = merchantData;  
        } else { 
            if (merchantData.error) {
                console.log(merchantData.error);
            } else {
                console.log(merchantData);
            }
        } 
        
        
        // define modal instance stuff
        this.myInterval = 8000;
        this.noWrapSlides = false;
        this.animationsEnabled = true;
        this.open = function(m) {
            $scope.curMer = m;
            $modal.open({
                animation: this.animationsEnabled,
                templateUrl: '/pages/details',
                scope: $scope,
                controller: 'modalInstanceController',
                size: 'lg'
            }).result.then(function () { /* do nothing */ });
        };
        
        // Turn on or off animation
        this.toggleAnimation = function () {
            this.animationsEnabled = !this.animationsEnabled;
        };  
    }]);

    // Modal controller
    app.controller('modalInstanceController', ['$scope', '$modalInstance', 
    function($scope, $modalInstance) {
        // $scope.curMer = mrch;
        $scope.close = function () {
            $modalInstance.dismiss('cancel');
        };
    }]);
    
    
    app.service('getService', ['$http', '$q', function ($http, $q) {
        var _url = '';
        
        this.setUrl = function (url) {
            _url = url;
        };
        
        this.getUrl = function () {
            return _url;
        };
        
        this.getData = function () {
            var deferred = $q.defer();
            $http({
                method: 'GET',
                url: _url
            }).then(function(data){
                deferred.resolve(data);
            }).catch(function(reason){
                deferred.reject(reason);
            });
            
            return deferred.promise;
            
        };
        
    }]);
    
    function sendGetRequest(getService){
        // Abstract the promise checking 
        return getService.getData()
            .then(function (response) {
                return response.data;
            })
            .catch(function (reason){
                var err = reason.status + ' ' + reason.statusText + ' at ' + getService.getUrl();
                return {"error": err};
            });
    }
    
    // Use ngResource to to GET requests for either JSON Arrays or Objects.
    function getData($resource, url, isArray){
        // Almost depricated!
        var resource = $resource(url);
        
        if (!isArray){
            var response = resource.get(
                function (data) { 
    	            return JSON.stringify(data);
    	    });
        } else {
            if (isArray){
                var response = resource.query(
                    function (data) {
                        return JSON.stringify(data);
                    });
            }
        }
        
	    
	    return response;
    }
    
    // // Find JSON element by value rather than key
    // function findElement(arr, propName, propValue) {
    //     for (var i=0; i < arr.length; i++) {
    //         if (arr[i][propName] == propValue) {
    //             return arr[i];    
    //         }
    //     }
    // }

})();


// Custom jQuery and js functions:
function filterMerchantList () {

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
}