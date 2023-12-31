import React from 'react';
import { Link } from 'react-router-dom';
import { useLocation } from 'react-router-dom';
import Example from "./paw.jpeg";

function Topbar({user}) {
    const location = useLocation();
    const pathname = location.pathname;

    if (pathname === '/') {
        return (
            <div className=''>
                
            </div>
        )
    }
    if (pathname === "/login" || pathname === "/register") {
        return (
            <div className='topbar'>
                <Link to="/" className='top_left'>Bark Avenue<img style={{height:"6vh"}} src={Example} /></Link>
                <Link className='register' to={pathname === "/login"? "/register": "/login"}>{pathname === "/login"? "Register": "Login"}</Link>
            </div>
        )
    }
    else {
        return (
            <div className='topbar'>
                <Link to="/" className='top_left'>Bark Avenue<img style={{height:"6vh"}} src={Example} /></Link>
                <Link className='register' to={{pathname:'user/update', state:{username:user.username}}}>Update</Link>
                <Link className='login' to={{pathname:'/feed', state:{username:user.username}}}>Feed</Link>
                <Link className='register' to={'/trails/canvas'}>Trails</Link>
                <Link className='register'>{user.username}</Link>
            </div>
        )
    }
  }
  
  export default Topbar;