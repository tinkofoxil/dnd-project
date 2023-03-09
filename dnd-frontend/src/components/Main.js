import React from 'react';
import '../css/main.css';
import character from "../assets/img/character.png"
import monster from "../assets/img/monster.png"
import map from "../assets/img/map.png"

function Main() {
  return (
    <div className="main-page-container">
      <main>
        <section>
          <h2>Добро пожаловать на ДНД сайт</h2>
          <p>Здесь вы можете найти все, что вам нужно для создания своих собственных персонажей, монстров и приключений. Присоединяйтесь к нашему сообществу и делитесь своими творениями с другими игроками!</p>
        </section>
        <section>
          <h2>Рекомендуемый контент</h2>
          <div className="featured-content-container">
            <div className="featured-content-item">
              <img src={character} width="25%" alt="Featured content" />
              <h3>Создать персонажа</h3>
              <p>Создавайте и настраивайте своих собственных персонажей DND с помощью нашего простого в использовании character creator.</p>
            </div>
            <div className="featured-content-item">
              <img src={monster} width="25%" alt="Featured content" />
              <h3>Генератор монстра</h3>
              <p>Создавайте уникальных монстров с помощью нашего генератора монстров. Выбирайте из множества способностей и черт характера.</p>
            </div>
            <div className="featured-content-item">
              <img src={map} width="25%" alt="Featured content" />
              <h3>Планировщик приключений</h3>
              <p>Спланируйте свое следующее приключение с помощью нашего планировщика приключений. Создавайте пользовательские встречи и точки построения.</p>
            </div>
          </div>
        </section>
      </main>
    </div>
  );
}

export default Main;
