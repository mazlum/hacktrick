var scanApp = angular.module('scanApp',[]).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

var scan_get = function ($scope, $http) {
      $http.get('/get-scans/').
      then(function(response) {
          $scope.scan_results = response.data;
      }, function(response) {
          console.log("err");
      });
    return $scope
}

scanApp.controller('TableController', ['$scope', '$http' ,'$interval', function($scope, $http, $interval) {
    $scope = scan_get($scope, $http);
    $interval(function() {
        $scope = scan_get($scope, $http);
    }, 2000);
}]);