$(function{

	var error_name = false;
	var error_pwd = false;

	$(#user_name).blur(function(){
		check_username(;)

	});

	$(#user_name).focus(function(){
		$(this).next()hide();

		function check_username(){
			var val = $(#user_name).val()
			var re = /^[a-z0-9_]{5,15}$/i;

			if(val==''){
			$('#user_name').next().html('用户名不能为空')
			$('#user_name').next().show()
			error_name = true;
			return;
			}

			if(re.test(val)){
				error_name = false;

			}
			else
			{
				error_name = true;

			}


		}



})