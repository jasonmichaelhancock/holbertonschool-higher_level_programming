#!/usr/bin/node
// A script that computes and prints a factorial.
let num = Number(process.argv[2]);
var factorial = function(num) {
  if(num == 0) {
    return 1
  } else {
    return num * factorial(num - 1);
  }
}
console.log(factorial(num));
