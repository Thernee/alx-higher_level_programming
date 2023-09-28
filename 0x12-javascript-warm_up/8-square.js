#!/usr/bin/node

let convertedNum = parseInt(process.argv[2]);
if (isNaN(convertedNum)) console.log('Missing size');
else {
  const holder = convertedNum;
  while (convertedNum > 0) {
    let temp = holder;
    let row = '';
    while (temp > 0) {
      row += 'X';
      temp--;
    }
    console.log(row);
    convertedNum--;
  }
}
