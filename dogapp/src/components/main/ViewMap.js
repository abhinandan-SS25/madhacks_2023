import React, { useEffect, useRef, useState } from 'react';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import { useParams } from 'react-router-dom';

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
      console.log(trail.trail.trail.coordinates[0][0])
      const coordinates = trail.trail.trail.coordinates;

      const map = L.map(mapRef.current).setView([coordinates[0][0], coordinates[0][1]], 13);

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

  /*useEffect(() => {
    if (trail) {
      console.log(trail.trail.trail.coordinates[0][0], trail.trail.trail.coordinates[0][1])
      // Initialize the map
      const map = L.map(mapRef.current).setView([trail.trail.trail.coordinates[0][0], trail.trail.trail.coordinates[0][1]], 15);

      // Add a tile layer (you can choose a different tile provider)
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors',
      }).addTo(map);

      // Create a Leaflet polygon and add it to the map
      const polygon = L.polygon(trail.coordinates, { color: 'blue' }).addTo(map);

      // Add a popup with trail information
      if (trail.info) {
        polygon.bindPopup(trail.info).openPopup();
      }

      // Optionally, fit the map to the bounds of the polygon
      map.fitBounds(polygon.getBounds());
    }
  }, [trail]);*/

  return <div ref={mapRef} style={{ height: '400px' }} />;
};

export default ViewMap;