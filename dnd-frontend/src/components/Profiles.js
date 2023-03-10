import React, { useEffect, useState } from 'react';
import axios from 'axios';
import '../css/profiles.css'
import '../css/pagination.css'

const Profiles = () => {
    const [data, setData] = useState([]);
    const [offset, setOffset] = useState(0);
    const limit = 5;
    const [next, setNext] = useState(null);
    const [previous, setPrevious] = useState(null);
    const [count, setCount] = useState(0)

    useEffect(() => {
        const fetchData = async () => {
            const response = await axios.get(`http://127.0.0.1:8000/api/v1/profile/?limit=${limit}&offset=${offset}`);
            setNext(response.data.next);
            setPrevious(response.data.previous);
            setData(response.data);
            setCount(response.data.count);
        };
        fetchData();
    }, [offset]);

    function handlePaginationClick(newOffset) {
        setOffset(newOffset);
    }

    const pages = Math.ceil(count / limit);
    const currentPage = Math.ceil(offset / limit) + 1;

    return (
        <div>
          {data.results?.map(item => (
            <div className="profile-container" key={item.pk}>
                <div className="profile-header">
                    <h1>{item.name}</h1>
                    <img src={item.image} alt="Character Portrait"/>
                </div>
                <div className="profile-body">
                    <div className="profile-section">
                        <h2>Basic Info</h2>
                        <ul>
                            <li>Age: {item.age}</li>  
                            <li>Race: {item.race}</li>
                            <li>Class: {item.class_name}</li>
                            <li>Strength: {item.strength}</li>
                            <li>Level: {item.level}</li>
                        </ul>
                    </div>
                </div>
            </div>
          ))}
            <div className='pagination'>
            {previous && (
                <button onClick={() => handlePaginationClick(offset - limit)}>
                Предыдущая
                </button>
            )}
            {Array.from(Array(pages).keys()).map((page) => (
                <button key={page} onClick={() => handlePaginationClick(page * limit)} className={currentPage === page + 1 ? 'active' : ''}>
                    {page + 1}
                </button>
            ))}
            {next && (
                <button onClick={() => handlePaginationClick(offset + limit)}>
                Следующая
                </button>
            )}
            </div>
        </div>
    );

}

export default Profiles