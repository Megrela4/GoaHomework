// 1
let num = Number(prompt("შეიყვანე დადებითი რიცხვი:"));

let result = 1;
let i = 1;

while (i <= num) {
    result *= i;
    i++;
}

console.log("ნამრავლი:", result);

// 2
function getRandomElement(arr) {
    let randomIndex = Math.floor(Math.random() * arr.length);
    return arr[randomIndex];
}

// მაგალითი
let numbers = [10, 20, 30, 40, 50];
console.log(getRandomElement(numbers));

// 3
// do while ციკლი მუშაობს ასე:
// კოდი პირველად მაინც შესრულდება (მიუხედავად პირობის),
// შემდეგ კი ამოწმებს პირობას და თუ true-ა, აგრძელებს.

// მაგალითი 1
let i = 1;

do {
    console.log(i);
    i++;
} while (i <= 5);


// მაგალითი 2
let password;

do {
    password = prompt("შეიყვანე პაროლი:");
} while (password !== "1234");

// ეს ციკლი გაგრძელდება მანამდე სანამ მომხმარებელი სწორ პაროლს არ შეიყვანს
