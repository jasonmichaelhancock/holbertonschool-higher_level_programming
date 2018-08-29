#!/usr/bin/node
// A script that prints the addition of 2 integers.
let a = Number(process.argv[2]);
let b = Number(process.argv[3]);
function add (a, b) {
  return a + b;
}
console.log(add(a, b));
