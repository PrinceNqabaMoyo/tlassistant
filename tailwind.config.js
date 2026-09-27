/** @type {import('tailwindcss').Config} */
export default { // <--- Changed this line
  // For Tailwind CSS v4, automatic source detection is usually active.
  // However, keeping this 'content' array can act as a fallback or for clarity.
  content: [
    "./src/**/*.{js,jsx,ts,tsx}", // Essential for Tailwind to scan your React files
    "./public/index.html",
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          blue: '#13519C',
          navy: '#081326',
          cobalt: '#0f3e77',
          sky: '#2B7BD8',
          orange: '#FF9100',
          orangeDark: '#f58200',
          amber: '#FFD166',
        },
      },
      boxShadow: {
        ribbon: '0 4px 14px rgba(255,145,0,0.39)',
        lift: '0 16px 50px rgba(19,81,156,0.14)',
      },
    },
  },
  plugins: [],
}