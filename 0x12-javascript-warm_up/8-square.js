#!/usr/bin/node
const x_size = Math.floor(Number(process.argv[2]));
if (isNaN(x_size)) {
  console.log('Missing size');
} else {
  for (let k = 0; k < x_size; k++) {
    let row = '';
    for (let d = 0; d < x_size; d++) row += 'X';
    console.log(row);
  }
}
