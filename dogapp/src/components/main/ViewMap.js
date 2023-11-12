// MapWithPolyline.js
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';

const ViewMap = () => {
  const { username } = useParams(); // Access the dynamic parameter from the path
  const [polyline, setPolyline] = useState(null);

  useEffect(() => {
    // Placeholder URL for fetching polyline data with the dynamic parameter
    const placeholderUrl = `https://localhost:5000/trails/${username}`;

    // Fetch polyline data from the placeholder URL
    const fetchPolylineData = async () => {
      try {
        const response = await fetch(placeholderUrl, {
          method: 'GET'
        });
        const data = await response.json();

        // Assuming your polyline data is in a 'coordinates' property
        const polylineData = {
          coordinates: data.map(comment => [comment.longitude, comment.latitude]),
          info: 'Polyline Information', // Provide a general information for the polyline
        };

        setPolyline(polylineData);
      } catch (error) {
        console.error('Error fetching polyline data:', error);
      }
    };

    fetchPolylineData();
  }, [username]); // Fetch data whenever the username parameter changes

  useEffect(() => {
    if (polyline) {
      // Initialize the map
      const map = L.map('map').setView([polyline.coordinates[0][1], polyline.coordinates[0][0]], 15);

      // Add a tile layer (you can choose a different tile provider)
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors',
      }).addTo(map);

      // Create a Leaflet polyline and add it to the map
      const polylineLayer = L.polyline(polyline.coordinates, { color: 'blue' }).addTo(map);

      // Add a popup with polyline information
      if (polyline.info) {
        polylineLayer.bindPopup(polyline.info).openPopup();
      }

      // Optionally, fit the map to the bounds of the polyline
      map.fitBounds(polylineLayer.getBounds());
    }
  }, [polyline]);

  return <div username="map" style={{ height: '50vh' }} />;
};

export default ViewMap;