// 1
function printNumbers(number) {
    for (let i = 0; i <= number; i++) {
        console.log(i);
    }
}


// 2
function greetUser(name, age) {
    if (age < 18) {
        return "You're not an adult yet";
    } else {
        return `Hello, ${name}! Welcome.`;
    }
}