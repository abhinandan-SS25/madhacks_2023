import React from 'react';
import { Link } from 'react-router-dom';

function Home() {
    return (
      <div className='home'>
        <div className="header">
          This is Bark Avenue
        </div>
        <div className="subheader" >
          Here you can find dogs nerby and arrange playdates!
        </div>
        <div className='lowbar flex_center'>
            <Link className='bar flex_center' to="/login">Login</Link>
            <Link className='bar flex_center' to="/register">Register</Link>
        </div>
      </div>
    );
  }
  
  export default Home;