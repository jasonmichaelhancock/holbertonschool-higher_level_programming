#!/usr/bin/node
// A script that display the status code of a GET request.

let url = process.argv[2];
let request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log('code:', response && response.statusCode);
  }
});
