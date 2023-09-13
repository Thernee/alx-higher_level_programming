#!/usr/bin/node

function addMeMaybe (x, xfunction) {
  xfunction(x + 1);
}

module.exports = { addMeMaybe };
