var truncateSentence = function (s, k) {
    let theArray = []
    splitSentence = s.split(" ")
    console.log(splitSentence)
    for (let i = 0; i < k; i++) {
        theArray.push(splitSentence[i])
    }
    console.log(theArray.join(" "))
};












console.log
    (truncateSentence(s = "What is the solution to this problem", k = 4))