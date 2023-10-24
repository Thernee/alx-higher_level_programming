#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).results;
    let count = 0;
    for (const movie in results) {
      const filmChars = results[movie].characters;
      for (const idx in filmChars) {
        if (filmChars[idx].includes('18')) count++;
      }
    }
    console.log(count);
  }
});
