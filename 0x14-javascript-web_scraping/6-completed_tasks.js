#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const tasks = JSON.parse(body);
    const completed = tasks.reduce((acc, task) => {
      if (task.completed === true) {
        acc[task.userId] = (acc[task.userId] || 0) + 1;
      }
      return acc;
    }, {});
    console.log(completed);
  }
});
