import logo from './logo.svg';
import Header from './components/Header';
import Footer from './components/Footer';
import Profiles from './components/Profiles';
import About from './components/About';
import Main from './components/Main';
import Register from './components/users/Register';
import Login from './components/users/Login';
import { Route, Routes } from 'react-router-dom';
import RegistrationSuccess from './components/users/RegistrationSuccess';

function App() {
  return (
    <div>
      <Header />
      <div>
        <Routes>
          <Route path="/" element={<Main />}/>
          <Route path="/profiles" element={<Profiles />}/>
          <Route path="/about" element={<About />}/>
          <Route path="/register" element={<Register />}/>
          <Route path="/register/success" element={<RegistrationSuccess />}/>
          <Route path="/login" element={<Login />}/>
        </Routes>
      </div>
      <Footer />
    </div>
  );
}

export default App;
