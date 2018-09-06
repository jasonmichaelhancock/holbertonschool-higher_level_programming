#!/usr/bin/node
// A script that writes a string to a file.

let fs = require('fs');
let file = process.argv[2];
let str = process.argv[3];

fs.writeFile(file, str, function (err) {
  if (err) console.log(err);
});
