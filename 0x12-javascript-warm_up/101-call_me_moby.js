#!/usr/bin/node
function callMeMoby(x, theFunction) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
};

module.exports.callMeMoby = callMeMoby;
