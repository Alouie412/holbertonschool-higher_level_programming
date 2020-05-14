#!/usr/bin/node

const array = require('./100-data').list;

console.log(array);
const map = array.map((a, b) => a * b);
console.log(map);
