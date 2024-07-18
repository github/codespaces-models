const path = require('path')
const rollup = require('rollup').rollup
const buble = require('rollup-plugin-buble')

const pckg = require(path.join(process.cwd(), 'package.json'))
const config = pckg.config.mistral

const globbing = require('./lib/helper/globbing')(config)
const bundling = require('./lib/helper/bundling')(config)

const buildConfig = {
  bundles: config.bundles,
  paths: {
    dist: config.paths.dist
  }
}

// In this build tool wrapper we decide for rollup (because of its tree-shaking functionality)
// and buble as es6 transpiler.
const bundle = (lib, external) => rollup(Object.assign({}, { external }, {
  entry: lib,
  plugins: [buble()]
}))
.then((bundle) => bundle.write({
  format: config.format,
  dest: bundling.modulePath(lib)
}))
.catch(e => console.log(e))

// Collect all files found by the given glob-patterns and build each file
// as own bundle. To the build process all collected libraries will be configured
// as externals to each other.
Promise.all(buildConfig.bundles.map(bundle => globbing.collect(bundle)))
.then(bundleGlobs => globbing.flatten(bundleGlobs))
.then(bundles => {
  const externalBundles = bundling.externals(bundles)

  return bundles.map(lib => bundle(lib, externalBundles))
})
.then(bundles => Promise.all(bundles))
.then(() => console.log('finished'))
.catch(e => console.log(e))
