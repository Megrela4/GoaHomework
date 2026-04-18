const isEven = function(num) {
  return num % 2 === 0;
};

console.log(isEven(4));
console.log(isEven(7));

function greet(name = "Guest") {
  return `Hello ${name}`;
}

console.log(greet("Aleqsandre"));
console.log(greet());

function toCelsius(f = 0) {
  return (f - 32) * 5 / 9;
}

function main(f) {
  return toCelsius(f) * 5;
}

console.log(main(68));