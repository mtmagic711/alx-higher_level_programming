#!/usr/bin/node
const { argv } = require('process');
const parsed = parseInt(argv[2]);
if (!isNaN(parsed)) console.log(`My number: ${parsed}`);
else console.log('Not a number');
