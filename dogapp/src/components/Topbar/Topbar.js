import React from 'react';
import { Link } from 'react-router-dom';
import { useLocation } from 'react-router-dom';

function Topbar() {
    const location = useLocation();
    const pathname = location.pathname;

    if (pathname === '/') {
        return (
            <div className='topbar'>
                <Link to="/" className='top_left'>Home</Link>
                <Link className='login' to="/login">Login</Link>
                <Link className='register' to="/register">Register</Link>
            </div>
        )
    }
    if (pathname === "/login" || pathname === "/register") {
        <div className='topbar'>
            <Link to="/" className='top_left'>Home</Link>
            <Link className='register' to={pathname === "/login"? "/register": "/login"}>{pathname === "/login"? "Register": "Login"}</Link>
        </div>
    }
    else {
        <div className='topbar'>
            <Link to="/" className='top_left'>Home</Link>
            <Link className='login' to="/login">Login</Link>
            <Link className='register' to="/register">Register</Link>
        </div>
    }
  }
  
  export default Topbar;