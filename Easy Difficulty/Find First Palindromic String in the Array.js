var firstPalindrome = function (words) {
    for (i = 0; i < words.length; i++) {
        if (words[i] == words[i].split("").reverse().join("")) {
            return words[i]
        }
    }
    return ""
};


console.log(
    firstPalindrome(words = ["def", "ghi"]
    )
);