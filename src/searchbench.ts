'use-strict'

import { matchObject } from 'searchjs'
import NanoTimer from 'nanotimer'

import { loadJson } from './loadtxn'
import { percentile } from './percentile'

const TRANSACTION_DATA = './data/event.json'

class FilterBenchmark {

    run(benchmark): void {

        const transaction_data = loadJson(TRANSACTION_DATA)
        const filter_list = loadJson(benchmark)

        filter_list.forEach(function(filter) {
            const percentiles = [5.0, 10.0, 20.0, 50.0, 68.0, 95, 99.7]
            const iteration = 1000

            let match = 0
            let miss  = 0
            let count = 0
            console.log('test: ' + filter.name)
            const query = filter.filter

            const nanoTimer = new NanoTimer()

            const timeArray = []
        
            transaction_data.forEach(event => {
                count++
                const matchEvent = function() {
                    for(let i = 0; i<iteration; ++i) {
                        if(matchObject(event, query)) {
                            match++
                        } else {
                            miss++
                        }
                    }
                }
                const timens = nanoTimer.time(matchEvent, '', 'n')/iteration
                timeArray.push(timens)
            })
        
            timeArray.sort(function(a, b) {return a-b})
            percentiles.forEach(p => {
                console.log(p + '%: ' + percentile(timeArray, p/100.0))
            })
        
            const totalNs = timeArray.reduce(function (a, b) {return a + b}, 0)
            const meanNs = totalNs/timeArray.length
            console.log('transactions   : ' + count)
            console.log('mean time (ns) : ' + meanNs)
            console.log('total time (ms): ' + totalNs/1e6)

            console.log('match: '+match/iteration)
            console.log('miss: '+miss/iteration)
            console.log('')
        })
    }
}

export function searchBenchmark(benchmark:string) {
    const filterBench = new FilterBenchmark()
    filterBench.run(benchmark)
}

