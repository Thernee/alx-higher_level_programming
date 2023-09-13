#!/usr/bin/node

const Rectangle = require('./3-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  double () {
    this.width = (this.size * 2);
    this.height = (this.size * 2);
  }

  charPrint (c = 'X') {
    let height = this.size;
    while (height > 0) {
      let temp = this.size;
      let row = '';
      while (temp > 0) {
        row += c;
        temp--;
      }
      console.log(row);
      height--;
    }
  }
}

module.exports = Square;
