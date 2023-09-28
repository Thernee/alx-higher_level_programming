#!/usr/bin/node

function factorial (num) {
  if (isNaN(num) || num === 0) return 1;
  else if (num < 0) return -1;
  return num * factorial(num - 1);
}

const input = parseInt(process.argv[2]);
console.log(factorial(input));
