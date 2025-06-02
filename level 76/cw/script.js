// 1) შექმენით ცვლადი სადაც შეინახავთ თქვენთვის სასურველ ასაკს, თუ იქნება 13 წელზე ნაკლების გამოუტანეთ You are kid, თუ იქნება 18 წელზე ნაკლების მაგრამ 
// 13'ზე მეტის გამოუტანეთ You are not adult yet და თუ იქნება 18 წელზე მეტის გამოუტანეთ You are adult
let age = 13
if (age < 13) {
  console.log("You are kid");
} else if (age > 13 && age < 18) {
  console.log("You are not adult yet");
} else {
  console.log("You are adult");
}

// 2) შექმენით ცვლადი სადაც შეიტანთ რაიმე რიცხვს, თუ რიცხვი იყოფა 2'ზე უნაშთოდ გამოიტანეთ ეს რიცხვი, სხვა შემთხვევაში დააბრუნეთ "ეს რიცხვი კენტია"
let num = 4
if (num / 2 == 0) {
    console.log(num)
} else {
    console.log("ეს რიცხვი კენტია")
}

// 3) პირველი დავალება შეასრულეთ python'შიც და დაწერეთ განსხვავებები python'ისა და js'ს შორის.

// python
// let age = 13                                           
// if age < 13:
//     print("You are kid")
// elif age < 18:
//     print("You are not adult yet")
// else:
//     print("You are adult")

// js
// let age = 13
// if (age < 13) {
//   console.log("You are kid");
// } else if (age > 13 && age < 18) {
//   console.log("You are not adult yet");
// } else {
//   console.log("You are adult");
// }

// python-ში ვიყენებთ პრინტს და javasciptshi ვიყენებთ {} და console.logს ასევე pythonში არის elifი ხოლო javascriptში არის else ifი


// 4) რას აკეთებს "!" ოპერატორი ახსენით თქვენი სიტყვებით
// თუ რაღაც მართალია ! გადააქცევს მას ცრუად
// თუ რაღაც ცრუა ! გადააქცევს მას მართლად

// example:
console.log(!true);   // false
console.log(!false);  // true


