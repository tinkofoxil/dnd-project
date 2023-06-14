import React, {useEffect, useState} from 'react';
import { Link, useParams } from 'react-router-dom';
import axios from 'axios';
import "../css/account.css"
import Account from './Account';

const UserAccount = () => {

  const [user, setUser] = useState({});
  const userId = localStorage.getItem('user_id');
  const [profile, setProfile] = useState({});
  const [error, setError] = useState('');
  const [isFriendAdded, setIsFriendAdded] = useState(false);
  const { id } = useParams();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const result = await axios.get(`http://127.0.0.1:8000/api/v1/users/${id}`, {
          headers: { Authorization: `Bearer ${localStorage.getItem('access')}` }
        });
        await fetch(`http://127.0.0.1:8000/api/v1/user/${result.data.pk}/profiles`)
        .then((res) => res.json())
        .then((data) => setProfile(data))
        .catch((error) => console.error(error));
        setUser(result.data);
      } catch (error) {
        console.error(error);
      }
    };
    fetchData();
  }, [id]);

  if (user.id !== parseInt(userId)) {
    return (
    <div>
    <div className='account-page'>
      {isFriendAdded && <div className="notification">Успешное добавление в друзья!</div>}
      <div className="account-container">
        <h1>Аккаунт</h1>
        <h3>Имя пользователя: {user.username}</h3>
          <button 
            onClick={() => {
              axios.post(`http://127.0.0.1:8000/api/v1/users/${id}/friend/`, {}, {
                  headers: { Authorization: `Bearer ${localStorage.getItem('access')}` }
              })
              .then((response) => {
                  console.log(response);
                  setIsFriendAdded(true);
              })
              .catch((error) => {
                  setError(error.response.data.non_field_errors)
              });
            }}>
            Добавить в друзья
          </button>
      </div>
      {error && <div className='notification'>{error}</div>}
    <div>
      {profile.results?.map(item => (
        <div className="account-profile-container" key={item.pk}>
            <div className="account-profile-header">
                <h1>{item.name}</h1>
                <img src={item.image} alt="Character Portrait"/>
            </div>
            <div className="account-profile-body">
                <div className="account-profile-section">
                    <h2>Краткая инфа</h2>
                    <ul>
                        <li>Возраст: {item.age}</li>  
                        <li>Раса: {item.race}</li>
                        <li>Класс: {item.class_name}</li>
                        <li>Уровень: {item.level}</li>
                        <li><Link className='account-profile-link' to={`/profiles/${item.pk}`}>Больше инфы</Link></li>
                    </ul> 
                </div>
            </div>
        </div>
      ))}
    </div>
    </div>
    </div>
  );
  } else {
    return <Account />
  }
};

export default UserAccount;
