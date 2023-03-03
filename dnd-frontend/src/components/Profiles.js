import React, { useEffect, useState } from 'react';
import '../css/profiles.css'

const baseUrl = "http://127.0.0.1:8000/api/v1/profile/"

function Profiles() {
    const [data, setData] = useState([]);

    useEffect(() => {
        fetch(baseUrl, {
            method: 'GET',
        }).then(response => response.json()).then((data) => setData(data));
    }, []);

    return (
        <div>
          {data.results.map(item => (
            <div className="profile-container" key={item.pk}>
                <div className="profile-header">
                    <h1>{item.name}</h1>
                    <img src={item.image} alt="Character Portrait"/>
                </div>
                <div className="profile-body">
                    <div className="profile-section">
                        <h2>Basic Info</h2>
                        <ul>
                            <li>Race: {item.race}</li>
                            <li>Class: {item.class_name}</li>
                            <li>Level: {item.level}</li>
                        </ul>
                    </div>
                </div>
            </div>
          ))};
        </div>
    );

}

export default Profiles