function ageConvert(date) {

    var dob = []
    dob = date.split("-");
    var today = new Date();
    var age = today.getFullYear() - dob[0];
    if (today.getMonth() < dob[1] || (today.getMonth() == dob[1] && today.getDate() < dob[3])) {
        age--;
    }
    console.log(age);

}

ageConvert("1999-07-08");