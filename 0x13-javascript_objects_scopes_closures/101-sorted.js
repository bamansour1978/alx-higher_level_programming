#!/usr/bin/node
const dict = require('./101-data.js').dict;
let new_Dict = {};
for (let ky in dict) {
  if (new_Dict[dict[ky]] === undefined) {
    new_Dict[dict[ky]] = [ky];
  } else {
    new_Dict[dict[ky]].push(ky);
  }
}
console.log(new_Dict);
