import "../../App.css";
import React, { useEffect, useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';

function Update() {
    const navigate = useNavigate();


    const [info, setInfo] = useState(
        {
          username: "",
          phoneNum: "",
          description: "",
          streetAddress: "",
          city: "",
          state: "",
          country: "",
          pincode: "",
          ownerName: "",
          ownerDOB: "",
          ownerSex: "",
          dogName: "",
          dogBreed: "",
          dogDOB: "",
          dogSex: "",
          dogsFavoriteActivities: "",
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
        fetch("http://localhost:5000/update", {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(info)
        })
        .then((res) => res.json())
        .then((res) => {
          console.log(res)
          if (res.status === 200) {
              navigate('/feed', {state:{username:info.username}});
          }
          else {
            console.log(res.status)
            setError(res.error);
          }
        })
        .catch((error) => {
          setError("There was an issue logging in.");
        })
      }

    return (
        <div className='flex_center'>
          <div style={{justifyContent:"flex-start", height:"100%", width:"40vw"}} className='flex_center left_div'>
          <div className='form_header flex_center'>
                Doggo
              </div>
              <div className='error'>{error?error: " "}</div>
              <div className='flex_center form_input_div'>
                <div>
                  <label className='form_label'>
                    Owner Name
                  </label>
                  <input value={info.ownerName} onChange={handleChange} type='text' name="ownerName" className='flex_center form_input' />
                </div>
                <div>
                  <label className='form_label'>
                    DOB owner
                  </label>
                  <input value={info.ownerDOB} onChange={handleChange} type='text' name="ownerDOB" className='flex_center form_input' />
                </div>
                <div>
                  <label className='form_label'>
                    Owner Sex
                  </label>
                  <input value={info.ownerSex} onChange={handleChange} type='text' name="ownerSex" className='flex_center form_input' />
                </div>
                <div>
                  <label className='form_label'>
                    Doggo Name
                  </label>
                  <input value={info.dogName} onChange={handleChange} type='text' name="dogName" className='flex_center form_input' />
                </div>
                <div>
                  <label className='form_label'>
                    Dog Breed
                  </label>
                  <input value={info.dogBreed} onChange={handleChange} type='text' name="dogBreed" className='flex_center form_input' />
                </div>
                <div>
                  <label className='form_label'>
                    DOB Doggo
                  </label>
                  <input value={info.dogDOB} onChange={handleChange} type='text' name="dogDOB" className='flex_center form_input' />
                </div>
                <div>
                  <label className='form_label'>
                    Doggo sex
                  </label>
                  <input value={info.dogSex} onChange={handleChange} type='text' name="dogSex" className='flex_center form_input' />
                </div>
                <div>
                  <label className='form_label'>
                    Doggo Fav Activity 
                  </label>
                  <input value={info.dogsFavoriteActivities} onChange={handleChange} type='text' name="dogsFavoriteActivities" className='flex_center form_input' />
                </div>
              </div>
          </div>
          <div style={{justifyContent:"flex-start", height:"100%", width:"40vw"}} className='flex_center right_div'>
            <form id="login_form">
              <div className='form_header flex_center'>
                You
              </div>
              <div className='error'>{error?' ': " "}</div>
              <div className='flex_center form_input_div'>
                <div>
                  <label className='form_label'>
                    Username
                  </label>
                  <input value={info.username} onChange={handleChange} type='text' name="username" className='flex_center form_input' />
                </div>
                <div>
                  <label className='form_label'>
                    Phone Number
                  </label>
                  <input value={info.phoneNum} onChange={handleChange} type='text' name="phoneNum" className='flex_center form_input' />
                </div>
                <div>
                  <label className='form_label'>
                    Description
                  </label>
                  <input value={info.description} onChange={handleChange} type='text' name="description" className='flex_center form_input' />
                </div>
                <div>
                  <label className='form_label'>
                    Street Address
                  </label>
                  <input value={info.streetAddress} onChange={handleChange} type='text' name="streetAddress" className='flex_center form_input' />
                </div>
                <div>
                  <label className='form_label'>
                    City
                  </label>
                  <input value={info.city} onChange={handleChange} type='text' name="city" className='flex_center form_input' />
                </div>
                <div>
                  <label className='form_label'>
                    State
                  </label>
                  <input value={info.state} onChange={handleChange} type='text' name="state" className='flex_center form_input' />
                </div>
                <div>
                  <label className='form_label'>
                    Country
                  </label>
                  <input value={info.country} onChange={handleChange} type='text' name="country" className='flex_center form_input' />
                </div>
                <div>
                  <label className='form_label'>
                    Pincode
                  </label>
                  <input value={info.pincode} onChange={handleChange} type='text' name="pincode" className='flex_center form_input' />
                </div>
              </div>
            </form>
          </div>
            <div className='form_footer flex_center'>
                <button onClick={handleSubmit} className='form_button'>Update</button>
            </div>
        </div>
      );
}

export default Update;