#!/usr/bin/node

const Sqr = require('./5-square');

class Square extends Sqr {
  charPrint (c) {
    if (c === undefined) this.print();

    else {
      let height = this.height;
      while (height > 0) {
        let temp = this.width;
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
