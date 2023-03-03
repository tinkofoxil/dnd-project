import logo from './logo.svg';
import Header from './components/Header';
import Footer from './components/Footer';
import Profiles from './components/Profiles';
import Image from './components/Image';

function App() {
  return (
    <div>
      <Header />
      <div>
        <Profiles/>
      </div>
      <Footer />
    </div>
  );
}

export default App;
