(function (angular) {
    'use strict';


    var app = angular.module('Service', [], function ($httpProvider) {
        $httpProvider.interceptors.push('Auth');
    });

    app.service('Service', ['$http',

        function ($http) {

            var API = 'https://api.dribbble.com/v1';
            
            this.getShots = function (page, success, error) {
                $http.get(API + '/shots/?page=' + page).success(success).error(error);
            };            
        }
    ]);

    app.factory('Auth', function () {
        return {
            request: function (config) {
                var token = '2dc2be1047838f60217de89cae3d25ce348f20f5418e3db9d73214f18e49ff14';
                config.headers = config.headers || {};
                config.headers.Authorization = 'Bearer ' + token;
                return config;
            }
        }
    });


})(angular);