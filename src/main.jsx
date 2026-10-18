import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import '@fontsource/afacad'
import './index.css'
import App from './App.jsx'
import studentStore from './services/studentStore'

if (typeof window !== 'undefined') {
  window.studentStore = studentStore;
}

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
