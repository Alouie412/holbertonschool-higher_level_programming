#!/usr/bin/node

const value = process.argv[2];
let string = ''

if (isNaN(value)) {
  console.log('Missing size');
} else {
  for (i = 0; i < value; i++)
    string += 'X';

  for (i = 0; i < value; i++)
    console.log(string);
}
