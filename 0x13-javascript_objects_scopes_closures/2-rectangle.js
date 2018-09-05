#!/usr/bin/node
// An class Rectangle that defines a rectangle with w and h parameters.
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && w !== undefined && h !== undefined) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
