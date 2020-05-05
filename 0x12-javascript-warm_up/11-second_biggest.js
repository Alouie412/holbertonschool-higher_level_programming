#!/usr/bin/node

const length = process.argv.length;
let array = [];
let bigNum;

if (length === 2 || length === 3) {
  console.log(0);
} else {
  for (i = 2; i < length; i++)
    array.push(parseInt(process.argv[i]));

  array.sort();
  array.pop();

  console.log(Math.max.apply(null, array));
}
