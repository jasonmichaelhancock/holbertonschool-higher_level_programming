#!/usr/bin/node
// A script that prints two arguments passed to it, in this format: " is ".
if (process.argv.length < 3) {
  console.log('undefined is undefined');
} else {
  console.log(process.argv[2], 'is', process.argv[3]);
}
