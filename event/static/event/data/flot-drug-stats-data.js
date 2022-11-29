//Flot Line Chart

var offset = 0;
// plot();
// console.log(drug_chart_url);

function load_drug_chart(selected_vial_content) {
    pbscode = recently_clicked_pbscode
    // console.log(pbscode)

    if( pbscode.length == 0 ) return;

    $.ajax({
        url: drug_chart_url,
        type: 'GET',
        data: {
            'pbscode': pbscode,
            'vial_content': selected_vial_content
        },
        success: function(response) {
            // console.log(response)
            drug_stats_chart_details = response;
            // console.log(pbs_usage_chart_details)
            load_drug_line_data(response)
            // plot()
        },
        error: function(response) {
            alert('Error Occured while getting data for Drug Cart');
        }
    })
}

function load_drug_line_data(response) {
    response = JSON.parse(JSON.stringify(response));

    $('#flot-line-chart-drug').html('')
    Morris.Line({
        element: 'flot-line-chart-drug',
        data: response['qs'],
        lineColors: ['#819C79', '#86550d'],
        xkey: 'PriceDate',
        ykeys: response['ykeys'],
        labels: response['labels'],
        xLabels: 'year',
        xLabelAngle: 45,
        yLabelFormat: function(y) {
              return "$" + y;
        },
        resize: true
    });
}

