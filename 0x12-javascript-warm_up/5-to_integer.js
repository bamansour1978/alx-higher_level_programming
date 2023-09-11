#!/usr/bin/node
const Num = Math.floor(Number(process.argv[2]));
console.log(isNaN(Num) ? 'Not a number' : `My number: ${Num}`);
