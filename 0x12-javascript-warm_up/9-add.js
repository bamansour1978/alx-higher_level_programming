#!/usr/bin/node

const { argv } = require('process');
const [,, a, b] = argv.map(Number);

const add = (a, b) => a + b;

console.log(add(a, b));
