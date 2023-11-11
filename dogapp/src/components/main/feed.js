import React, { useEffect, useState } from 'react';
import "../../App.css";
import { useLocation, useNavigate } from 'react-router-dom';

function Feed() {

    const location = useLocation();
    const history = useNavigate();

    const [feedData, setFeedData] = useState([]);

    useEffect(()=> {
        if (location.state === null) {
            history("/login");
        }
        try {
            fetch(`http://localhost:5000/feed/${location.state.username}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    }
                }
            )
            .then((res) => res.json())
            .then((res) => {
                    if (res.status === 300) {
                        setFeedData([
                            <div className='complete_profile'>
                                Please complete your profile to see other people in your area!
                                <div className='compete_profile_button'>
                                    <button id='complete_profile'>
                                        Complete Profile
                                    </button>
                                </div>
                            </div>
                        ]);
                    }
                    else if(res.status === 200) {
                        setFeedData([...res.data]);
                        console.log(feedData);
                    }
                    else {
                        setFeedData([
                            <div className='complete_profile'>
                                There was an error loading your data. {res.error}
                            </div>
                        ]);
                    }
                }
            )
            .catch(
                setFeedData([
                    <div className='complete_profile'>
                        There was an error loading your data.
                    </div>
                ])
            )
        }
        catch {
            setFeedData([
                <div className='complete_profile'>
                    There was an error loading your data.
                </div>
            ])
        }
        
    }, [])

    return (
        location.state === null || location.state.username === null?
            <div>
                <div>
                    <div className='flex_center'>
                        <div className='flex_center left_div'>
                            <div className='feed_header'>
                                Login
                            </div>
                        </div>
                        <div className='flex_center right_div'>

                        </div>
                    </div>
                    
                </div>
            </div>
            :
            <div>
                <div>
                    <div className='flex_center'>
                        <div className='flex_center left_div'>
                            <div className='feed_header'>
                                Discover paws-ible friends
                            </div>
                            <div className='feed_data_list'>
                                {feedData.map((e)=>{
                                    <div className="feed_data">
                                        <div className="data_pic">
                                            <img src={e.profilePicture} />
                                        </div>
                                        <div className="data_dets">
                                            <div className="data_name">
                                                {e.ownerName}
                                            </div>
                                            <div className="data_desc">
                                                {e.dogsFavoriteActivities}
                                            </div>
                                        </div>
                                        <div className="data_contact">
                                            <div className="contact_number">
                                                {e.phoneNum}
                                            </div>
                                        </div>
                                    </div>
                            })}
                            </div>
                        </div>
                        <div className='flex_center right_div'>

                        </div>
                    </div>
                    
                </div>
            </div>
    );
  }
  
  export default Feed;