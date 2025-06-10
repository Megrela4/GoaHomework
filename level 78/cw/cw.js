// 1) მომხმარებელს შემოატანინეთ თვისი წლოვანება თუ ასაკი არ აღემატება 14 გამოიტანეთ "you are kid"
//  თუ ასაკი აღემატება 14 მაგრამ არ აღემატება 18 დააბრუნეთ "you are not adult yet" და თუ აღემატება 18 დააბრუნეთ "you are adult"
let age = prompt("შეიყვანე ასაკი:");
age = Number(age);

if (age <= 14) {
  alert("you are kid");
} else if (age <= 18) {
  alert("you are not adult yet");
} else {
  alert("you are adult");
}



// 2) შემქენით ცვლადი რომელშიც შეინახავთ თქვენთვის სასურველ სახელს ან დატოვებთ ცარიელს თუ ცვლადი იქნება true მიესალმეთ ამ სახელს სხვაშემთხვევაში მიანიჭეთ "guest" და შემდეგ მიესალმეთ მას
let nam = ""; 

if (nam) {
  console.log("Hello, " + nam);
} else {
  nam = "guest";
  console.log("Hello, " + nam);
}


// 3) შექმენით ცვლადი სადაც მომხმარებელს შემოატანინებთ თავის სახელს შემდეგ შემქნით ცვლადი სადაც მომხმარებელს შემოატანინებთ თავის ასაკს თუ ასაკი არ აღემატება 18 გამოიტანეთ
//  "you are not adult yet 'name'!" თუ ასაკი აღემატება 18 მაშინ გამოიტანეთ "Hello 'name'!"
let na = prompt("შეიყვანე შენი სახელი:");
let ag = Number(prompt("შეიყვანე შენი ასაკი:"));

if (ag <= 18) {
  console.log(`you are not adult yet ${na}!`);
} else {
  console.log(`Hello ${na}!`);
}
