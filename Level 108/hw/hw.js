const fruits = ["apple", "banana", "orange"];
fruits.push("mango");
console.log(fruits);

const numbers = [10, 20, 30, 40];
const removed = numbers.pop();
console.log(removed);
console.log(numbers);

const words = ["one", "two", "three", "four", "five"];
const joined = words.join("-");
console.log(joined);

const arr = [1, 2, 3, 4, 5, 6];
const sliced = arr.slice(2, 5);
console.log(sliced);

const cities = ["Tbilisi", "Paris", "London", "Rome"];
const firstCity = cities.shift();
console.log(firstCity);
console.log(cities);

const nums = [5, 10, 15];
nums.unshift(1);
console.log(nums);
console.log(nums.length);

const animals = ["dog", "cat", "lion"];
const birds = ["eagle", "sparrow", "owl"];
const combined = animals.concat(birds);
console.log(combined);

const list = [1, 2, 3, 4, 5, 6, 7];
list.splice(3, 2);
console.log(list);