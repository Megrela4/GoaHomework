// 1
function grhi(name){
    let num = prompt("Enter a Number: ");
    let i = 0;
    while(i < num) {
        console.log("hello" + name);
        i++
    }
}
console.log(grhi("nika"))


// 2
function guessnum(number){
    let other = prompt("enter number 1 to 10");
    switch (number == number){
        case number == other:
            console.log("ყოჩაღ შენ გამოიცანი");
            break;
        case number !== other:
            other = console.log(prompt("enter number 1 to 10"));
            break;
        default:
            other = console.log(prompt("enter number 1 to 10"));
            break;
    }
}
