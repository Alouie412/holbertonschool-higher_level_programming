#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (parseInt(h) > 0) {
      this.height = h;
    }
    if (parseInt(w) > 0) {
      this.width = w;
    }
  }
}

module.exports = Rectangle;
