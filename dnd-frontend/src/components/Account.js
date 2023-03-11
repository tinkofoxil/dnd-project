import React, {useEffect, useState} from 'react';
import LogoutButton from './users/LogoutButton';
import axios from 'axios';
import "../css/account.css"

const Account = () => {

  const [user, setUser] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      try {
        const result = await axios.get('http://127.0.0.1:8000/api/v1/auth/users/me', {
          headers: { Authorization: `Bearer ${localStorage.getItem('access')}` }
        });
        setUser(result.data);
      } catch (error) {
        console.error(error);
      }
    };
    fetchData();
  }, []);

  return (
    <div className='AccountPage'>
      <h1>Аккаунт</h1>
      <h3>Имя пользователя: {user.username}</h3>
      <LogoutButton />
    </div>
  );
};

export default Account;
