#!/usr/bin/node

function add (a, b) {
  a = parseInt(a);
  b = parseInt(b);
  console.log(a + b);
}

const { argv } = require('process');

add(argv[2], argv[3]);
