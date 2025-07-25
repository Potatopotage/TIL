import { useState, useEffect } from 'react'

function App() {
  const [loading, setLoading] = useState(true)
  const [coins, setCoins] = useState([])
  
  useEffect(() => {
    fetch('https://api.coinpaprika.com/v1/tickers')
    .then((response) => response.json())
    .then((json) => {
      setCoins(json)
      setLoading(false)
    })
  }, [])

  return (
    <>
      <h1>The coins!</h1>
      {loading ? <strong>Loading...</strong> : null}
      <ul>
        {coins.map((coin, index) => (
          <li key={index}>{coin.id}</li>
        ))}
      </ul>
    </>
  )
}

export default App
