#!/usr/bin/node
// A script that prints x times "C is fun".
let num = Number(process.argv[2]);
let line = ''
if (isNaN(num)) {
  console.log('Missing size');
} else for (i = 0; i < num; i++) {
    line += 'X'
} for (j = 0; j < num; j++) {
      console.log(line);
}
