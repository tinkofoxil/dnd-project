import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

const Profile = ({ match }) => {
  const [profile, setProfile] = useState(null);
  const { id } = useParams();

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/api/v1/profile/${id}`)
      .then((res) => res.json())
      .then((data) => setProfile(data))
      .catch((error) => console.error(error));
  }, []);

  if (!profile) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>{profile.name}</h1>
      <p>{profile.age}</p>
    </div>
  );
};

export default Profile;
