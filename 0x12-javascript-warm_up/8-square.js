#!/usr/bin/node

/** this is a script that prints a square the first argument being the size of the square */
const args = process.argv.slice(2); /* the slice(2) excempts the first 2 arguments */
const size = parseInt(args[0]);/* the parseint converts the argument which is an array to an integer */
if (isNaN(size)) { /* the isNaN checks if the number is a NUmber */
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
