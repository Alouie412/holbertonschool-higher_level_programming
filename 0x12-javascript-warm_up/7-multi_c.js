#!/usr/bin/node

let count = parseInt(process.argv[2], 10);

if (isNaN(count)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < count; i++)
    console.log('C is fun');
}
