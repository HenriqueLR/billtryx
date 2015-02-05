(function (angular) {
    'use strict';

    var app = angular.module('Directives', ['Service']);

    app.directive('pagination', ['Service', function (Service) {
        return {
            template: '<div class="row"> \
                        <div class="col-md-4 col-md-offset-4"> \
                        <nav><ul class="pager"> \
                        <li><a ng-click="previous()" class="item" style="background-color:#6C5195;color:white;">&lt;&lt;</a></li> \
                        <a class="item">{{ page }}</a> \
                        <li><a style="background-color:#6C5195;color:white;" ng-click="next()">&gt;&gt;</a></li> \
                        </ul></nav></div></div>',

            link: function(scope, element, attrs) {
                scope.next = function () {
                    scope.page++;
                    scope.getListShots();
                };

                scope.previous = function () {
                    scope.page--;
                    if (scope.page < 1) {
                        scope.page = 1;
                    }
                    scope.getListShots();
                };

            }
        }
    }]);

})(angular);