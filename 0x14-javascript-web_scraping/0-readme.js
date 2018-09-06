#!/usr/bin/node
// A script that reads and prints the content of a file.

let fs = require('fs');
let file = process.argv[2];
let encoding = 'utf-8';

fs.readFile(file, encoding, function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
