#!/usr/bin/node
function add(a, b) {
    return a + b; // addition
}

console.log(add(Number(process.argv[2]), Number(process.argv[3])));
