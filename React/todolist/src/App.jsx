import { useState } from 'react'


function App() {
  const [toDo, setToDo] = useState('')
  const [toDos, setToDos] = useState([])

  const onChange = (event) => setToDo(event.target.value)
  const onSubmit = (event) => {
    event.preventDefault()
    if (toDo === '') {
      return
    }
    setToDos(currentArray => [toDo, ...currentArray])
    setToDo('')
  }
  console.log(toDos)

  return (
    <>
      <h1>My todos({toDos.length})</h1>
      <form onSubmit={onSubmit}>
        <input 
          value={toDo} 
          type="text" 
          placeholder='Write your Todo!' 
          onChange={onChange}
        />
        <button>Add To Do</button>
      </form>

      <hr />

      <ul>
        {toDos.map((item, index) => 
          <li key={index}>{item}</li>
        )}
      </ul>
    </>
  )
}

export default App
