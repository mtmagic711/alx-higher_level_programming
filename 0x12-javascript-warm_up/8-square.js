#!/usr/bin/node
const { argv } = require('process');
const N = parseInt(argv[2]);
let i;
if (!isNaN(N)) {
  for (i = 0; i < N; i++) {
    console.log('x'.repeat(N));
  }
} else console.log('Missing size');
