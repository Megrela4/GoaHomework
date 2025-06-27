// 1
for (let i = 2; i <= 20; i += 2) {
    console.log(i);
}

// 2
let text = "გამარჯობა";
for (let i = 0; i < text.length; i++) {
    console.log(text[i]);
}

// 3
let myArray = ["ა", "ბ", "გ", "დ", "ე", "ვ", "ზ"];
for (let i = 0; i < myArray.length; i++) {
    if (i % 2 === 0) {
        console.log(myArray[i]);
    }
}

// 4
let i = 1;
while (i <= 50) {
    if (i % 2 === 0) {
        console.log(i);
    }
    i++;
}

// 5
let i = 1;
let sum = 0;
while (i <= 80) {
    if (i % 2 === 0) {
        sum += i;
    }
    i++;
}
console.log("ლუწი რიცხვების ჯამი:", sum);