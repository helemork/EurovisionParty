// Load scoreboard every 5 seconds

function loadScoreboard() {
    console.log('load')
    $('#scoreboard').load('/scoreboard/get/');
    Height = $("#scrollwrapper").height(); // Update height
    setTimeout(loadScoreboard, 5000);
}

var Height, i, status;
var viewportHeight;

function updateViewportHeight() {
     if (self.innerHeight)
        viewportHeight = window.innerHeight
    else if (document.documentElement && document.documentElement.clientHeight)
        viewportHeight= document.documentElement.clientHeight;
    else if (document.body)
        viewportHeight= document.body.clientHeight;
    console.log('vp height', viewportHeight);
}

$(document).ready(function() {
    $('#scoreboard').load('/scoreboard/get/', function() {

        setTimeout(loadScoreboard, 5000);

        Height = $("#scrollwrapper").height();
        updateViewportHeight();

        $('#activate_scroll_button').click(function () {
            function scrollpage() {
                function f() {
                    window.scrollTo(0, i);
                    updateViewportHeight();
                    if (status == 0) {
                        i = i + 4;
                        if (i >= Height - viewportHeight) {
                            status = 1;
                        }
                    } else {
                        i = i - 4;
                        if (i <= 1) {
                            status = 0;
                        }  // if you don't want continue scroll then remove this line
                    }
                    setTimeout(f, 100);
                }

                f();
            }

            i = 1;
            status = 0;
            scrollpage();
        });
    });});
