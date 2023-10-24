#!/usr/bin/node

//import request
const request = require('request');

//const the url
let url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

// use req & log title
request(url, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
