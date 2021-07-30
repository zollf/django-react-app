import React from 'react';
import { render } from '@testing-library/react';

import Home from './index.jsx';

it('matches its snapshot', () => {
  expect(render(<Home />).asFragment()).toMatchSnapshot();
});
