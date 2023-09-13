#!/usr/bin/node

function SecondLargest () {
  const args = process.argv.slice(2);
  const integers = args.map(Number).filter(Number.isInteger);
  const uniqInts = Array.from(new Set(integers));

  if (uniqInts.length < 2) {
    console.log(0);
  } else {
    uniqInts.sort((a, b) => b - a);
    console.log(uniqInts[1]);
  }
}

SecondLargest();
