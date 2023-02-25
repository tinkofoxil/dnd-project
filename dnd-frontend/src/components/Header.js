import React from "react";
import "../css/bootstrap.min.css"

class Header extends React.Component {
    render() {
        return (
            <header class="p-3 text-bg-dark">
            <div class="container">
              <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
                <a href="/" class="d-flex align-items-center mb-2 mb-lg-0 text-white text-decoration-none">
                  <svg class="bi me-2" width="40" height="32" role="img" aria-label="Bootstrap"></svg>
                </a>
        
                <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
                  <li><a href="#" class="nav-link px-2 text-secondary">Home</a></li>
                  <li><a href="#" class="nav-link px-2 text-white">Профили</a></li>
                  <li><a href="#" class="nav-link px-2 text-white">Игры</a></li>
                  <li><a href="#" class="nav-link px-2 text-white">О проекте</a></li>
                </ul>
        
                <div class="text-end">
                  <button type="button" class="btn btn-outline-light me-2">Вход</button>
                  <button type="button" class="btn btn-warning">Регистрация</button>
                </div>
              </div>
            </div>
          </header>
        )
    }
}

export default Header