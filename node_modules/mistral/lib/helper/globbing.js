const path = require('path')
const denodeify = require('denodeify')

const glob = denodeify(require('glob'))

// provided glob patterns should be relative to the base path.
const prefixGlobPattern = (basePath, globPattern) => path.join(basePath, globPattern)

module.exports = (config) => ({
  _: {
    prefixGlobPattern
  },

  // array flattenig
  flatten: (list) => list.reduce((collection, entry) => collection.concat(entry), []),

  // file list for the bundle glob pattern
  collect: (bundle) => glob(prefixGlobPattern(config.base, bundle))
})
