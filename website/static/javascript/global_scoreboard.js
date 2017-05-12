// Load scoreboard every 5 seconds

function loadScoreboard() {
    console.log('load')
    $('#scoreboard').load('/global_scoreboard/get/');
    setTimeout(loadScoreboard, 5000);
}

$(document).ready(function() {
    $('#scoreboard').load('/global_scoreboard/get/');

    setTimeout(loadScoreboard, 5000);

    function scrollpage() {
        function f()
        {
            window.scrollTo(0,i);
            if(status==0) {
                i=i+4;
                if(i>=Height){	status=1; }
            } else {
                i=i-4;
                if(i<=1){	status=0; }  // if you don't want continue scroll then remove this line
            }
        setTimeout( f, 100 );
        }
        f();
    }
    var Height=document.documentElement.scrollHeight;
    var i=1,j=Height,status=0;
    scrollpage();
});