// შექმენით ცვლადი სახელად person და შეინახეთ მასში ობიექტი შემდეგი კუთვნილებებით(key): name, age, height
// დაბეჭდეთ ეს ობიექტი, შემდეგ კი დაბეჭდეთ მისი თითოეული კუთვნილება ცალ-ცალკე.

    let person = {
        name: "Nika",
        age: 14,
        height: 172,
    }

    console.log(person);

    console.log(person.name);
    console.log(person.age);
    console.log(person.height);

// თქვენს მიერ, პირველ დავალებაში შექმნილი ობიექტის age კუთვნილება შეცვალეთ და დაბეჭდეთ განახლებული ობიექტი.
person.age = 15;
console.log(person.age)

// წაშალეთ იგივე ობიექტიდან height კუთვნილება(გამოიყენეთ delete)
delete person.height;
console.log(person);