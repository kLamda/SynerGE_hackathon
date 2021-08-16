'use strict';
$(document).ready(function() {
    setTimeout(function() {
        floatchart()
    }, 100);
    // [ campaign-scroll ] start
    var px = new PerfectScrollbar('.customer-scroll', {
        wheelSpeed: .5,
        swipeEasing: 0,
        wheelPropagation: 1,
        minScrollbarLength: 40,
    });
    var px = new PerfectScrollbar('.customer-scroll1', {
        wheelSpeed: .5,
        swipeEasing: 0,
        wheelPropagation: 1,
        minScrollbarLength: 40,
    });
    var px = new PerfectScrollbar('.customer-scroll2', {
        wheelSpeed: .5,
        swipeEasing: 0,
        wheelPropagation: 1,
        minScrollbarLength: 40,
    });
    var px = new PerfectScrollbar('.customer-scroll3', {
        wheelSpeed: .5,
        swipeEasing: 0,
        wheelPropagation: 1,
        minScrollbarLength: 40,
    });
    // [ campaign-scroll ] end
});

function floatchart() {
    // [ seo-card1 ] start
    $(function() {
        var options1 = {
            chart: {
                type: 'area',
                height: 145,
                sparkline: {
                    enabled: true
                }
            },
            dataLabels: {
                enabled: false
            },
            colors: ["#ff5370"],
            fill: {
                type: 'gradient',
                gradient: {
                    shade: 'dark',
                    gradientToColors: ['#ff869a'],
                    shadeIntensity: 1,
                    type: 'horizontal',
                    opacityFrom: 1,
                    opacityTo: 0.8,
                    stops: [0, 100, 100, 100]
                },
            },
            stroke: {
                curve: 'smooth',
                width: 2,
            },
            series: [{
                data: [45, 35, 60, 50, 85, 70]
            }],
            yaxis: {
               min: 5,
               max: 90,
           },
            tooltip: {
                fixed: {
                    enabled: false
                },
                x: {
                    show: false
                },
                y: {
                    title: {
                        formatter: function(seriesName) {
                            return 'Ticket '
                        }
                    }
                },
                marker: {
                    show: false
                }
            }
        }
        new ApexCharts(document.querySelector("#seo-card1"), options1).render();
    });
    // [ seo-card1 ] end
    // [ customer-chart ] start
    $(function() {
        var options = {
            chart: {
                height: 100,
                type: 'donut',
            },
            dataLabels: {
                enabled: false
            },
            plotOptions: {
                pie: {
                    donut: {
                        size: '75%'
                    }
                }
            },
            labels: ['New', 'Return'],
            series: [39, 10],
            legend: {
                show: false
            },
            tooltip: {
                theme: 'datk'
            },
            grid: {
                padding: {
                    top: 20,
                    right: 0,
                    bottom: 0,
                    left: 0
                },
            },
            colors: ["#4680ff", "#2ed8b6"],
            fill: {
                opacity: [1, 1]
            },
            stroke: {
                width: 0,
            }
        }
        var chart = new ApexCharts(document.querySelector("#customer-chart"), options);
        chart.render();

    });
    // [ customer-chart ] end
    // [ unique-visitor-chart ] start

    // [ unique-visitor-chart ] end
}
