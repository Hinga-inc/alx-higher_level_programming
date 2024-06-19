#!/usr/bin/node

/** this is a script that prints the addition of 2 integers using a function */
const args = process.argv.slice(2);
const a = parseInt(args[0]);
const b = parseInt(args[1]);
function add (a, b) {
  console.log(a + b);
}
add(a, b);
