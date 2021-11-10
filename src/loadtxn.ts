'use-strict'

import fs from 'fs'

export function loadJson(path: string) {
    const json_data = fs.readFileSync(path, 'utf8')
    const json = JSON.parse(json_data)
    return json
}
