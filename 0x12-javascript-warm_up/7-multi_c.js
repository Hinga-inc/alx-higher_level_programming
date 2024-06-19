#!/usr/bin/node

/** this is a script that prints x times 'c is fun' where x is the first argument of the script */

const args = process.argv.slice(2); /* the slice(2) excempts the first 2 arguments */
const myError = 'Missing number of occurrences';
const mysentence = 'C is fun';
const number = parseInt(args[0]);/* the parseint converts the argument which is an array to an integer */
if (isNaN(number)) { /* the isNaN checks if the number is a NUmber */
  console.log(myError);
} else {
  for (let i = 0; i < number; i++) {
    console.log(mysentence);
  }
}
