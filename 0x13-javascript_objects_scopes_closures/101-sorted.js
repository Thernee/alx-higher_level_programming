#!/usr/bin/node

const dict = require('./101-data.js').dict;

const sortedDict = { };
for (const key in dict) {
  const value = dict[key];
  if (!sortedDict[value]) {
    sortedDict[value] = [];
  }
  sortedDict[value].push(Number(key));
}

console.log(sortedDict);
