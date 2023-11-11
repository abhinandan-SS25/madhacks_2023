import React, { useState } from 'react';
import "../App.css";
import { useNavigate } from 'react-router-dom';

function Registration() {

  const navigate = useNavigate();

    const [info, setInfo] = useState(
      {
        username: "",
        password: "",
        confirm: ""
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
      fetch("http://localhost:5000/register", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(info)
      })
      .then((res) => res.json())
      .then((res) => {
        if (res.status === 200) {
            navigate('/feed', {username:info.username});
        }
        else {
          setError(res.error);
        }
      })
      .catch((error) => {
        setError("There was an issue registering in.");
      })
    }

    return (
      <div className='flex_center'>
        <div className='flex_center left_div'>
          REGISTRATION
        </div>
        <div className='flex_center right_div'>
          <form id="login_form">
            <div className='form_header flex_center'>
              Sign up
            </div>
            <div className='error'>{error?error: " "}</div>
            <div className='flex_center form_input_div'>
              <div>
                <label className='form_label'>
                  Account Username
                </label>
                <input value={info.username} onChange={handleChange} type='text' name="username" className='form_input' />
              </div>
              <div>
                <label className='form_label'>
                  Account Password
                </label>
                <input value={info.password} onChange={handleChange} type='text' name="password" className='form_input' />
              </div>
              <div>
                <label className='form_label'>
                  Confirm Password
                </label>
                <input value={info.confirm} onChange={handleChange} type='text' name="confirm" className='form_input' />
              </div>
            </div>
            <div className='form_footer flex_center'>
              <button onClick={handleSubmit} className='form_button'>Register</button>
            </div>
          </form>
        </div>
      </div>
    );
  }
  
  export default Registration;