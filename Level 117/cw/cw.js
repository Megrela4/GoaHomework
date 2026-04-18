// მხოლოდ ციკლების, ცვლადების და სიის საბაზისო მეთოდების გამოყენებით(იგულისხმება სიაში ელემენტის დამატება) შექმენით შემდეგი ფუნქციების კლონი:
// forEach, map, filter, findIndex, some, every, reduce


// map
const myMap = (arr, callback) => {
    const result = [];

    for (let i = 0; i < arr.length; i++) {
        result.push(callback(arr[i], i, arr));
    }

    return result
}

// some
function mySome(arr, callback) {
    for (let i = 0; i < arr.length; i++) {
        if (callback(arr[i], i, arr)) {
            return true;
        }
    }
    return false
}

// findIndex
function myFindIndex(arr, callback) {
    for (let i = 0; i < arr.length; i++) {
        if (callback(arr[i], i, arr)) {
            return i;
        }
    }
    return -1;
}

// forEach
const myForEach = (arr, callback) => {
    for (let i = 0; i < arr.length; i++) {
        callback(arr[i], i, arr);
    }
}