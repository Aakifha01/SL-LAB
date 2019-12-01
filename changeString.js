function changeString(word) {
    var encrypt = '';
    for (var i = 0; i < word.length; i++) {
        if (word[i] == "z") {
            encrypt += "a";
        }
        else if (word[i] >= "a" && word[i] < "z") {

            encrypt += String.fromCharCode(word.charCodeAt(i) + 1);

        }
        else {
            encrypt += word[i];
        }

    }
    var newText = "";
    for (var i = 0; i < encrypt.length; i++) {

        if (encrypt[i] == "a" || encrypt[i] == "e" || encrypt[i] == "i" || encrypt[i] == "o" || encrypt[i] == "u") {

            newText += encrypt[i].toUpperCase();

        }
        else {
            newText += encrypt[i];
        }
    }
    console.log(newText);
}

changeString("hello*3");