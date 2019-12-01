function hourMin(num) {
    if (num < 60) {
        console.log("0 :", num);
    }
    else {
        var hours = num / 60;
        var mins = num % 60;
        console.log(String(parseInt(hours) + ' : ' + mins));
    }
}

hourMin(145);