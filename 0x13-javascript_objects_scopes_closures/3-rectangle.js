#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let height = this.height;
    while (height > 0) {
      let temp = this.width;
      let row = '';
      while (temp > 0) {
        row += 'X';
        temp--;
      }
      console.log(row);
      height--;
    }
  }
}

module.exports = Rectangle;
