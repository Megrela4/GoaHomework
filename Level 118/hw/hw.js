const numbers1 = [3, 10, 7, 20, 5];
const result1 = numbers1.map(n => n > 10 ? n * 2 : n + 5);
console.log(result1);

const numbers2 = [12, 25, 7, 30, 18, 5];
const result2 = numbers2.filter(n => n > 10 && (n % 2 === 0 || n % 5 === 0));
console.log(result2);

const numbers3 = [1, 2, 3, 4, 5, 6];
const result3 = numbers3
  .map(n => n * n)
  .filter(n => n > 10);
console.log(result3);

const numbers4 = [5, 17, 3, 9, 21];
const max = numbers4.reduce((acc, curr) => acc > curr ? acc : curr);
console.log(max);

const words = ["Hello", "world", "this", "is", "JS"];
const sentence = words.reduce((acc, curr) => acc + " " + curr);
console.log(sentence);

const numbers5 = [4, 9, 16, 25, 36, 49];
const result6 = numbers5
  .filter(n => n % 2 === 0)
  .map(n => Math.sqrt(n))
  .reduce((sum, n) => sum + n, 0);
console.log(result6);