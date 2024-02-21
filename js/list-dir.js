import fs from 'fs'

const srcDir = process.argv[2]

const files =  fs.readdir(srcDir,  function (err, files) { //callback
    if (err) {
        console.log(err)
    } else {
        for (const name of files) {
            console.log(name)
        }
    }

}) 


console.log('last line of program')

