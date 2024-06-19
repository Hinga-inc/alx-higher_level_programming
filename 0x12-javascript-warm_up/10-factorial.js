#!/usr/bin/node

/** this is a scripts that computes and prints a factorial */
const args = process.argv.slice(2);
const num = parseInt(args[0]);
function factorial (num) {
  if (num <= 1) {
    return 1;
  }
  return num * factorial(num - 1);
}

if (isNaN(num)) {
  console.log(1);
} else {
  console.log(factorial(num));
}
