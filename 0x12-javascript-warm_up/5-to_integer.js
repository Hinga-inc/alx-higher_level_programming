#!/usr/bin/node

/* this is a script that prints My number: <first argumnet converted into an integer> if it can */
const args = process.argv.slice(2); /* the slice(2) excempts the first 2 arguments */
if (args === NaN) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(args[0]));
}
