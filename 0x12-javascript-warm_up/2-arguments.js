#!/usr/bin/node
const args = process.argv.slice(2); // the slice(2) excempts the first 2 arguments

if (args.length === 0) {
    console.log("No argument");
} else if (args.length === 1){
    console.log("Argument found");
} else {
    console.log("Arguments found");
}
// this is a script that prints a message depending on the number of args passed
