import "../../App.css";
import React, { useEffect, useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';

function Update(props) {
    const navigate = useNavigate();
    const user = props.user;

    console.log(user)
    if (user == null || user.authenticated == false || user.username == "Guest" || user.username == null) {
        navigate("/login");
    }

    const [info, setInfo] = useState(
        {
          username: user.username? user.username: "",
          phoneNum: user.phoneNum? user.phoneNum: "",
          description: user.description? user.description: "",
          streetAddress: user.streetAddress? user.streetAddress: "",
          city: user.city? user.city: "",
          state: user.state? user.state: "",
          country: user.country? user.country: "",
          pincode: user.pincode? user.pincode: "",
          ownerName: user.ownerName? user.ownerName: "",
          ownerDOB: user.ownerDOB? user.ownerDOB: "",
          ownerSex: user.ownerSex? user.ownerSex: "",
          dogName: user.dogName? user.dogName: "",
          dogBreed: user.dogBreed? user.dogBreed: "",
          dogDOB: user.dogDOB? user.dogDOB: "",
          dogSex: user.dogSex? user.dogSex: "",
          dogsFavoriteActivities: user.dogsFavoriteActivities? user.dogsFavoriteActivities: "",
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
    <div>
      <div style={{ height: '10vh', fontWeight: "900", fontSize:35 }} className='trailheader flex_center'>
          Hello, fur-riend, please complete your profile.
      </div>
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
                  <input placeholder="MM-DD-YYYY" value={info.ownerDOB} onChange={handleChange} type='text' name="ownerDOB" className='flex_center form_input' />
                </div>
                <div>
                  <label className='form_label'>
                    Owner Sex
                  </label>
                  <input placeholder="M/F/X" value={info.ownerSex} onChange={handleChange} type='text' name="ownerSex" className='flex_center form_input' />
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
                  <input placeholder="MM-DD-YYYY" value={info.dogDOB} onChange={handleChange} type='text' name="dogDOB" className='flex_center form_input' />
                </div>
                <div>
                  <label className='form_label'>
                    Doggo sex
                  </label>
                  <input placeholder="M/F/X" value={info.dogSex} onChange={handleChange} type='text' name="dogSex" className='flex_center form_input' />
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
            <form>
              <div className='form_header flex_center'>
                You
              </div>
              <div className='error'>{error?' ': " "}</div>
              <div className='flex_center form_input_div'>
                <div>
                  <label className='form_label'>
                    Username
                  </label>
                  <input value={info.username} onChange={handleChange} type='text' name="username" className='flex_center form_input' disabled/>
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
    </div>
      );
}

export default Update;