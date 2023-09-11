#!/usr/bin/node

const { argv } = require('process');
const a = parseInt(argv[2], 10);

const factorial = (n) => {
  if (n <= 1) return 1;
  return n * factorial(n - 1);
};

const result = isNaN(a) ? 1 : factorial(a);
console.log(result);
