const path = require('path')
const webpack = require('webpack')
const HtmlWebpackPlugin = require('html-webpack-plugin');
const VueLoaderPlugin = require('vue-loader/lib/plugin')

module.exports = {
  entry: './src/main.js',
  plugins: [
    new VueLoaderPlugin(),
    new HtmlWebpackPlugin({
      title: 'IMG Benji',
      //filename: '/home/staticfiles/public/jukenukem/v4/index.html',
      filename: path.resolve(__dirname, './static/index.html'),
      template: 'src/assets/index.html'
    })
  ],
  output: {
    path: path.resolve(__dirname, './static/js/'),
    //path: '/home/staticfiles/public/jukenukem/v4/',
    publicPath: '/static/js/',
    //filename: 'bundle.js'
    filename: '[name].[hash].js'
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          'vue-style-loader',
          'css-loader'
        ],
    },      {
      test: /\.vue$/,
      loader: 'vue-loader',
      options: {
        loaders: {
        }
        // other vue-loader options go here
      }
    },
    {
      test: /\.js$/,
      loader: 'babel-loader',
      exclude: /node_modules/
    },
    {
      test: /\.(png|jpg|gif|svg)$/,
      loader: 'file-loader',
      options: {
        name: '[name].[ext]?[hash]'
      }
    }
  ]
},
resolve: {
    alias: {
      'vue$': 'vue/dist/vue.esm.js'
    },
    extensions: ['*', '.js', '.vue', '.json']
  },
  devServer: {
    host: '0.0.0.0',
    historyApiFallback: true,
    noInfo: true,
    overlay: true,
    disableHostCheck: true
  },
  performance: {
    hints: false
  },
  devtool: '#eval-source-map',
  optimization: {
    minimize: false
  }
}

if (process.env.NODE_ENV === 'production') {
    module.exports.mode = 'production'
    module.exports.optimization.minimize = true
    module.exports.devtool = '#source-map'
    // http://vue-loader.vuejs.org/en/workflow/production.html
    module.exports.plugins = (module.exports.plugins || []).concat([
      new webpack.DefinePlugin({
        'process.env': {
          NODE_ENV: '"production"'
        }
      }),
      new webpack.LoaderOptionsPlugin({
        minimize: true
      })
    ])
  }