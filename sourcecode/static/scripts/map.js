/* Map implementation adapted from Leaflet quick start guide at https://leafletjs.com/examples/quick-start/ */

/* Sets max bounds for viewing window */

var maxBounds = L.latLngBounds(
    L.latLng(-55.499550, -150.276413),
    L.latLng(83.162102, -52.233040)
);

/* Initializes map*/

var map = L.map( 'map', {
  center: [42.373455, -71.119090],
  minZoom: 12,
  maxZoom: 18,
  zoom: 3,
  zoomControl: false,
  'maxBounds': maxBounds
}).fitBounds(maxBounds);

/* Use of base layer from basemaps.cartocdn.com */

/* Superimposes base layer onto map */

L.tileLayer( 'https://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}.png', {
 subdomains: ['a','b','c']
}).addTo( map );

/* Sets center view of map */

map.setView(new L.LatLng(42.37727747944798, -71.12431846261856), 13);

/* Icon implementation adapted from Leaflet tutortial at https://leafletjs.com/examples/custom-icons/ */

/* Creates Leaflet Icon class */

var LeafIcon = L.Icon.extend({
    options: {
        iconSize:     [40, 46.15],
        popupAnchor:  [0, -25]
    }
});

/* Initializes Leaflet icon */

var eliot = new LeafIcon({iconUrl: '/static/assets/houses/eliot.png'}),
    kirkland = new LeafIcon({iconUrl: '/static/assets/houses/kirkland.png'}),
    winthrop = new LeafIcon({iconUrl: '/static/assets/houses/winthrop.png'});
    dunster = new LeafIcon({iconUrl: '/static/assets/houses/dunster.png'});
    mather = new LeafIcon({iconUrl: '/static/assets/houses/mather.png'});
    leverett = new LeafIcon({iconUrl: '/static/assets/houses/leverett.png'});
    quincy = new LeafIcon({iconUrl: '/static/assets/houses/quincy.png'});
    adams = new LeafIcon({iconUrl: '/static/assets/houses/adams.png'});
    lowell = new LeafIcon({iconUrl: '/static/assets/houses/lowell.png'});
    pfohozeimer = new LeafIcon({iconUrl: '/static/assets/houses/pfohozeimer.png'});
    currier = new LeafIcon({iconUrl: '/static/assets/houses/currier.png'});
    cabot = new LeafIcon({iconUrl: '/static/assets/houses/cabot.png'});

/* Adds icons to map */

L.marker([42.3702748, -71.1209696], {icon: eliot}).addTo(map).bindPopup("Eliot House");
L.marker([42.3709439, -71.1203644], {icon: kirkland}).addTo(map).bindPopup("Kirkland House");
L.marker([42.3703060, -71.1185175], {icon: winthrop}).addTo(map).bindPopup("Winthrop House");
L.marker([42.3686283, -71.1162346], {icon: dunster}).addTo(map).bindPopup("Dunster House");
L.marker([42.3684133, -71.1155596], {icon: mather}).addTo(map).bindPopup("Mather House");
L.marker([42.3696177, -71.1166243], {icon: leverett}).addTo(map).bindPopup("Leverett House");
L.marker([42.3706419, -71.1169438], {icon: quincy}).addTo(map).bindPopup("Quincy House");
L.marker([42.3717153, -71.1166671], {icon: adams}).addTo(map).bindPopup("Adams House");
L.marker([42.370838, -71.1190269], {icon: lowell}).addTo(map).bindPopup("Lowell House");
L.marker([42.382022, -71.1246837], {icon: pfohozeimer}).addTo(map).bindPopup("Pfohozeimer House");
L.marker([42.381636, -71.1259926], {icon: currier}).addTo(map).bindPopup("Cuirrier House");
L.marker([42.3809301, -71.1239417], {icon: cabot}).addTo(map).bindPopup("Cabot House");



