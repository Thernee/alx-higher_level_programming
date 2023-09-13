#!/usr/bin/node

const Sqr = require('./5-square');

class Square extends Sqr {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  double () {
    this.width = (this.size * 2);
    this.height = (this.size * 2);
  }

  charPrint (c) {
    if (c === undefined) this.print();

    else {
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
}

module.exports = Square;
