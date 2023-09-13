#!/usr/bin/node

function callMeMoby (x, xfunction) {
  while (x > 0) {
    xfunction();
    x--;
  }
}

module.exports = { callMeMoby };
