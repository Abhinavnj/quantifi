/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [require('daisyui')],
  daisyui: {
    themes: [
      {
        'custom-dark': {
          'primary': '#ffffff',
          'primary-focus': '#ffffff',
          'primary-content': '#000000',

          'secondary': '#0a0a0a',
          'secondary-focus': '#966321',
          'secondary-content': '#ffffff',

          'accent': '#ffffff',
          'accent-focus': '#ffffff',
          'accent-content': '#000000',

          'neutral': '#333333',
          'neutral-focus': '#4d4d4d',
          'neutral-content': '#ffffff',

          'base-100': '#000000',
          'base-200': '#333333',
          'base-300': '#4d4d4d',
          'base-content': '#ffffff',

          'info': '#3347e1',
          'success': '#45b045',
          'warning': '#f0f024',
          'error': '#d63838',

          '--rounded-box': '0.5rem',
          '--rounded-btn': '0.5rem',
          '--rounded-badge': '0',

          '--animation-btn': '0',
          '--animation-input': '0',

          '--btn-text-case': 'lowercase',
          '--navbar-padding': '.5rem',
          '--border-btn': '1px',
        },
      },
      "black",  // Default light theme
      "light"    // Default dark theme
    ],
  },
}