// 1) გააკეთეთ მომდევნო დავალება if else, ternary  operator, switch case ის გამოყენებით
let number = Number(prompt("შეიყვანე რიცხვი:"));

if (number > 50) {
    console.log("big");
} else if (number > 25) {
    console.log("medium");
} else {
    console.log("small");
}
// მომხარებელს შემოატანინეთ რიცხვი (prompt ჩასვით Number() ში), შემდეგ შეამოწნეთ, თუ ეს რიცხვი მეტია 50 ზე დააკონსოლოგეთ "big", თუ ნაკლებია 50 ზე და მეტია 25 ზე დააკონსოლოგეთ "medium", სხვა შემთხვევაში  დააკონსოლოგეთ "small"


// 2) გააკეთეთ პირველი დავალება ternary  operator ის გამოყენებით
let number2 = Number(prompt("შეიყვანე რიცხვი:"));

number2 > 50 
    ? console.log("big") 
    : number2 > 25 
        ? console.log("medium") 
        : console.log("small");


// 3) გააკეთეთ მომდევნო დავალება switch case ის გამოყენებით
let number3 = Number(prompt("შეიყვანე რიცხვი:"));

switch (true) {
    case (number3 > 50):
        console.log("big");
        break;
    case (number3 > 25):
        console.log("medium");
        break;
    default:
        console.log("small");
}

