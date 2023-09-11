#!/usr/bin/node

const { argv } = require('process');
if (argv.length < 3) {
  console.error("Veuillez fournir un nombre en argument.");
  process.exit(1); // Quitter le script avec un code d'erreur
}

const a = parseInt(argv[2], 10);

function factorial(a) {
  if (a <= 1) return 1;
  return a * factorial(a - 1);
}

if (isNaN(a)) console.log(1);
else console.log(factorial(a));
