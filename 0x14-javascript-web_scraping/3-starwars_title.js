#!/usr/bin/node
// A script that prints the title of a Star Wars movie where the episode number
// matches a given integer.

let epnum = process.argv[2];
let url = 'http://swapi.co/api/films/' + epnum;
let request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
