// Load scoreboard every 5 seconds

function loadScoreboard() {
    console.log('load')
    $('#scoreboard').load('/scoreboard/get/');
    setTimeout(loadScoreboard, 5000);
}

$(document).ready(function() {
    $('#scoreboard').load('/scoreboard/get/');

    setTimeout(loadScoreboard, 5000);
});