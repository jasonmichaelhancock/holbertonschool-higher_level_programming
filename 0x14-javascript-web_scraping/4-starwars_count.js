#!/usr/bin/node
// A script that prints the number of movies where the character Wedge Antilles
// is present.

let url = process.argv[2];
let request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    let films = JSON.parse(body).results;
    let count = 0;
    for (let film in films) {
      let chars = films[film].characters;
      for (let char in chars) {
        if (chars[char].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
