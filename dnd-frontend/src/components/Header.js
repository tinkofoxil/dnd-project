import React from 'react';
import { Link } from 'react-router-dom';
import '../css/header.css';

const Header = () => {
  return (
    <>
      <header className="header">
        <div className="header__logo">
          <Link className="header__link" to="/">DND :)</Link>
        </div>
        <nav className="header__nav">
          <ul className="header__list">
            <li className="header__item"><Link className="header__link" to="/profiles">Профили</Link></li>
            <li className="header__item"><Link className="header__link" to="/about">О проекте</Link></li>
            <li className="header__item"><Link className="header__link" to="/register">Регистрация</Link></li>
            <li className="header__item"><Link className="header__link" to="/login">Войти</Link></li>
          </ul>
        </nav>
      </header>
    </>
  );
};

export default Header;
