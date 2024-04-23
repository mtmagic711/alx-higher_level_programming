#!/usr/bin/node

const { argv } = require('process');
const len = argv.length;
if (len <= 3) console.log(0);
else {
  argv.sort((a, b) => b - a);
  console.log(parseInt(argv[3]));
}
