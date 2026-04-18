// 1
let numbers = [];

for (let i = 0; i < 10; i++) {
    let num = Number(prompt("შეიყვანე რიცხვი:"));
    numbers.push(num);
}

console.log("საწყისი სია:", numbers);

// 2
// პირველი ელემენტის წაშლა
numbers.shift();

// ბოლო ელემენტის წაშლა
numbers.pop();

// მე-3 და მე-4 ინდექსების წაშლა
numbers.splice(3, 2);

console.log("განახლებული სია:");

for (let i = 0; i < numbers.length; i++) {
    console.log(numbers[i]);
}

// 3
let sum = 0;

for (let i = 0; i < 5; i++) {
    let num = Number(prompt("შეიყვანე რიცხვი:"));
    sum += num;
}

let average = sum / 5;

console.log("საშუალო არითმეტიკული:", average);