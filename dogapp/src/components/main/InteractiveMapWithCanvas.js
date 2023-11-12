// MapWithDrawing.js
import React, { useEffect, useRef , useState} from 'react';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import 'leaflet-draw/dist/leaflet.draw.css';
import 'leaflet-draw';

const MapWithDrawing = ({user}) => {
    const [drawnLayers, setDrawnLayers] = useState([]);
    const [coord, setCoord] = useState({lat:0, long:0});
    const [currentCenter, setCurrentCenter] = useState({ lat: 0, lon: 0 });

    useEffect(() => {
    fetch(`https://nominatim.openstreetmap.org/search?q=${user.pincode}&format=json`).then(res=>res.json())
    .then((res)=>{
        setCurrentCenter({
          lat:res[0].lat,
          lon:res[0].lon
        });
        // Initialize the map
        const map = L.map('map').setView([res[0].lat, res[0].lon], 25);

        // Add a tile layer (you can choose a different tile provider)
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors',
        }).addTo(map);

        // Initialize the Leaflet Draw control
        const drawControl = new L.Control.Draw({
            draw: {
            polyline: {
                allowIntersection: false, // if true, overlapping paths are allowed
                shapeOptions: {
                color: 'red', // outline color
                fillOpacity: 1, // fill opacity (0 to 1)
                weight: 10
                },
            },
            polygon: false,
            circle: false,
            circlemarker: false,
            },
            edit: {
            featureGroup: new L.FeatureGroup(),
            edit: {
                selectedPathOptions: {
                color: 'red', // outline color for selected path during editing
                },
            },
            },
        });

        map.addControl(drawControl);

        // Event listener for when a shape is drawn on the map
        map.on('draw:created', (e) => {
            const layer = e.layer;
            map.addLayer(layer);

            // Update the state with the drawn layers
            setDrawnLayers([...drawnLayers, layer]);
        });

        // Event listener for when the map is moved
        map.on('moveend', () => {
          console.log(map.getCenter())
          setCurrentCenter({
            lat:currentCenter.lat+map.getCenter().lat,
            lon:currentCenter.lon+map.getCenter().lng,
          });
        });

        // Cleanup event listeners when the component unmounts
        return () => {
            map.off('draw:created');
        };
    })
    }, []);

    const handleSave = async () => {
        try {
          // Extract coordinates from drawnLayers
          const shapesData = drawnLayers.map((layer) => {
            const latlngs = layer.getLatLngs();
            return {
              type: 'Polygon', // You might need to adjust this based on the drawn shape
              coordinates: latlngs.map((latlng) => [latlng.lng, latlng.lat]),
            };
          });
    
          // Send the shapesData to the backend using fetch
          const response = await fetch('http://localhost:5000/save_shapes', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({"data":shapesData, "center":currentCenter,  "username":user.username}),
          });
    
          /*if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }*/
    
          // Optional: You can clear the drawn layers after successfully saving
        } catch (error) {
          console.error('Error saving shapes:', error);
        }
      };

  return (
    <div>
        <div style={{ height: '10vh', fontWeight: "900", fontSize:35 }} className='trailheader flex_center'>
            Design your own trail.
        </div>
        <div id="map" style={{ height: '70vh' }}>
        </div>
        <div className='save_trail flex_center'>
            <button onClick={handleSave} className='form_button' id='save_trail'>Save Trail</button>
        </div>
    </div>
  );
};

export default MapWithDrawing;