import logo from './logo.svg';
import Header from './components/Header';
import Image from './components/Image';
import './App.css';
import './css/main.css'

function App() {
  return (
    <div>
      <Header title="хедер" />
      <Image image={logo} />
    </div>
  );
}

export default App;
