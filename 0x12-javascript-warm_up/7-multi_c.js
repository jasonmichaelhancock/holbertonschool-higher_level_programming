#!/usr/bin/node
// A script that prints x times "C is fun".
let num = Number(process.argv[2]);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else for (i = 0; i < num; i++) {
  console.log('C is fun');
}
