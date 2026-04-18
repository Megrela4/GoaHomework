const numbers1 = [3, 10, 15, 20, 7, 8];
const result1 = numbers1
  .filter(n => n % 2 === 0)
  .map(n => n * 3);
console.log(result1);

const names1 = ["nino", "giorgi", "ana", "luka"];
const result2 = names1.map(name =>
  name.charAt(0).toUpperCase() + name.slice(1).toLowerCase()
);
console.log(result2);

const users1 = [
  { name: "Gio", age: 17 },
  { name: "Nika", age: 21 },
  { name: "Luka", age: 15 }
];
const result3 = users1
  .filter(user => user.age >= 18)
  .map(user => user.name);
console.log(result3);

const numbers2 = [10, 20, 30, 40];
const avg = numbers2.reduce((sum, n) => sum + n, 0) / numbers2.length;
console.log(avg);

const words1 = ["apple", "kiwi", "banana", "fig", "orange"];
const result5 = words1.filter(word => word.length > 4);
console.log(result5);

const products = [
  { name: "Book", price: 20 },
  { name: "Pen", price: 5 },
  { name: "Laptop", price: 1000 }
];
const result6 = products.map(p => ({
  ...p,
  price: p.price * 1.1
}));
console.log(result6);

const sentences = ["hello world", "javascript is fun"];
const result7 = sentences.map(s => s.toUpperCase());
console.log(result7);

const items = ["a", "b", "c"];
items.forEach((item, index) => {
  console.log(`${index}: ${item}`);
});

const numbers3 = [1, 2, 2, 3, 4, 4, 5];
const unique = [...new Set(numbers3)];
console.log(unique);

const users2 = [
  { name: "Gio", score: 80 },
  { name: "Nika", score: 45 },
  { name: "Luka", score: 90 }
];
const result10 = users2
  .filter(u => u.score > 50)
  .map(u => ({ ...u, passed: true }));
console.log(result10);