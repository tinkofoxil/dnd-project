import axios from 'axios';
import React, { useState } from "react";
import { useNavigate } from 'react-router-dom';
import "../css/profileCreate.css"

const ProfileCreate = () => {
    const [name, setName] = useState("");
    const [age, setAge] = useState("");
    const [image, setImage] = useState(null);
    const [gender, setGender] = useState("N");
    const [race, setRace] = useState("");
    const [class_name, setClassName] = useState("");
    const [level, setLevel] = useState("");
    const [charisma, setCharisma] = useState("");
    const [description, setDescription] = useState("");
    const [strength, setStrength] = useState("");
    const [dexterity, setDexterity] = useState("");
    const [constitution, setConstitution] = useState("");
    const [intelligence, setIntelligence] = useState("");
    const [wisdom, setWisdom] = useState("");
    const history = useNavigate();

    const handleSubmit = async (e) => {
      e.preventDefault();
      const token = localStorage.getItem("git ");
       // получение токена из локального хранилища
      try {
        const response = await axios.post(
          "http://127.0.0.1:8000/api/v1/profile/",
          { name, image, age, gender, race, class_name, level, charisma, description, strength, dexterity, constitution, intelligence, wisdom },
          {
            headers: {
              Authorization: `Bearer ${token}`,
              'Content-Type': 'multipart/form-data',
            },
          }
        );
        setName("");
        setImage("");
        setAge("");
        setGender("");
        setRace("");
        setClassName("");
        setLevel("");
        setCharisma("");
        setDescription("");
        setStrength("");
        setDexterity("");
        setConstitution("");
        setIntelligence("");
        setWisdom("");
        if (response.ok) {
          history('/');
        }
      } catch (error) {
        console.error(error);
      }
    };
  
    return (
      <form className="ProfileCreate" onSubmit={handleSubmit}>
        <h2>Создать персонажа</h2>
        <div >
          <label htmlFor="name">Имя:</label>
          <input
            type="text"
            id="name"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="image">Фотка:</label>
          <input type="file" id="image" onChange={(e) => setImage(e.target.files[0])} />
        </div>
        <div>
          <label htmlFor="age">Возраст:</label>
          <input
            type="number"
            id="age"
            value={age}
            onChange={(e) => setAge(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="gender">Гендер</label>
          <select id="gender" value={gender} onChange={(e) => setGender(e.target.value)}>
            <option value="W">Женщина</option>
            <option value="M">Мужчина</option>
            <option value="N">ХЗ</option>
          </select>
        </div>
        <div>
          <label htmlFor="race">Раса:</label>
          <input
            type="text"
            id="race"
            value={race}
            onChange={(e) => setRace(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="class_name">Класс:</label>
          <input
            type="text"
            id="class_name"
            value={class_name}
            onChange={(e) => setClassName(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="level">Уровень:</label>
          <input
            type="number"
            id="level"
            value={level}
            onChange={(e) => setLevel(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="charisma">Харизма:</label>
          <input
            type="number"
            id="charisma"
            value={charisma}
            onChange={(e) => setCharisma(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="description">Описание:</label>
          <textarea id="description" value={description} onChange={(e) => setDescription(e.target.value)} />
        </div>
        <div>
          <label htmlFor="strength">Сила:</label>
          <input
            type="number"
            id="strength"
            value={strength}
            onChange={(e) => setStrength(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="dexterity">Ловкость:</label>
          <input
            type="number"
            id="dexterity"
            value={dexterity}
            onChange={(e) => setDexterity(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="constitution">Телосложение:</label>
          <input
            type="number"
            id="constitution"
            value={constitution}
            onChange={(e) => setConstitution(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="intelligence">Интеллект:</label>
          <input
            type="number"
            id="intelligence"
            value={intelligence}
            onChange={(e) => setIntelligence(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="wisdom">Мудрость:</label>
          <input
            type="number"
            id="wisdom"
            value={wisdom}
            onChange={(e) => setWisdom(e.target.value)}
          />
        </div>
        <button type="submit">Создать</button>
      </form>
    );
  };
  
  export default ProfileCreate;