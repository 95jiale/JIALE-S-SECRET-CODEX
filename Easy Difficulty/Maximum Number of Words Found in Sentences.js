var mostWordsFound = function (sentences) {
    let maxNumberOfWord = 0
    for (let i = 0; i < sentences.length; i++) {
        splitSentences = sentences[i].split(" ")
        console.log(splitSentences)
        wordCount = splitSentences.length
        if (wordCount > maxNumberOfWord) {
            maxNumberOfWord = wordCount
        }
    }
    return maxNumberOfWord
};











console.log(
    mostWordsFound([
        "please wait", "continue to fight", "continue to win",
    ])
);