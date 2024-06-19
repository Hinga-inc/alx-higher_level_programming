#!/usr/bin/node

const args = process.argv.slice(2); // the slice(2) excludes the first two arguments

console.log("Arguments received:", args); // Logging the arguments received

if (args.length === 0) {
    console.log("No argument");
} else if (args.length === 1) {
    console.log("Argument found");
} else {
    console.log("Arguments found");
}
