#!/usr/bin/node
// A script that computes and prints a factorial.
let num = Number(process.argv[2]);
function factorial(num) {
  if (isNaN(num)) {
    return 1;
  }
  if (Number(num) === 1) {
    return 1;
  }
  return num * factorial(Number(num) - 1);
}
console.log(factorial(num));
