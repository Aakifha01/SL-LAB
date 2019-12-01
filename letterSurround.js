function letterSurround(word) {
    if (word[0] >= 'a' && word[0] <= 'z' || (word[word.length - 1] >= "a" && word[word.length - 1] <= "z")) {
        console.log("False");
        return;
    }
    else {
        for (var i = 0; i < word.length; i++) {
            if (word[i] >= "a" && word[i] <= "z") {
                if (word[i - 1] != "+" || word[i + 1] != "+") {
                    console.log("False");
                    return;
                }
            }
        }
    }
    console.log("True");
}

letterSurround("+f++d+");