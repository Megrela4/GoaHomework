// 1) შექმენით ფუნქცია, რომელიც მომხმარებელს შემოატანინებს სახელს და თუ ეს სახელი ემთხვევა თქვენსას დაბეჭდეთ true, სხვა შემთხვევაში დაბეჭდეთ false.
function checkName() {
  const userName = prompt("შეიყვანეთ თქვენი სახელი:");
  const myName = "Nika";

  console.log(userName === myName);
}


// 2) შექმენით arrow ფუნქცი, რომელიც არგუმენტად მიიღებს 3 რიცხვს და დააბრუნებას მათ ნამრავლს.

// გამოიძახეთ ეს ფუნქცია და დაბეჭდეთ მისი დაბრუნებული მნიშვნელობა
const multiplyNumbers = (a, b, c) => a * b * c;

const result = multiplyNumbers(2, 3, 4);
console.log(result);
