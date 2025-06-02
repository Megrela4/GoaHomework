// 1) "!" ოპერატორზე შეასრულეთ 5 true და 5 false ოპერაციები.
console.log(!false);       
console.log(!0);           
console.log(!undefined);
console.log(!null);       
console.log(!"");  
console.log(!true);       
console.log(!"hello");    
console.log(!{});         
console.log(![]); 


// 2) შექმენით ცვლადი რომელშიც შეინახავთ 0-100 მდე რენდომ რიცხვს შემდეგ კი გამოიტანეთ შეფასება თუ მაგალითად 90'დან 100'ის ჩათვლით ექნება ქულა გამოუტანეთ "Grade A",
// თუ 80'დან 89'ის ჩათვლით გამოუტანეთ "Grade B" და ა.შ.
let score = Math.floor(Math.random() * 101); 
console.log("შენმა ქულამ შეადგინა:", score);

if (score >= 90 && score <= 100) {
  console.log("Grade A");
} else if (score >= 80 && score <= 89) {
  console.log("Grade B");
} else if (score >= 70 && score <= 79) {
  console.log("Grade C");
} else if (score >= 60 && score <= 69) {
  console.log("Grade D");
} else {
  console.log("Grade F");
}


// 3) შექმენით ცვლადი სადაც 10'ის ფარგლებში რანდომულად შეინახავთ რაღაც რიცხვს თუ ეს რიცხვი მეტი იქნება 5'ზე მაშინ დააბრუნეთ ეს რიცხვი სხვა შემთხვევაში დააბრუნეთ მისი კვადრატი.
let number = Math.floor(Math.random() * 11);
console.log("შემთხვევითი რიცხვი არის:", number);

if (number > 5) {
  console.log("რიცხვი მეტია 5-ზე:", number);
} else {
  let square = number * number;
  console.log("რიცხვი 5-ზე ნაკლებია ან ტოლია. მისი კვადრატი არის:", square);
}