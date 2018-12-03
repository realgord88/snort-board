
var app = angular.module('app', []);



app.controller('status', function QuestionController($scope, $http){
	$scope.status = 'Off';
	$scope.changestatus = function (text){
	
	$http.get('http://localhost:8000/api/changestatus').success(function() {
        
        });
	$scope.status='On';
	};
});


      app.controller('iptables', function($scope, $http) {
          $scope.addrule = function () {
              $scope.all_rule = $scope.name;
              var parameter = JSON.stringify({"rule": $scope.all_rule});
			    $http.post('http://0.0.0.0:8000/api/iptables/', parameter).
			    success(function(data, status, headers, config) {
			        
			        console.log(data);
			      }).
			      error(function(data, status, headers, config) {
			        $scope.status=config
			      });

    };  
}); 



app.controller('alertsget', function($scope, $http) {
    $http({
        method : "GET",
        url : "http://0.0.0.0:8000/api/alerts/"
    }).then(function getalert(response) {
        $scope.alerts = response.data;
    }, function myError(response) {

        $scope.alerts = response.statusText;
    });
});