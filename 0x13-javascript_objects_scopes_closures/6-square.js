#!/usr/bin/node

const squareBase = require('./5-square.js');

class Square extends squareBase {
  charPrint (c) {
    if (c === undefined) c = 'X';
    for (let i = 0; i < this.height; i++) console.log(`${c}`.repeat(this.width));
  }
}

module.exports = Square;
