// 1) შექმენით function expression, რომელიც არგუმენტად მიიღებს რიცხვს და დააბრუნებს true-ს,
// თუ რიცხვი ლუწია, ხოლო false-ს — თუ კენტია.

// გამოიძახეთ ფუნქცია და დაბეჭდეთ შედეგი.

const isEven = function (number) {
    return number % 2 === 0;
};

console.log(isEven(10));
console.log(isEven(7));



// 2) შექმენით ფუნქცია default parameter-ით, რომელიც მიესალმება მომხმარებელს. მაგ: "Hello Aleqsandre" მაგრამ თუ მომხმარებელმა პარამეტრად არაფერი შეიყვანა მაშინ დააბრუნეთ "Hello Guest"

function greetUser(name = "Guest") {
    return `Hello ${name}`;
}

console.log(greetUser("Aleqsandre"));
console.log(greetUser());



// 3) შექმენით helper ფუნქცია რომელსაც ექნება default პარამეტრი: 0, რომელიც მიიღებს ტემპერატურას Fahrenheit-ში და დააბრუნებს შესაბამის მნიშვნელობას Celsius-ში. ფორმულა: (F − 32) × 5 / 9 ან (F - 32) : 1,8. შემდეგ შექმენით მთავარი ფუნქცია, რომელიც გამოიყენებთს Fahrenheit-ს helper ფუნქციას, და დააბრუნებს მიღებულ Celsius-ს.

function fahrenheitToCelsius(fahrenheit = 0) {
    return (fahrenheit - 32) * 5 / 9;
}

function getCelsiusFromFahrenheit(fahrenheit) {
    return fahrenheitToCelsius(fahrenheit);
}

console.log(getCelsiusFromFahrenheit(68));
console.log(getCelsiusFromFahrenheit());   