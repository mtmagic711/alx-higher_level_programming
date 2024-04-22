#!/usr/bin/node

function factorial (number) {
  if (isNaN(number)) return 1;
  if (number === 0) return 1;
  return number * factorial(number - 1);
}

const { argv } = require('process');
const fact = factorial(argv[2]);

console.log(fact);
