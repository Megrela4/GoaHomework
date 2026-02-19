// 1) ცვლადში შეინახეთ random რიცხვი 1-10 მდე. შეამოწმე ეს რიცხვი ლუწია თუ კენტი.
let randomNumber = Math.floor(Math.random() * 10) + 1;

console.log("Random რიცხვი არის:", randomNumber);

if (randomNumber % 2 === 0) {
    console.log("ეს რიცხვი ლუწია");
} else {
    console.log("ეს რიცხვი კენტია");
}


// 2) შექმენით ცვლადი age. თუ ასაკი ნაკლებია 13-ზე გამოიტანოს "ბავშვი", თუ ასაკი 13-დან 17-მდეა გამოიტანოს  "თინეიჯერი", თუ ასაკი 18 ან მეტია გამოიტანოს  "ზრდასრული"
let age = 15;

if (age < 13) {
    console.log("ბავშვი");
} else if (age >= 13 && age <= 17) {
    console.log("თინეიჯერი");
} else {
    console.log("ზრდასრული");
}


// 3) შექმენით 2 ცვლადი, პირველში შეინახეთ username მეორეში password. შეამოწმე ეს username უდრის თუ არა "admin" და password უდრის თუ არა "1234" თუ უდრის გამოიტანოს "გილოცავთ თქვენ მოიგეთ 1000 robux". თუ რომელიმე username ან password არასწორია გამოიტანოს "თავიდან სცადე".
let username = "admin";
let password = "1234";

if (username === "admin" && password === "1234") {
    console.log("გილოცავთ თქვენ მოიგეთ 1000 robux");
} else {
    console.log("თავიდან სცადე");
}