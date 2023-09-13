#!/usr/bin/node
const dict = require('./101-data.js').dict;
let newDict = {};
for (let ky in dict) {
  if (newDict[dict[ky]] === undefined) {
    newDict[dict[ky]] = [ky];
  } else {
    newDict[dict[ky]].push(ky);
  }
}
console.log(newDict);
