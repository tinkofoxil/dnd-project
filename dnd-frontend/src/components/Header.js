import React from 'react';
import { Link } from 'react-router-dom';
import '../css/header.css';

const Header = () => {
  return (
    <header className="header">
      <div className="header__logo">DND :)</div>
      <nav className="header__nav">
        <ul className="header__list">
          <li className="header__item"><Link className="header__link" to="/">Профили</Link></li>
          <li className="header__item"><Link className="header__link" to="/">О проекте</Link></li>
          <li className="header__item"><Link className="header__link" to="/">Регистрация</Link></li>
          <li className="header__item"><Link className="header__link" to="/">Войти</Link></li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;
