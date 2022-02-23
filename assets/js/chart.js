$(function () {
    var $lineChart = $("#line-chart");
    $.ajax({
      url: $lineChart.data("url"),
      success: function (data) {

            var ctx = $lineChart[0].getContext("2d");
            var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Produksi Tahun 2020 (Kg)',
                    data: data.default,
                    backgroundColor: [
                        'rgba(75, 192, 192, 0.2)', 
                    ],
                    borderColor: [
                        'rgba(75, 192, 192, 1)', 
                    ],
                    borderWidth:1,

                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });

        }
    })  
})