import React, { useEffect, useState } from 'react';
import "../../App.css";
import { useLocation, useNavigate } from 'react-router-dom';
import DrawableCanvas from "./trails";
import { Link } from 'react-router-dom';

function Feed({user, setUser}) {
    const location = useLocation();
    const history = useNavigate();

    const [feedData, setFeedData] = useState([]);
    const [feedTrails, setFeedTrails] = useState([]);

    useEffect(()=> {
        if (location.state === null && (user == null || user.username == "Guest")) {
            history("/login");
        }
        try {
            const url = location.state != null? `http://localhost:5000/feed/${location.state.username}`: `http://localhost:5000/feed/${user.username}`;
            fetch(url, {
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
                        setFeedData(res.data);
                        setFeedTrails(res.trails);
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

    const data = feedData.map((e)=>(
        <div className="feed_data flex_center">
            <div className="data_pic">
                <img id='data_img' src={e.profilePicture} />
            </div>
            <div className="data_dets">
                <div className="data_name">
                    {e.ownerName}
                </div>
                <div className="data_desc">
                    {e["dogsFavoriteActivities"]}
                </div>
            </div>
            <div className="data_contact">
                <div className="contact_number">
                    Phone Number
                </div>
                <div className="data_name">
                    {e.phoneNum}
                </div>
            </div>
        </div>
    ));

    const trails = feedTrails.map((e)=>(
        <div className="feed_data flex_center">
            <div className="data_pic">
                Liked:{e.likes}
            </div>
            <div className="data_dets">
                <div className="data_name">
                    On trails:{e.onTrail}
                </div>
                <div className="data_desc">
                    {e.id}'s trail
                </div>
            </div>
            <div className="data_contact">
                <Link to={`/trails/view/${e.id}`}>
                    View
                </Link>
            </div>
        </div>
    ));

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
                        <div style={{justifyContent:"flex-start", height:"100vh"}} className='feed_left_div'>
                            <div className='feed_header'>
                                Discover paws-ible friends
                            </div>
                            <div className='feed_data_list'>
                                {[data]}
                            </div>
                        </div>
                        <div style={{justifyContent:"flex-start", height:"100vh"}} className='flex_center right_div'>
                            <div className='feed_header'>
                                Popular trails near you
                            </div>
                            <div className='feed_data_list'>
                                {[trails]}
                            </div>
                        </div>
                    </div>
                    
                </div>
            </div>
    );
  }
  
  export default Feed;