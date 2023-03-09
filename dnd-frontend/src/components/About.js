import React from 'react';
import '../css/about.css';

function About() {
  return (
    <div className="about-container">
      <h1>О проекте</h1>
      <div className="about-info">
        <p>
          Привет, дрогой друг! Я автор проекта DND :) Здесь можно удобно хранить данные профилей/анкет ваших персонажий из ДНД игр.
          Это мой первый опыт создания клиента приложения на React, так что сорьки.
        </p>
      </div>
    </div>
  );
}

export default About;
