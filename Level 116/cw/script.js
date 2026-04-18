// 🔹 სავარჯიშო 1 — findIndex
const numbers1 = [3, 7, 10, 15, 2];
// იპოვე პირველი ლუწი რიცხვის ინდექსი
const index = numbers1.findIndex(num => num % 2 === 0);
console.log(index);


// 🔹 სავარჯიშო 2 — findIndex
const words = ["cat", "dog", "elephant", "bee"];
// იპოვე იმ სიტყვის ინდექსი, რომლის სიგრძე არის 5-ზე მეტი
const index2 = words.findIndex(word => word.length > 5);
console.log(index2)


// 🔹 სავარჯიშო 3 — indexOf
const colors = ["red", "blue", "green", "blue"];
// იპოვე:
// 1. "blue"-ს პირველი ინდექსი
// 2. "yellow"-ს ინდექსი
const blue = colors.indexOf("blue");
const yellow = colors.indexOf("yellow");


// 🔹 სავარჯიშო 4 — reduce
const numbers2 = [2, 4, 6, 8];
// იპოვე ყველა რიცხვის ნამრავლი reduce-ის გამოყენებით
const namravli = numbers2.reduce((acc, num) => acc * num, 1);
console.log(namravli)


// 🔹 სავარჯიშო 5 — კომბინირებული
const nums = [5, 10, 15, 10, 20];
// 1. იპოვე პირველი 10-ის ინდექსი (indexOf)
// 2. იპოვე პირველი რიცხვი, რომელიც 12-ზე მეტია (findIndex)
// 3. იპოვე ყველა რიცხვის ჯამი (reduce)
const firstTen = nums.indexOf("10");
const BigNum = nums.findIndex(num => num > 12);
const jami = nums.reduce((acc, num) => acc + num, 1)


