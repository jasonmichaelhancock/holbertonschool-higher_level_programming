#!/usr/bin/node
// A script that searches the second biggest integer in the list of arguments.
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = [];
  for (let i = 3; i <= process.argv.length; i++) {
    args.push(Number(process.argv[i - 1]));
  } console.log(args.sort(function (a, b) { return a - b; }).reverse()[1]);
}
