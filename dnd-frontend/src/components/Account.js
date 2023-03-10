import React from 'react';
import LogoutButton from './users/LogoutButton';
import "../css/account.css"

const Account = () => {

  return (
    <div className='AccountPage'>
      <h1>Аккаунт</h1>
      <LogoutButton />
    </div>
  );
};

export default Account;
