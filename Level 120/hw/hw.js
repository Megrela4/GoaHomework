// ობიექტი არის მონაცემთა სტრუქტურა, რომელიც ინახავს მონაცემებს key-value წყვილების სახით
// key (კუთვნილება) არის სახელი, ხოლო value (მნიშვნელობა) არის ამ სახელთან დაკავშირებული ინფორმაცია

const car = {
  model: "BMW",
  color: "black",
  year: 2020
};

const userInput = prompt("Enter property (model, color, year):");

console.log(car[userInput]);

// თუ ვცდით არარსებული კუთვნილების წამოღებას:
console.log(car.speed);

// შედეგი იქნება undefined,
// რადგან ობიექტში ასეთი კუთვნილება არ არსებობს