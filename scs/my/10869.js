const readline = require("readline")

const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
})

let input

rl.on("line", line => {
	input = line.split(" ").map(num => Number(num))
	rl.close()
})
rl.on("close", () => {
	const [ a, b ] = input
	console.log(a + b)
	console.log(a - b)
	console.log(a * b)
	console.log(Math.trunc(a / b))
	console.log(a % b)
})