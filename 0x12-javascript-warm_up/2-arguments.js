#!/usr/bin/node

// console.log(process.argv.length - 2);
const argLength = (process.argv.length - 2);

if (argLength === 0) console.log('No argument');
else if (argLength === 1) console.log('Argument found');
else if (argLength > 1) console.log('Arguments found');
