#!/usr/bin/node
// An class Rectangle that defines a rectangle with w and h parameters,
// which prints the rectangle object.
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && w !== undefined && h !== undefined) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    let line = '';
    let i = 0;
    let j = 0;
    while (j < this.width) {
        line += 'X';
        j++;
    }
    while (i < this.height) {
      console.log(line);
      i++;
    }
  }
}
module.exports = Rectangle;
