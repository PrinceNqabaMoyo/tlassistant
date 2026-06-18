import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc' // Use @vitejs/plugin-react-swc for JavaScript + SWC variant
import tailwindcss from '@tailwindcss/vite' // Import the Tailwind CSS Vite plugin

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    react(),
    tailwindcss(), // Add this line
  ],
})