//Flot Line Chart

var offset = 0;
// plot();
// console.log(services_chart_url);

function load_chart() {
    var pbs_list_arr = $("#pbs-list-item li").map(function() {
        return $(this).text();
    }).get();
    // console.log(pbs_list_arr)
    
    if( pbs_list_arr.length == 0 ) {
        $('#flot-line-chart').html('');
        return;
    }
    
    $.ajax({
        // url: "{% url 'myapp:myapp-api:services-chart' %}",
        url: services_chart_url,
        // url: `{% url 'myapp:myapp-api:atc-code-list' %}`,
        type: 'GET',
        data: {
            'pbscode': JSON.stringify(pbs_list_arr)
        },
        success: function(response) {
            // console.log(response)
            pbs_usage_chart_details = response;
            // console.log(pbs_usage_chart_details)
            load_multi_chart(response);
            // load_line_data(response)
            
            // plot()
        },
        error: function(response) {
            alert('Error Occured while getting data for Services CHart');
        }
    })
}

function plot() {
    var sin = [],
        cos = [],
        tan = [];
    for (var i = 0; i < 12; i += 0.2) {
        sin.push([i, Math.sin(i + offset)]);
        cos.push([i, Math.cos(i + offset)]);
        tan.push([i, Math.tan(i + offset)]);
    }

    var options = {
        series: {
            lines: {
                show: true
            },
            points: {
                show: true
            }
        },
        grid: {
            hoverable: true //IMPORTANT! this is needed for tooltip to work
        },
        yaxis: {
            min: 0,
            max: 10,
        },
        // xaxis: {
        //     min: 0,
        //     max: 100,
        // },
        xLabels: 'day',
        xLabelAngle: 45,
        tooltip: true,
        tooltipOpts: {
            content: "'%s' of %x.1 is %y.4",
            shifts: {
                x: -60,
                y: 25
            }
        },
        resize: true
        
    };

    var plotObj = $.plot($("#flot-line-chart"), [{
            data: sin,
            label: "sin(x)1"
        }, {
            data: cos,
            label: "cos(x)2"
        }, {
            data: tan,
            label: "tan(x)"
        }],
        options);
}

function load_line_data(response) {
    // response = JSON.parse(response);
    $('#flot-line-chart').html('')
    Morris.Line({
        element: 'flot-line-chart',
        // data: [
        //   { period: '2016-05-10', park1: 500, park2: 200, park3: 50, park4: 10, park5: 0 },
        //   { period: '2016-05-11', park1: 15, park2: 275, park3: 5, park4: 60, park5: 0 },
        //   { period: '2016-05-12', park1: 80, park2: 20, park3: 30, park4: 30, park5: 0 },
        //   { period: '2016-05-13', park1: 100, park2: 200, park3: 250, park4: 50, park5: 0 },
        //   { period: '2016-05-14', park1: 50, park2: 60, park3: 20, park4: 10, park5: 0 },
        //   { period: '2016-05-15', park1: 75, park2: 65, park3: 10, park4: 60, park5: 0 },
        //   { period: '2016-05-16', park1: 175, park2:95, park3: 110, park4: 30, park5: 0 },
        //   { period: '2016-05-17', park1: 150, park2:95, park3: 90, park4: 111, park5: 0 },
        //   { period: '2016-05-18', park1: 120, park2:95, park3: 60, park4: 47, park5: 0 },
        //   { period: '2016-05-19', park1: 60, park2:95, park3: 50, park4: 231, park5: 0 },
        //   { period: '2016-05-20', park1: 10, park2:95, park3: 100, park4: 80, park5: 0 }
        // ],
        data: response.length ? response : [ { label:"Total", value:100 } ],
        lineColors: ['#819C79'],
        xkey: 'Date',
        // hoverCallback: function (index, options, content, row) {
        //     return "sin(" + row.x + ") = " + row.y;
        // },
        // yaxis: {
        //     min: 0,
        //     max: 10,
        // },
        // ykeys: ['park1','park2','park3','park4','park5'],
        ykeys: ['total_sum'],
        labels: ['Total'],
        xLabels: 'year',
        xLabelAngle: 45,
        // xLabelFormat: function (d) {
        //   var weekdays = new Array(7);
        //   weekdays[0] = "SUN";
        //   weekdays[1] = "MON";
        //   weekdays[2] = "TUE";
        //   weekdays[3] = "WED";
        //   weekdays[4] = "THU";
        //   weekdays[5] = "FRI";
        //   weekdays[6] = "SAT";
        
        //   return d.getYear() + '-' + d.getMonth() + '-' + d.getDate();
        // },
        resize: true
        });
}

