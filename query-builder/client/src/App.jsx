import { useState } from 'react'
import styles from './styles.module.css'
import databaseLogo from './assets/database-storage.png'

import './App.css'

function App() {

  return (
    <main className={styles.main}>
          <img src={databaseLogo} 
          alt="Database Logo" 
          className={styles.icon}
          style={{ width: '100px', height: '100px' }} 
          />
          <h1>Decision Hub</h1>
          <form>
            <input 
              type="text"
              name="query-descriptor"
              placeholder="Describe your query"
              />
          </form>
    </main>

  )
}

export default App
