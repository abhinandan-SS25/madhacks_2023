import React, { useState } from 'react';
import "../App.css";
import { useNavigate } from 'react-router-dom';

function Login() {
    const navigate = useNavigate();

    const [info, setInfo] = useState(
      {
        username: "",
        password: ""
      }
    )

    const [error, setError] = useState("")

    const handleChange = (e) => {
      const { name, value } = e.target;
      setInfo((prevFormData) => ({
        ...prevFormData,
        [name]: value,
      }));
    };

    const handleSubmit = (e) => {
      e.preventDefault();
      fetch("http://localhost:5000/login", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(info)
      })
      .then((res)=>res.json())
      .then((res) => {
        console.log(res)
        if (res.status === 200) {
            navigate('/');
        }
        else {
          console.log(res)
          setError(res.error);
        }
      })
      .catch((error) => {
        setError("There was an issue logging in.");
      })
    }

    return (
      <div className='flex_center'>
        <div className='flex_center left_div'>
          LOGIN
        </div>
        <div className='flex_center right_div'>
          <form id="login_form">
            <div className='form_header flex_center'>
              Log in
            </div>
            <div className='error'>{error?error: " "}</div>
            <div className='flex_center form_input_div'>
              <div>
                <label className='form_label'>
                  Doggo Username
                </label>
                <input value={info.username} onChange={handleChange} type='text' name="username" className='flex_center form_input' />
              </div>
              <div>
                <label className='form_label'>
                  Password
                </label>
                <input value={info.password} onChange={handleChange} type='text' name="password" className='flex_center form_input' />
              </div>
            </div>
            <div className='form_footer flex_center'>
              <button onClick={handleSubmit} className='form_button'>Log In</button>
            </div>
          </form>
        </div>
      </div>
    );
  }
  
  export default Login;