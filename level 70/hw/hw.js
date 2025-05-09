// 1) შექმენით ობიექტი დასაც ჩამოწერთ თქვენს თავზე ინფორმაციას, შემდეგ ამ ობიექტიდან გამოიტანეთ თქვენი სახელი და გვარი.
let me = {
    saxeli: "ნიკა",
    gvari: "მეგრელიშვილი                                              ",
    asaki: 13,
    iqnebaProgramisti: true
};


// 2) შექმენით ობიექტი სადაც შეიყვანთ სახელსა და გვარს შემდეგ კი გაანახლეთ მათი value'ბი და გამოიტანეთ ეს ობიექტი.
let person = {
    saxeli: "ალექსანდრე",
    gvari: "მეგრელიშვილი"
};
person.saxeli = "ნიკა";
person.gvari = "მეგრელიშვილი";


// 4) შექმენით ცვლადი რომელსაც გადასცემთ სტრინგს შემდეგ კი დააბრუნეთ ამ ცვლადის სიგრძე.
let myText = "გამარჯობა";
console.log(myText.length);


// 5) შექმენით ცვლადი და გადაიყვანეთ იგი uppercase'ში შემდეგ კი lowercase'ში.
let text = "random";
let upper = text.toUpperCase();
let lower = upper.toLowerCase();