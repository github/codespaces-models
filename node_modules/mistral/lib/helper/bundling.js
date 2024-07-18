const path = require('path')

// file basename without js-extension
const jsBaseName = (jsFilePath) => path.basename(jsFilePath, '.js')

// the direct parent folder name
const folderName = (filePath) => path.basename(path.dirname(filePath))

const isIndexFile = (libPath) => jsBaseName(libPath) === 'index'

// lib names are usually build by file name. For files named index
// the parent folder name is used instead.
const libName = (libPath) =>
  isIndexFile(libPath) ? folderName(libPath) : jsBaseName(libPath)

// for module path resolution we don't want to have the relative dot path for dir names
const cleanedDirName = (filePath) => {
  const dirName = path.dirname(filePath)
  return dirName === '.' ? '' : dirName
}

// module base path is the target folder the actual module file will be located in
// and is relative to the base path.
const moduleBasePath = (basePath, libPath) => {
  const libFolder = path.dirname(libPath)
  const pathDifference = path.relative(basePath, libFolder)

  return (isIndexFile(libPath)) ? cleanedDirName(pathDifference) : pathDifference
}

module.exports = (config) => ({
  libName,
  jsBaseName,
  isIndexFile,
  folderName,
  moduleBasePath,

  // module file path for the bundling target
  modulePath: (libPath) => path.join(
    config.paths.dist,
    moduleBasePath(config.base, libPath),
    `${libName(libPath)}.js`),

  // module bundles considered as externals for the bundle process
  externals: (bundles) => bundles.map((libPath) => {
    const moduleBase = moduleBasePath(config.base, libPath)

    return moduleBase !== '.' ? `${moduleBase}/${libName(libPath)}` : libName(libPath)
  })
})
