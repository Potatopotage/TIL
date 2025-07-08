import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client' // 이 줄 추가!
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
