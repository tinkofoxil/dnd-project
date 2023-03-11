import logo from './logo.svg';
import Header from './components/Header';
import Footer from './components/Footer';
import Profiles from './components/Profiles';
import Profile from './components/Profile';
import About from './components/About';
import Main from './components/Main';
import Register from './components/users/Register';
import Login from './components/users/Login';
import Account from './components/Account';
import ProfileCreate from './components/ProfileCreate';
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
          <Route path="/profiles/:id" element={<Profile />}/>
          <Route path="/profile_create" element={<ProfileCreate />}/>
          <Route path="/about" element={<About />}/>
          <Route path="/register" element={<Register />}/>
          <Route path="/register/success" element={<RegistrationSuccess />}/>
          <Route path="/account" element={<Account />}/>
          <Route path="/login" element={<Login />}/>
        </Routes>
      </div>
      <Footer />
    </div>
  );
}

export default App;
