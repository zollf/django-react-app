import React from 'react';
import { render } from 'react-dom';
import Header from '../components/header/index.jsx';

const header = document.getElementById('react-header');
render(<Header />, header);