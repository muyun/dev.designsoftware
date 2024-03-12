// singleton design pattern
// this pattern ensures a class only has one instance, and provides a global point of access to it
// 
import assert from 'assert'
import caller from 'caller'


class Hope {
    //state of tests
    constructor() {
        this.hopeTests = []
        this.passes = []
        this.fails = []
        this.errors = []
    }

    // record a single test for running later 
    test(message, callback) {
        this.hopeTests.push([`${caller()}::${message}`, callback])
    }

    run() {
        this.hopeTests.forEach(([message, test]) => {
            try {
                test()
                this.passes.push(message)
            } catch (e) {
                if (e instanceof assert.AssertionError) {
                    this.fails.push(message)
                } else {
                    this.errors.push(message)
                }
            }
            
        })  
    }

    terse() {
        return this.cases().map(([title, results]) => `${title}: ${results.length}`).join(' ')
        
    }

    verbose() {
        let report = ''
        let prefix = ''
        for (const [title, results] of this.cases()) {
          report += `${prefix}${title}:`
          prefix = '\n'
          for (const r of results) {
            report += `${prefix}  ${r}`
          }
        }
        return report
      }

    cases() {
        return [
            ['passes', this.passes],
            ['fails', this.fails],
            ['errors', this.errors]
        ]

    }
}

export default new Hope()


//import hope from './hope.js'
//var hope = new Hope()
//hope.test('Quotient of 1 and 0', () => assert((1 / 0) === 0))
//hope.run()
//console.log(hope.verbose())
