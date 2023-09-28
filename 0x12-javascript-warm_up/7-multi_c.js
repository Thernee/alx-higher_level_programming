#!/usr/bin/node

let argLen = (parseInt(process.argv[2]));
if (!argLen) console.log('Missing number of occurrences');

while (argLen > 0) {
  console.log('C is fun');
  argLen--;
}
