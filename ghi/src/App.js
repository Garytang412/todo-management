import logo from './logo.svg';
import './App.css';
import { useState, useEffect } from "react";

function App() {
  const [info, setInfo] = useState({});
  useEffect(() => {
    const url = 'http://localhost:8000/account/';
    const fetchConfig = {
      method: 'GET'
    }
    fetch(url, fetchConfig)
      .then(res => res.json())
      .then(data => {
        if (data) setInfo(data)
      }).catch(e => console.error(e))
  }, [])
  return (
    <div>
      <h4>Got data from api:</h4>
      <p>{info.hello}</p>

    </div>
  );
}

export default App;
