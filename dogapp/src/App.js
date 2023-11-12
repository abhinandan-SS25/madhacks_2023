import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './components/home';
import Login from './components/login';
import Registration from './components/registration';
import Topbar from "./components/Topbar/Topbar";
import Feed from "./components/main/feed";
import DrawableCanvas from "./components/main/trails";
import InteractiveMapWithCanvas from "./components/main/InteractiveMapWithCanvas";
import ViewMap from "./components/main/ViewMap";
import Update from "./components/user/update";
import React, { useState } from 'react';

function App() {
  const [user, setUser] = useState({username:"Guest", isAuthenticated:false});

  return (
    <div>
      <Topbar user={user} />
      <Routes>
        <Route path="/" exact element={<Home/>} />
        <Route path="/login" exact element={<Login setUser={setUser}/>} />
        <Route path="/register" exact element={<Registration setUser={setUser}/>} />
        <Route path="/feed" exact element={<Feed user={user} setUser={setUser}/>} />
        <Route path="/user/update" element={<Update user={user}/>} />
        <Route path="/trails" element={<DrawableCanvas user={user}/>} />
        <Route path="/trails/canvas" element={<InteractiveMapWithCanvas user={user}/>} />
        <Route path="/trails/view/:username" element={<ViewMap user={user}/>} />
      </Routes>
    </div>
  );
}

export default App;
