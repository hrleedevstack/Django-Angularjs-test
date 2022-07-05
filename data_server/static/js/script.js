(function(angular) {
  'use strict';
  var app = angular.module('buttonTest', ['ui.bootstrap']);
  
  app.controller('buttonCtr', ['$scope', '$uibModal', function($scope, $uibModal){
    $scope.counter = 0;
    $scope.count = function(){
      $scope.counter+=1;
    };
    $scope.showAddPopup = function(){
      var modalInstance = $uibModal.open({
        templateUrl: "popup.html",
        controller: "popupCtr",
        size: '',
      });

      modalInstance.result.then(function(response){
        alert("response test, data added (id: " + response.data.id + ")");
        $scope.result = response.data;
      })
      console.log(response.data.id);
    };
  }]);

  app.controller('popupCtr', ['$scope', '$http', function($scope, $http, ){
    $scope.submit = function(data){
      // console.log(data);
      $http.post('/api/v1/data/', data).then(function(response){
        // console.log(response);
        // $uibModalInstance.close(response);
        $scope.$close(response);
      });
    };
    $scope.dismiss = function(){
      $scope.$dismiss();
    };
  }]);
  
  app.controller('tableCtr', ['$scope', function($scope, ){
    $scope.elem  = angular.element('tr')
  }])
})(window.angular);