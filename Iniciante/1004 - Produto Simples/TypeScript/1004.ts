import * as fs from "fs";

function main(): void {
  const input: string = fs.readFileSync("/dev/stdin", "utf8");
  const lines: string[] = input.split("\n");
  const valueOne: number = parseInt(lines.shift());
  const valueTwo: number = parseInt(lines.shift());
  const product: number = valueOne * valueTwo;
  console.log(`PROD = ${product}`);
}

main();
