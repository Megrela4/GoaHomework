// 1) ახსენით Truthy და Falsy კომენტარის სახით
// Falsy - მნიშვნელობა რომელიც if ში ჩაითვლება როგორც false.
// Truthy - მნიშვნელობა რომელიც if ში ჩაითვლება როგორც true.


// 2) ახსენით Ternary ოპერატორი და რისთვის ვიყენებთ მას კომენტარის სახით
// Ternary ოპერატორი არის მოკლე გზა if / else-ის ჩასაწერად


// 3)
// let age = prompt();

// if (age >= 18) {
//   console.log("Adult");
// } else {
//   console.log("Minor");
// }

// დაწერეთ იგივე კოდი Ternary ოპერატორის გამოყენებით: age >= 18 ? console.log("Adult") : console.log("Minor");


// 4)
// let number = prompt();

// if (number >= 0) {
//   console.log("Positive");
// } else {
//   console.log("Negative");
// }

// დაწერეთ იგივე კოდი Ternary ოპერატორის გამოყენებით: number >= 0 ? console.log("Positive") : console.log("Negative");


// 5) დაწერეთ პროგრამა, რომელიც იღებს ტემპერატურას და აბრუნებს: 15ზე ნაკლები: ცივა, 15ზე მეტი და 25ზე ნაკლები: თბილა, 25ზე მეტი: ცხელა
// let temperature = prompt();

// if (temperature < 15) {
//   console.log("ცივა");
// } else if (temperature >= 15 && temperature < 25) {
//   console.log("თბილა");
// } else {
//   console.log("ცხელა");
// }


// 6) დაწერეთ პროგრამა რომელიც მიიღებს 3 რიცხვს. თქვენი დავალებაა რომ დააბუნოთ ყველაზე დიდი რიცხვი მათ შორის.


// 7) ცვლადში შეინახეთ თქვენი სახელი და შექმენით switch case --> განიხილეთ case "davit" და დაბეჭდეთ შსაბამისად მისალმების ტექსტი, ასევე case "nikolozi", case "vazha" და რაიმე default case-ი.
// let name = prompt();

// switch (name) {
//   case "davit":
//     console.log("გამარჯობა Davit!");
//     break;

//   case "nikolozi":
//     console.log("გამარჯობა Nikolozi!");
//     break;

//   case "vazha":
//     console.log("გამარჯობა Vazha!");
//     break;

//   default:
//     console.log("გამარჯობა!");
// }


// 8) switch case გამოყენებით შეამოწმეთ ასო ხმოვანია თუ თანხმოვანი. tip: case-ებით განიხილეთ ხმოვნები და default იყოს თანხმოვანი
// let letter = prompt();

// switch (letter) {
//   case "a":
//   case "e":
//   case "i":
//   case "o":
//   case "u":
//     console.log("ხმოვანია");
//     break;

//   default:
//     console.log("თანხმოვანია");
// }