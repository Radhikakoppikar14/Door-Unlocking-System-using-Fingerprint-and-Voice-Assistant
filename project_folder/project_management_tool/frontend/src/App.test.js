import { render, screen } from '@testing-library/react';
import App from './App';

test('renders projects heading', () => {
  render(<App />);
  const linkElement = screen.getByText(/Projects/i);
  expect(linkElement).toBeInTheDocument();
});
