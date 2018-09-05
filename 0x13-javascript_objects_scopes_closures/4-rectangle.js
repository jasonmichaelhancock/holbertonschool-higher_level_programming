#!/usr/bin/node
// An class Rectangle that defines a rectangle with w and h parameters,
// which prints the rectangle object, adding rotate() and double() methods.
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
  rotate () {
    let temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
