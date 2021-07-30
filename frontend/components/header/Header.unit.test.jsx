import React from 'react';
import { render } from '@testing-library/react';

import Header from './index.jsx';

it('matches its snapshot', () => {
  expect(render(<Header />).asFragment()).toMatchSnapshot();
});
