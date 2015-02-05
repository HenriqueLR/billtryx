(function (angular) {
    'use strict';

    var app = angular.module('Controller', ['Service']);

    app.controller('Ctrl', ['$scope', 'Service',

        function ($scope, Service) {

            var handleError = function (fix) {
                console.log('error', fix);
            };
            
            $scope.page = 1;
            
            var listShots = function () {
                Service.getShots($scope.page, function (fix) {
                    $scope.shots = fix;
                },
                handleError);
            };

            $scope.getListShots = listShots;

            listShots();
        }
    ]);

})(angular);