#!/usr/bin/node

function esrever (list) {
  const reversed = [];
  let len = (list.length - 1);
  for (const elem of list) {
    reversed[len] = elem;
    len--;
  }
  return reversed;
}

exports.esrever = esrever;
