#!/usr/bin/node
const request = require('request');
const apiUrl = 'https://jsonplaceholder.typicode.com/todos';
request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const todos = JSON.parse(body);
    let completed = {};

    todos.forEach((todo) => {
      if (todo.completed) {
        if (completed[todo.userId] === undefined) {
          completed[todo.userId] = 1;
        } else {
          completed[todo.userId] += 1;
        }
      }
    });

    for (const userId in completed) {
      console.log(`User ${userId}: ${completed[userId]} completed tasks`);
    }
  } else {
    console.error("Error:", error);
  }
});
