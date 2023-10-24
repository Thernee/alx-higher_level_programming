#!/usr/bin/node
const request = require('request');

const url = 'https://swapi.co/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printChars(characters, 0);
  }
});

function printChars (characters, idx) {
  request(characters[idx], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (idx < characters.length - 1) {
        printChars(characters, idx + 1);
      }
    }
  });
}
