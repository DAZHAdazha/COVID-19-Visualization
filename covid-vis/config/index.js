'use strict'
// Template version: 1.3.1
// see http://vuejs-templates.github.io/webpack for documentation.

const path = require('path')

module.exports = {
  dev: {
    // Paths
    assetsSubDirectory: 'static',
    assetsPublicPath: '/',
    proxyTable: {
      // 对应的域名代理,通过这种方法来完成http跨域请求
      '/api': {
        target: 'https://interface.sina.cn/news/wap/fymap2020_data.d.json',
        changeOrigin: true,
        pathRewrite: {
          '^/api': ''
        }
      },
      '/news': {
        target: 'https://api.yonyoucloud.com/apis/dst/ncov/query',// 接口的域名
        changeOrigin: true,
        pathRewrite: {
          '^/news': ''//后面可以使重写的新路径，一般不做更改
        }
      },
      '/globalrank':{
        target:'https://corona.lmao.ninja/v2/countries?yesterday&sort=cases',
        changeOrigin: true,
        pathRewrite: {
          '^/globalrank': ''//后面可以使重写的新路径，一般不做更改
        }
      },
      '/globaldata':{
        target:'https://corona.lmao.ninja/v2/all?yesterday',
        changeOrigin: true,
        pathRewrite: {
          '^/globaldata': ''//后面可以使重写的新路径，一般不做更改
        }
      },
      '/baidu':{
        target:'http://index.baidu.com/api/WordGraph/multi?wordlist%5B%5D=%E7%96%AB%E6%83%85',
        changeOrigin: true,
        pathRewrite: {
          '^/baidu': ''//后面可以使重写的新路径，一般不做更改
        }
      },
      '/rumors_search':{
        target:'http://localhost:5000/rumors_search',
        changeOrigin: true,
        pathRewrite: {
          '^/rumors_search': ''//后面可以使重写的新路径，一般不做更改
        }
      },
    },

    // Various Dev Server settings
    host: 'localhost', // can be overwritten by process.env.HOST
    port: 8080, // can be overwritten by process.env.PORT, if port is in use, a free one will be determined
    autoOpenBrowser: false,
    errorOverlay: true,
    notifyOnErrors: true,
    poll: false, // https://webpack.js.org/configuration/dev-server/#devserver-watchoptions-

    // Use Eslint Loader?
    // If true, your code will be linted during bundling and
    // linting errors and warnings will be shown in the console.
    useEslint: true,
    // If true, eslint errors and warnings will also be shown in the error overlay
    // in the browser.
    showEslintErrorsInOverlay: false,

    /**
     * Source Maps
     */

    // https://webpack.js.org/configuration/devtool/#development
    devtool: 'cheap-module-eval-source-map',

    // If you have problems debugging vue-files in devtools,
    // set this to false - it *may* help
    // https://vue-loader.vuejs.org/en/options.html#cachebusting
    cacheBusting: true,

    cssSourceMap: true
  },

  build: {
    // Template for index.html
    index: path.resolve(__dirname, '../dist/index.html'),

    // Paths
    assetsRoot: path.resolve(__dirname, '../dist'),
    assetsSubDirectory: 'static',
    assetsPublicPath: '/',

    /**
     * Source Maps
     */

    productionSourceMap: true,
    // https://webpack.js.org/configuration/devtool/#production
    devtool: '#source-map',

    // Gzip off by default as many popular static hosts such as
    // Surge or Netlify already gzip all static assets for you.
    // Before setting to `true`, make sure to:
    // npm install --save-dev compression-webpack-plugin
    productionGzip: false,
    productionGzipExtensions: ['js', 'css'],

    // Run the build command with an extra argument to
    // View the bundle analyzer report after build finishes:
    // `npm run build --report`
    // Set to `true` or `false` to always turn it on or off
    bundleAnalyzerReport: process.env.npm_config_report
  }
}
