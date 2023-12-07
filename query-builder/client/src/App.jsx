import { useState } from 'react'
import styles from './styles.module.css'
import databaseLogo from './assets/database-storage.png'

import './App.css'

function App() {
// use state to track the query descriptor
  const [queryDescriptor, setQueryDescriptor] = useState("")

  const onSubmit = (e) => {
    e.preventDefault()
    console.log("`action: onSubmit` - form submitted: ", queryDescriptor)
  }

  return (
    <main className={styles.main}>
          <img src={databaseLogo} 
          alt="Database Logo" 
          className={styles.icon}
          style={{ width: '100px', height: '100px' }} 
          />
          <h1>Decision Hub</h1>
          <form onSubmit={onSubmit}>
            <input 
              type="text"
              name="query-descriptor"
              placeholder="Describe your query"
              onChange={(e) => setQueryDescriptor(e.target.value)}
              />
              <input type="submit" value="Generate Query" />
          </form>
    </main>

  )
}

export default App
