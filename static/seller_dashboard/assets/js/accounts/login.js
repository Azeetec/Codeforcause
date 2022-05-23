// validations applying on Email_valid_check
function Email_valid_check(){
    var letternumber = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

	var email_value = $("#email_reg").val()
	if (email_value){
		if (email_value.match(letternumber)){
			$("#email_check_label").text("")
			$("#email_reg").removeClass('has-error')
			$("#email_reg").addClass("has-success")
			return true;
		}
		else{
		$("#email_check_label").text("Please enter valid email address")
		$("#email_reg").addClass('has-error')
		$("#email_reg").removeClass("has-success")
		return false;
		}

	}
	else{
		$("#email_check_label").text("Please fill out this Field")
		$("#email_reg").addClass('has-error')
		$("#email_reg").removeClass("has-success")
		return false;
	}

}
// validations applying on Email_valid_check ends here

// validations applying on password_label
function Password_Register() {
    password_value = $("#registerPassword").val();
    if (password_value){
			$("#password_label").text("")
			$("#registerPassword").removeClass('has-error');
			$("#registerPassword").addClass('has-success');
			return true;
		}
    else {
        $("#password_label").text("Please fill out this Field")
        $("#registerPassword").addClass('has-error');
        $("#registerPassword").removeClass('has-success');

        return false;
    }
}

// validations applying on password_label ends here


$(document).on('submit', '#loginform', function(){
	if (Email_valid_check() && Password_Register() == true){
		return true;
	}
	else{
		Email_valid_check();
		Password_Register();
		return false;
	}

})


function show() {
    var x = document.getElementById("registerPassword");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}





// making function here for remember me functionality
function remember_me_hit_while_submitting() {
    var checkbox_value = $("#remember_me");
    if (checkbox_value.is(":checked")) {
        var usename_val = $('#email_reg').val(); //VALUE OF USERNAME
        var password_val = $('#registerPassword').val(); //VALUE OF PASSWORD

        console.log("password_val is ----->", password_val)

        localStorage.setItem('email_reg', usename_val); //SETTING VALUE IN LOCAL STORAGE
        localStorage.setItem('registerPassword', password_val); //SETTING VALUE IN LOCAL STORAGE
    } else {
        localStorage.setItem('email_reg', ''); //SETTING VALUE IN LOCAL STORAGE i.e None
        localStorage.setItem('email_reg', ''); //SETTING VALUE IN LOCAL STORAGE i.e None
    }
}
// ends here making function here for remember me functionality

//NEXT PAGE LOAD, THE USERNAME & PASSWORD WILL BE SHOWN IN THEIR FIELDS
$(document).ready(function(){
    var usename_val = localStorage.getItem("email_reg"); //"USERNAME" COOKIE
    var password_val = localStorage.getItem("registerPassword"); //"PASSWORD" COOKIE

    $("#email_reg").val(usename_val); //FILLS WITH "USERNAME" COOKIE
    $("#registerPassword").val(password_val); //FILLS WITH "PASSWORD" COOKIE
})