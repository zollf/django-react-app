const path = require('path');
const glob = require('glob');

const files = {};
glob.sync('./frontend/entrypoints/*.jsx*').forEach((s) => {
  files[s.split('/').slice(-1)[0].replace('.jsx', '')] = s;
});

module.exports = {
  entry: files,
  output: {
    path: path.resolve(__dirname, './app/resources/static/dist'),
    filename: '[name].bundle.js'
  },
  module: {
    rules: [
      {
        test: /\.jsx$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader'
        }
      }
    ]
  },
  optimization: {
    minimize: true
  }
};
