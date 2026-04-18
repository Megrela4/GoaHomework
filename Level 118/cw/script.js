// შეასრულეთ იგივე დავალება დარჩენილ მეთოდებზე:

// findIndex, some, every

// findIndex
const newFindIndex = (arr, callback) => {
    for(let i = 0; i < arr.length; i ++) {
        if (callback(arr[i], i, arr)) {
            return i
        }
    }
    return -1
}

const numbers = [5, 12, 8, 130, 44];

const result1 = newFindIndex(numbers, (num) => {
    return num > 10;
});

console.log(result1);




