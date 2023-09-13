#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

//   double () {
//     this.width = (this.size * 2);
//     this.height = (this.size * 2);
//   }
}

module.exports = Square;
