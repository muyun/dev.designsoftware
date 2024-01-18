import fs from 'node:fs'

const listContents = (err, files) => {}
const srcDir = process.argv[2]
const results = fs.readdir(srcDir, listContents)
console.log('last line of program')

