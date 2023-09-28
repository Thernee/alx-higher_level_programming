#!/usr/bin/node

const input = process.argv;
function add (a, b) {
  console.log(a + b);
}

add(parseInt(input[2]), parseInt(input[3]));
