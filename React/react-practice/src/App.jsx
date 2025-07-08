import Button from './button.jsx'
import styles from './App.module.css'
import { useState, useEffect } from 'react'

function App() {
  const [counter, setValue] = useState(0)
  const onClick = () => setValue((prev) => prev + 1)

  const [keyword, setKeyword] = useState('')
  const onChange = (event) => setKeyword(event.target.value)

  return (
    <>
      <div>
        <input type="text" placeholder='Search here' onChange={onChange} />
        <p>I'm searching for {keyword}</p>
        <h1>{counter}</h1>
        <button onClick={onClick}>clickme!</button>
      </div>
    </>
  )
}

export default App
