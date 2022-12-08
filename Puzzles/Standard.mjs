import { readFileSync } from "node:fs";

const lines = readFileSync("day??.txt", { encoding: "utf-8" })
  .replace(/\r/g, "")
  .trim()
  .split("\n") 
  .map(Number);
function part1() {
  //do something here
}

function part2() {
  //do something here
}

part1();
part2();