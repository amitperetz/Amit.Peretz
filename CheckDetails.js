function ValidateForm(formInput) {
    if (formInput.phoneNum.value == "") {
        alert('Phone is required.');
        formInput.Name.focus();
        return false;
    }
    if (formInput.mail.value == "") {
        alert('Email address is required.');
        formInput.mail.focus();
        return false;
    }
    if (formInput.mail.value.indexOf("@") < 1 || formInput.mail.value.indexOf(".") < 1) {
        alert('Please enter a valid email address.');
        formInput.mail.focus();
        return false;
    }
}