import React from 'react';
import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import App from './App';

test('renders App component', () => {
  render(
    <MemoryRouter>
      <App />
    </MemoryRouter>
  );

  // Проверяем, что компоненты Header, Main, Footer отрендерены
  const headerElement = screen.getByTestId('header');
  const mainElement = screen.getByTestId('main');
  const footerElement = screen.getByTestId('footer');

  expect(headerElement).toBeInTheDocument();
  expect(mainElement).toBeInTheDocument();
  expect(footerElement).toBeInTheDocument();
});
