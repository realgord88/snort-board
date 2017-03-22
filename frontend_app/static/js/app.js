var app = angular.module('app', []);

app.controller('status', function QuestionController($scope, $http){
	$scope.status = 'Off';
	$scope.changestatus = function (text){
	
	$http.get('api/changestatus').success(function(data) {
        $scope.status=data.status;
        });
	};
});