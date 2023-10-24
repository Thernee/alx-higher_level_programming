#!/usr/bin/node

const fs = require('fs');

const file = process.argv[2];
const message = process.argv[3];

fs.writeFile(file, message, 'utf-8', function (error) {
  if (error) console.log(error);
});
