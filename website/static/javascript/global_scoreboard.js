// Load scoreboard every 5 secs

function loadScoreboard() {
    console.log('load')
    $('#scoreboard').load('/global_scoreboard/get/');
    setTimeout(loadScoreboard, 5000);
}

var Height, i, status;

$(document).ready(function() {
    $('#scoreboard').load('/global_scoreboard/get/');

    setTimeout(loadScoreboard, 5000);
    var body = document.body, html = document.documentElement;

    Height = $(document).height();
    console.log('Scroll height', Height);
    console.log('Scroll height', $(window).height());
    console.log('Scroll height', $(html).height());
    var _docHeight = (document.height !== undefined) ? document.height : document.body.offsetHeight;
    console.log('Scroll height', _docHeight);

    $('#activate_scroll_button').click(function() {
        function scrollpage() {
            function f() {
                window.scrollTo(0, i);
                console.log('Scroll', i);
                if (status == 0) {
                    i = i + 4;
                    if (i >= Height) {
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
});
