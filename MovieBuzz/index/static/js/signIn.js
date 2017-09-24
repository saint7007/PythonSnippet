//$(function(){
//	$('#btnSignIn1').click(function(){
//		var userName=$("#inputEmail").val();
//		var userPassword=$("#inputPassword").val();
//		$.ajax({
//			url: '/validateLogin?userName='+userName+'&userPassword='+userPassword,
//			data:  {
//                        "userName": userName,
//                        "userPassword": userPassword,
//                    },
//			type: 'POST',
//			success: function(response){
//				console.log(response);
//			},
//			error: function(error){
//				console.log(error);
//			}
//		});
//	});
//});


$(function(){
	$('#btnSignIn1').click(function(){

		$.ajax({
			url: '/validateLogin',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});