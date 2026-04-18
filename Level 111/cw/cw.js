// 1) გამოთვალე 1-დან 100-მდე რიცხვების ჯამი for ციკლის გამოყენებით.
let sum = 0;

for (let i = 1; i <= 100; i++) {
    sum += i;
}

console.log(sum);


// 2) დაწერე პროგრამა, რომელიც 10-დან 1-მდე რიცხვებს დაბეჭდავს while ციკლით.
let num = 10;

while (num >= 1) {
    console.log(num);
    num--;
}

// 3) დაწერე პროგრამა, რომელიც მომხმარებელს სთხოვს რიცხვს, და მანამდე ეკითხება სანამ არ შეიყვანს 0-ს (do while გამოიყენე).
let intput;

do {
    input = Number(prompt("Enter number:"));
} while (input !== 0);



