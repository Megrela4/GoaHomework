// callback ფუნქცია არის ფუნქცია, რომელიც გადაეცემა სხვა ფუნქციას არგუმენტად
// და გამოიძახება ამ ფუნქციის შიგნით კონკრეტულ დროს ან პირობის შესრულებისას

const numbers = [10, 15, 20, 25, 30, 35];

numbers.forEach(function(item, index) {
  if (index % 2 === 0) {
    console.log(item);
  }
});

const newArr = [];

numbers.forEach(function(item) {
  if (item % 2 !== 0) {
    newArr.push(item);
  }
});

console.log(newArr);