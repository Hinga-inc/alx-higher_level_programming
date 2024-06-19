#!/usr/bin/node

// this is a script that prints the first argument passed to it
const args = process.argv.slice(2); // the slice(2) excempts the first 2 arguments
if (args === 0) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
