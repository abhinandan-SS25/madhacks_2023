import L from 'leaflet';

L.DrawingCanvasOverlay = L.Layer.extend({
  onAdd: function (map) {
    this._canvas = L.DomUtil.create('canvas', 'leaflet-drawing-canvas');
    map.getPanes().overlayPane.appendChild(this._canvas);
    this._ctx = this._canvas.getContext('2d');
  },

  onRemove: function (map) {
    map.getPanes().overlayPane.removeChild(this._canvas);
  },
});

L.drawingCanvasOverlay = function () {
  return new L.DrawingCanvasOverlay;
};