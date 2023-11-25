console.log("Your Problem");

// ------------------------------ Enter the array Numbres ---------------------

arr = [1, 2, 3, 5, 6, 7]
// Result --[1, 2, 3, 5, 6, 8]

// ------------------------------ End ---------------------
b = arr.join("")
b = Number.parseInt(b) + 1

d = b.toString()

h = []
Array.from(d).forEach((element)=>{
    element = Number.parseInt(element)
    h.push(element)
})

console.log(h);

/*

[1, 2, 3, 5, 6, 7]
 --[1, 2, 3, 5, 6, 8]


[1, 2, 3, 5, 6, 9]

--- [ 1, 2, 3, 5, 7, 0]
 
[9, 9 ,9 , 9, 9, 9] + 1
[1, 0, 0, 0, 0, 0, 0]


[1, 2, 3, 5, 6, 7]
9999
+ 1
10000

999
1

*/