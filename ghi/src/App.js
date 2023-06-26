import logo from './logo.svg';
import './App.css';
import { useState, useEffect } from "react";

function App() {
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const signup = (e) => {
    e.preventDefault();
    const signupData = {
      'username': username,
      'email': email,
      'password': password
    };
    const signupUrl = 'http://localhost:8000/account/signup/';
    const fetchConfig = {
      method: 'POST',
      mode: 'cors',
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(signupData)
    };
    fetch(signupUrl, fetchConfig)
      .then(res => res.json())
      .then(data => console.log(data))
      .catch(e => console.error(e))
  }
  const logout = e => {
    const logoutUrl = 'http://localhost:8000/account/logout/';
  }


  return (
    <div>
      <form onSubmit={signup}>
        <lable>username:</lable> <input type="text" value={username} onChange={e => setUsername(e.target.value)} />
        <lable>email:</lable> <input type="email" value={email} onChange={e => setEmail(e.target.value)} />
        <lable>password:</lable> <input type="password" value={password} onChange={e => setPassword(e.target.value)} />
        <br />
        <button>signup</button>
      </form>
      <div>
        <button onClick={logout}>logout</button>
      </div>
    </div>
  );
}

export default App;
