// 1) შექმენით 5 ელემენტიანი სია, .push() მეთოდის გამოყენებით სიაში ჩაამატეთ თქვენი სახელი.
let arr = [1, 2, 3, 4, 5];
arr.push("Nika");

console.log(arr);

// 2) იგივე სიის ბოლოდან ამოშალეთ ბოლო ელემენტი .pop() მეთოდის გამოყენებით.
arr.pop();

// 3) .join() მეთოდის მეშვეობით გააერთიანეთ ეს სია space-ით string-ის სახით.
let joined = arr.join(" ");
console.log(joined);

// 4) .slice() მეთოდის მეშვეობით სიიდან ამოიღეთ 0-ე ინდექსიდან 4-მდე ელემენტები და შესაბამისად დაბეჭდეთ.
let sliced = arr.slice(0, 4);
console.log(sliced);

// 5) .concat() მეთოდის გამოყენებით შეართეთ 2 სია ერთმანეთს და დაბეჭდეთ საბოლოო შედეგი.
let arr2 = [6, 7, 8];
let combined = arr.concat(arr2);
console.log(combined);

// 6) .shift() მეთოდის მეშვეობით დაბეჭდეთ სიაში პირველი ელემენტი
let first = arr.shift();
console.log(first);

// 7) .unshift() მეთოდის მეშვეობით ჩაამატეთ სიაში ახალი მნიშვნელობა და დაბეჭდეთ სიის საბოლოო სიგრძე
let gocha = arr.unshift(67);
console.log(gocha)