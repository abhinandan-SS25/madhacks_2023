import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './components/home';
import Login from './components/login';
import Registration from './components/registration';
import Topbar from "./components/Topbar/Topbar";
import Feed from "./components/main/feed";
import Update from "./components/user/update";

function App() {
  return (
    <div>
      <Topbar />
      <Routes>
        <Route path="/" exact element={<Home/>} />
        <Route path="/login" element={<Login/>} />
        <Route path="/register" element={<Registration/>} />
        <Route path="/feed" element={<Feed/>} />
        <Route path="/user/update" element={<Update />} />
      </Routes>
    </div>
  );
}

export default App;
