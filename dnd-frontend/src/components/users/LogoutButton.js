import { useNavigate } from 'react-router-dom';


const LogoutButton = () => {
  const history = useNavigate();

  const Logout = () => {
    localStorage.removeItem('access'); // удалить токен из localStorage
    history('/'); // перенаправить пользователя на страницу входа
    window.location.reload();
  };

  return (
    <button onClick={Logout}>Выход из аккаунта</button>
  );
};

export default LogoutButton;