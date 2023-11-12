import React, { useEffect, useRef, useState } from 'react';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import { useParams } from 'react-router-dom';
import "../../App.css";

const ViewMap = () => {
  const mapRef = useRef(null);
  const [trail, setTrail] = useState(null);
  const { username } = useParams(); // Access the dynamic parameter from the path

  useEffect(() => {
    const fetchData = async () => {
      try {
        // Replace 'your-api-endpoint' with the actual API endpoint that returns the trail data
        const response = await fetch(`http://localhost:5000/trails/${username}`);
        const data = await response.json();

        setTrail(data);
      } catch (error) {
        console.error('Error fetching trail data:', error);
      }
    };

    fetchData();
  }, []); // This effect runs once when the component mounts

  useEffect(() => {
    if (mapRef.current && trail) {
      console.log(trail.center)
      const coordinates = trail.trail.coordinates;

      const map = L.map(mapRef.current).setView([trail.center.lat, trail.center.lon], 13);

      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors',
      }).addTo(map);

      console.log(trail.trail.trail)
      if (coordinates && coordinates.length > 0) {
        const polyline = L.polyline(coordinates, { color: 'blue' }).addTo(map);

        map.fitBounds(polyline.getBounds());
      }
    }
  }, [trail]);
  console.log(trail)

  return (
    <div className='flex_center'>
      <div ref={mapRef} style={{ width: '60vw', height: "92vh" }}>
      </div>
      <div className='route flex_center' style={{flexDirection:"column", width: '40vw', height: "92vh" }}>
        <div className='route_header'>
          {trail && trail.id}
        </div>
        <div className='route_data'>
          Route created by
        </div>
        <div className='route_header'>
          {trail && trail.likes}
        </div>
        <div className='route_data'>
          Users that liked the route
        </div>
        <div className='route_header'>
          {trail && trail.onTrail}
        </div>
        <div className='route_data'>
          Users that follow this route
        </div>
        <div className='button'>
          <button className='form_button'>Like</button>
        </div>
      </div>
    </div>);
};

export default ViewMap;