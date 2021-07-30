const path = require("path");
const webpack = require("webpack");
var glob = require('glob');

module.exports = {
  entry: glob.sync('./frontend/entrypoints/*.jsx*'),
  output: {
    path: path.resolve(__dirname, "./app/resources/static/dist"),
    filename: "bundle.js",
  },
  module: {
    rules: [
      {
        test: /\.jsx$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
        },
      },
    ],
  },
  optimization: {
    minimize: true,
  },
};