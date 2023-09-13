#!/usr/bin/node

function nbOccurences(list, searchElement) {
  let count = 0;
  for (const elem of list) {
    if (elem === searchElement) count++;
  }
  return count;
}

exports.nbOccurences = nbOccurences;
