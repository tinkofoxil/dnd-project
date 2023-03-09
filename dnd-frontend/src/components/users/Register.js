import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function Registration() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const history = useNavigate();
  
    const handleSubmit = async (event) => {
      event.preventDefault();
      const response = await fetch('http://127.0.0.1:8000/api/v1/auth/users/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          username: username,
          password: password
        })
      });
      const data = await response.json();
      if (response.ok) {
        localStorage.setItem('token', data.token);
        history.push('/');
      } else {
        setError(data.message);
      }
    };
  
    return (
      <form onSubmit={handleSubmit}>
        <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
        <button type="submit">Register</button>
        {error && <p>{error}</p>}
      </form>
    );
  }

const Register = () => {
  return (
    <div>
        < Registration />
    </div>
  )
};

export default Register;