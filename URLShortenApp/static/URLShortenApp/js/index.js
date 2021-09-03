VANTA.WAVES({
    el: "#vanta-waves",
    mouseControls: true,
    touchControls: true,
    gyroControls: false,
    minHeight: 200.00,
    minWidth: 200.00,
    scale: 1.00,
    scaleMobile: 1.00,
    color: 0x2a2943,
    shininess: 42.00,
    waveHeight: 16.50,
    zoom: 1.23
})

$( document ).ready(function(){
    $('#hdtimeout').fadeIn('slow', function(){
       $('#hdtimeout').delay(3000).fadeOut(); 
    });
});