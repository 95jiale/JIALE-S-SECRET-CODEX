var countPoints = function (rings) {
    var count = 0
    var dict = {};

    for (let i = 0; i < rings.length - 1; i += 2) {
        // 0 2 4 6 8 10 ...
        // rings[i] -> color
        // rings[i+1] -> rod
        console.log(rings[i], rings[i + 1])

        // check if rod is used in the dictionary
        if (rings[i + 1] in dict == false) {
            // if its not used -> create a new set

            dict[rings[i + 1]] = new Set();
        }
        dict[rings[i + 1]].add(rings[i])
        //add the colour into the set number
    }
    for (let key in dict) {
        if (dict[key].size == 3) {
            count += 1
        }
    }
    console.log(count)
};

console.log(
    countPoints(rings = "B0B6G0R6R0R6G9"
    )
);