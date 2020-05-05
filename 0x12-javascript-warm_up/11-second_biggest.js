#!/usr/bin/node

const length = process.argv.length;
const array = [];
let i;

if (length === 2 || length === 3) {
  console.log(0);
} else {
  for (i = 2; i < length; i++) {
    array.push(parseInt(process.argv[i]));
  }

  array.sort();
  console.log(array);
  console.log(i);
  /*
    Because of how sorting works, NaN always comes after
    numbers. This for loop is to purge the array of all NaNs
    Also length - 3. 1 because of how arrays are counted, and 2
    because of the execution of this file
  */
  for (i = length - 3; isNaN(array[i]); i--)
    array.pop();

  // After purging all NaNs (if any), get rid of the largest value
  // because we want the 2nd largest value in the array
  array.pop();
  console.log(Math.max.apply(null, array));
}
