import logo from './logo.svg';
import Header from './components/Header';
import Footer from './components/Footer';
import Profiles from './components/Profiles';
import About from './components/About';
import Image from './components/Image';
import Register from './components/users/Register';
import { Route, Routes } from 'react-router-dom';

function App() {
  return (
    <div>
      <Header />
      <div>
        <Routes>
          <Route path="/profiles" element={<Profiles />}/>
          <Route path="/about" element={<About />}/>
          <Route path="/register" element={<Register />}/>
        </Routes>
      </div>
      <Footer />
    </div>
  );
}

export default App;
