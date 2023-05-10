import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { Link } from 'react-router-dom';


const Profile = () => {
    const [profile, setProfile] = useState(null);
    const { id } = useParams();
    const [isProfileDeleted, setIsProfileDeleted] = useState(false);
    const userId = localStorage.getItem('user_id');
    const history = useNavigate();

    useEffect(() => {
        fetch(`http://127.0.0.1:8000/api/v1/profile/${id}`)
        .then((res) => res.json())
        .then((data) => setProfile(data))
        .catch((error) => console.error(error));
    }, [id]);

    const handleDeleteProfile = () => {
        fetch(`http://127.0.0.1:8000/api/v1/profile/${id}/`, {
            method: 'DELETE',
            headers: { Authorization: `Bearer ${localStorage.getItem('access')}` }
        })
        .then(() => {
            setIsProfileDeleted(true);
            setTimeout(() => {
                setIsProfileDeleted(false);
                history('/profiles');
            }, 3000); // устанавливаем таймер на 3 секунды
        })
        .catch((error) => console.error(error));
    };

    if (!profile) {
        return <div>Loading...</div>;
    }

    return (
        <div className="profile-container" key={profile.pk}>
        {isProfileDeleted && <div className="notification">Профиль был успешно удален!</div>}
            <div className="profile-header">
                <h1>{profile.name}</h1>
                <img src={profile.image} alt="Character Portrait"/>
            </div>
            <div className="profile-body">
                <div className="profile-section">
                    <ul>
                        <li>Возраст: {profile.age} </li>  
                        <li>Раса: {profile.race}</li>
                        <li>Класс: {profile.class_name}</li>
                        <li>Уровень: {profile.level}</li>
                    </ul> 
                </div>
            </div>
            <div className="profile-section">
                <ul>
                    <li>Описание: {profile.description}</li>
                    <li><Link className='profile-link' to={`/account/${profile.user_id}`}>Автор: {profile.user}</Link></li>
                    {profile.user_id === parseInt(userId) && <li><button onClick={handleDeleteProfile}>Удалить профиль</button></li>}
                </ul> 
            </div>
        </div>
    );
    };

export default Profile;
