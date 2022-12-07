import { readFileSync } from "node:fs";

//const elves = readFileSync("day01.txt",)
const elves = readFileSync("day01.txt", { encoding: "utf-8" })

elves();