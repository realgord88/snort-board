var app = angular.module('app', []);

app.controller('status', function QuestionController($scope, $http){
	$scope.status = 'Off';
	$scope.changestatus = function (text){
	
	$http.get('localhost:8000/api/changestatus').success(function(data) {
        $scope.status=data;
        });
	};
});