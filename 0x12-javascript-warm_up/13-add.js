#!/usr/bin/node
/** this is a script that returns the addition of 2 integers that is visible from outside */

const add = (a, b) => {
  return a + b;
};
module.exports = { add };
