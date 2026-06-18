/** @type {import('tailwindcss').Config} */
export default { // <--- Changed this line
  // For Tailwind CSS v4, automatic source detection is usually active.
  // However, keeping this 'content' array can act as a fallback or for clarity.
  content: [
    "./src/**/*.{js,jsx,ts,tsx}", // Essential for Tailwind to scan your React files
    "./public/index.html",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}