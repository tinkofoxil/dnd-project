import React, {useEffect, useState} from 'react';
import { useParams } from "react-router-dom";
import { Link } from 'react-router-dom';
import LogoutButton from './users/LogoutButton';
import axios from 'axios';
import "../css/account.css"

const Account = () => {

  const [user, setUser] = useState({});
  const [profile, setProfile] = useState({});
  const { id } = useParams();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const result = await axios.get('http://127.0.0.1:8000/api/v1/auth/users/me', {
          headers: { Authorization: `Bearer ${localStorage.getItem('access')}` }
        });
        await fetch(`http://127.0.0.1:8000/api/v1/user/${result.data.id}/profiles`)
        .then((res) => res.json())
        .then((data) => setProfile(data))
        .catch((error) => console.error(error));
        setUser(result.data);
      } catch (error) {
        console.error(error);
      }
    };
    fetchData();
  }, []);

  return (
    <div>
    <div className='AccountPage'>
      <h1>Аккаунт</h1>
      <h3>Имя пользователя: {user.username}</h3>
      <LogoutButton />
    </div>
    <div>
      {profile.results?.map(item => (
        <div className="profile-container" key={item.pk}>
            <div className="profile-header">
                <h1>{item.name}</h1>
                <img src={item.image} alt="Character Portrait"/>
            </div>
            <div className="profile-body">
                <div className="profile-section">
                    <h2>Краткая инфа</h2>
                    <ul>
                        <li>Возраст: {item.age}</li>  
                        <li>Раса: {item.race}</li>
                        <li>Класс: {item.class_name}</li>
                        <li>Уровень: {item.level}</li>
                        <li><Link className='profile-link' to={`/profiles/${item.pk}`}>Больше инфы</Link></li>
                    </ul> 
                </div>
            </div>
        </div>
      ))}
    </div>
    </div>
  );
};

export default Account;
