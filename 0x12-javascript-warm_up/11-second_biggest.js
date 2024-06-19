#!/usr/bin/node
/** this is a script that searches the biggest ineger in a list of arguments */
const args = process.argv.slice(2);
const secondBiggest = (args) => {
  const numbers = args.map(Number).filter(num => !isNaN(num));
  if (numbers.length === 0 || numbers.length === 1) {
    console.log(0);
  }
  const sortednums = numbers.sort((a, b) => b - a);
  const secondbiggest = sortednums[1];
  console.log(secondbiggest);
};
