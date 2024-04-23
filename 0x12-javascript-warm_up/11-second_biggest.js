#!/usr/bin/node

const { argv } = require('process');
const len = argv.length;
if (len === 2 || len === 3) console.log(0);
else {
  argv.sort();
  console.log(parseInt(argv[len - 2]));
}
