import { useState, useEffect } from 'react'

const API = 'http://localhost:5000/api/users'

function App() {
  const [users, setUsers] = useState([])
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')

  const fetchUsers = () => {
    fetch(API).then(res => res.json()).then(setUsers)
  }

  useEffect(() => { fetchUsers() }, [])

  const addUser = (e) => {
    e.preventDefault()
    fetch(API, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, email })
    }).then(() => {
      setName('')
      setEmail('')
      fetchUsers()
    })
  }

  return (
    <div style={{ padding: '40px', fontFamily: 'Arial', maxWidth: '500px', margin: '0 auto' }}>
      <h1 style={{ color: '#333' }}>User Management</h1>
      <form onSubmit={addUser} style={{ marginBottom: '20px' }}>
        <input
          value={name}
          onChange={e => setName(e.target.value)}
          placeholder="Name"
          required
          style={{ padding: '10px', marginRight: '10px', width: '150px' }}
        />
        <input
          value={email}
          onChange={e => setEmail(e.target.value)}
          placeholder="Email"
          type="email"
          required
          style={{ padding: '10px', marginRight: '10px', width: '180px' }}
        />
        <button type="submit" style={{ padding: '10px 20px', background: '#007bff', color: '#fff', border: 'none', cursor: 'pointer' }}>
          Add User
        </button>
      </form>
      <h2>Users ({users.length})</h2>
      <ul style={{ listStyle: 'none', padding: 0 }}>
        {users.map((u, i) => (
          <li key={i} style={{ padding: '10px', background: '#f5f5f5', marginBottom: '5px', borderRadius: '4px' }}>
            <strong>{u.name}</strong> - {u.email}
          </li>
        ))}
      </ul>
    </div>
  )
}

export default App
