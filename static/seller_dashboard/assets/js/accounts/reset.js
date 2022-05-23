function CheckPassword() {
    var password_value = $("#password_id").val();
    var regex_var = /^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=])(?=\S+$).{8,}$/

    if (password_value){
			$("#password_label").text("");
			$("#password_id").removeClass('has-error');
			$("#password_id").addClass('has-success');
			return true;
		}
	else{
			$("#password_label").text("Please fill out this Field")
			$("#password_id").addClass('has-error');
			$("#password_id").removeClass('has-success');
		}  
}
// validations applying on password ends here

function Confirm_password() {
    var confirm_password_value = $("#conf_password").val();
    var regex_var = /^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=])(?=\S+$).{8,}$/
	var password_value = $("#password_id").val();

    if (confirm_password_value){
		if (confirm_password_value == password_value){
			$("#conf_password_label").text("");
			$("#conf_password").removeClass('has-error');
			$("#conf_password").addClass('has-success');
			return true;
		}
		else{
			$("#conf_password_label").text("Password is not matching")
			$("#conf_password").addClass('has-error');
			$("#conf_password").removeClass('has-success');
			return false;
		}
	}
	else{
		$("#conf_password_label").text("Please fill out this Field")
		$("#conf_password").addClass('has-error');
		$("#conf_password").removeClass('has-success');
		return false;
		} 
}
// validations applying on confirm password ends here

function EmailCheck() {
    var confirm_password_value = $("#email").val()
    if (confirm_password_value){
    	if(confirm_password_value.length <= 3 || confirm_password_value.length >150){
			$("#email").addClass('has-error');
			$("#email").removeClass('has-success');
			$("#email_label").text("Invalid email")
			return false;
		}

		else{
			$("#email_label").text("");
			$("#email").removeClass('has-error');
			$("#email").addClass('has-success');

			return true;
		}
	}
	else{

		$("#email_label").text("Please fill out this Field")
		$("#email").addClass('has-error');
		$("#email").removeClass('has-success');
		}  
	}
// validations applying on otpcheck ends here

function UserCheck() {
    var confirm_password_value = $("#username").val()
    if (confirm_password_value){
    	if(confirm_password_value.length <= 3 || confirm_password_value.length >150){
			$("#username").addClass('has-error');
			$("#username").removeClass('has-success');
			$("#username_label").text("Invalid username")
			return false;
		}

		else{
			$("#username_label").text("");
			$("#username").removeClass('has-error');
			$("#username").addClass('has-success');

			return true;
		}
	}
	else{

		$("#username_label").text("Please fill out this Field")
		$("#username").addClass('has-error');
		$("#username").removeClass('has-success');
		}  
	}
// validations applying on otpcheck ends here

function FullName() {
    var confirm_password_value = $("#name").val()
    if (confirm_password_value){
    	if(confirm_password_value.length <= 3 || confirm_password_value.length >150){
			$("#name").addClass('has-error');
			$("#name").removeClass('has-success');
			$("#full_name_label").text("Invalid name")
			return false;
		}

		else{
			$("#full_name_label").text("");
			$("#name").removeClass('has-error');
			$("#name").addClass('has-success');

			return true;
		}
	}
	else{

		$("#full_name_label").text("Please fill out this Field")
		$("#name").addClass('has-error');
		$("#name").removeClass('has-success');
		}  
	}
// validations applying on otpcheck ends here




function role_name_exact() {
    var confirm_password_value = $("#role_instance").val()
    if (confirm_password_value){
		$("#role_name_label").text("");
		$("#role_instance").removeClass('has-error');
		$("#role_instance").addClass('has-success');
		return true;
		}
	else{

		$("#role_name_label").text("Please fill out this Field")
		$("#role_instance").addClass('has-error');
		$("#role_instance").removeClass('has-success');
		return false;
		}  
	}
// validations applying on otpcheck ends here



$(document).on('submit', '#reset_PasswordForm', function(){
	if (CheckPassword() && Confirm_password() && EmailCheck() && UserCheck() && FullName() && role_name_exact() && FullName()== true){
		return true;
	}
	else{
		CheckPassword(); 
		Confirm_password();
		UserCheck();
		EmailCheck();
		FullName();
		role_name_exact();
		FullName();

		return false;
	}
})


function show() {
    var x = document.getElementById("password_id");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}


function show1() {
    var x = document.getElementById("conf_password");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}
