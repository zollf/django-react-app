module.exports = {
  cacheDirectory: 'node_modules/.cache/jest',
  collectCoverage: true,
  collectCoverageFrom: [
    'frontend/components/**/*.jsx',
    '!frontend/entrypoints/*.jsx'
  ],
  setupFilesAfterEnv: ['<rootDir>/frontend/tests/setupTests.js'],
  testEnvironment: 'jsdom'
};
