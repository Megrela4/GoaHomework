// // 1.
const numbers1 = [2, 4, 6, 8, 10];
// // forEach გამოყენებით დაბეჭდე თითოეული რიცხვი
numbers1.forEach(num => console.log(num));

// // 2.
const numbers2 = [1, 2, 3, 4];
// // map გამოყენებით შექმენი ახალი მასივი, სადაც ყველა ელემენტი გაორმაგებულია
const double = numbers2.map(num => num * 2);
console.log(double);

// // 3.
const numbers3 = [5, 12, 8, 130, 44];
// // filter გამოყენებით დატოვე მხოლოდ რიცხვები > 10
const atzeMeti = numbers3.filter(num => num > 10);
console.log(atzeMeti);

// // 4.
const names = ["Nino", "Giorgi", "Ana"];
// // forEach გამოყენებით დაბეჭდე: "Hello, Nino" და ა.შ.
names.forEach(name => console.log(`Hello, ${name}`));


// // 5.
const prices = [10, 20, 30];
// // map გამოყენებით დაამატე თითოეულს +5
const higherPrices = prices.map(prices => price + 5);
console.log(higherPrices);


// // 6.
const numbers4 = [3, 7, 2, 9, 12];
// // filter გამოყენებით დატოვე მხოლოდ ლუწი რიცხვები
const evenNumbers = numbers4.filter(num => num % 2 === 0);
console.log(evenNumbers);

// // 7.
const words = ["apple", "banana", "kiwi"];
// // map გამოყენებით დააბრუნე სიტყვების სიგრძეები
const sigrdze = words.map(word => word.length);
