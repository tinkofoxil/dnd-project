import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

const Profile = () => {
    const [profile, setProfile] = useState(null);
    const { id } = useParams();
    const [isStatsVisible, setIsStatsVisible] = useState(false);

    useEffect(() => {
        fetch(`http://127.0.0.1:8000/api/v1/profile/${id}`)
        .then((res) => res.json())
        .then((data) => setProfile(data))
        .catch((error) => console.error(error));
    }, []);

    if (!profile) {
        return <div>Loading...</div>;
    }

    return (
        <div className="profile-container" key={profile.pk}>
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
                    </ul> 
                </div>
            </div>
    );
    };

export default Profile;
