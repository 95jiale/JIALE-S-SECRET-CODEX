var targetIndices = function (nums, target) {
    nums = nums.sort(function (a, b) {
        return a - b
    })
    let theArray = []
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] == target) {
            theArray.push(i)
        }
    }

    console.log(theArray)
};




console.log(
    targetIndices(nums = [1, 2, 5, 2, 3], target = 5
    )
);