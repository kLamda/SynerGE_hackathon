'use strict';
$(document).ready(function() {
    $(".predictor").hide();
    var eh_month = {{eh_month}};
    console.log(abc);
    $(function() {
            var chart = new ApexCharts(
                document.querySelector("#equipment-history"),
                chart1_equipment
            );
            chart.render();
        });
    $(function() {
            var options = {
                chart: {
                    height: 340,
                    type: 'bar',
                },
                plotOptions: {
                    bar: {
                        horizontal: false,
                        columnWidth: '55%',
                        endingShape: 'rounded'
                    },
                },
                dataLabels: {
                    enabled: false
                },
                colors: ["#0e9e4a", "#4099ff", "#FF5370"],
                stroke: {
                    show: true,
                    width: 2,
                    colors: ['transparent']
                },
                fill: {
                    type: 'gradient',
                    gradient: {
                        shade: 'light',
                        type: "vertical",
                        shadeIntensity: 0.25,
                        inverseColors: true,
                        opacityFrom: 1,
                        opacityTo: 0.7,
                        stops: [50, 100]
                    },
                },
                series: [{
                    name: 'Net Profit',
                    data: [44, 55, 57, 56, 61, 58, 63]
                }, {
                    name: 'Revenue',
                    data: [76, 85, 101, 98, 87, 105, 91]
                }, {
                    name: 'Free Cash Flow',
                    data: [35, 41, 36, 26, 45, 48, 52]
                }],
                xaxis: {
                    categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'],
                },
                yaxis: {
                    title: {
                        text: '$ (thousands)'
                    }
                },
                tooltip: {
                    y: {
                        formatter: function(val) {
                            return "$ " + val + " thousands"
                        }
                    }
                }
            }
            var chart = new ApexCharts(
                document.querySelector("#bar-chart-1"),
                options
            );
            chart.render();
        });
        $(function() {
            var options = {
                chart: {
                    height: 250,
                    type: 'bar',
                },
                plotOptions: {
                    bar: {
                        horizontal: true,
                        dataLabels: {
                            position: 'top',
                        },
                    }
                },
                colors: ["#4099ff", "#0e9e4a"],
                dataLabels: {
                    enabled: true,
                    offsetX: -6,
                    style: {
                        fontSize: '12px',
                        colors: ['#fff']
                    }
                },
                stroke: {
                    show: true,
                    width: 1,
                    colors: ['#fff']
                },
                fill: {
                    type: 'gradient',
                    gradient: {
                        shade: 'light',
                        type: "horizontal",
                        shadeIntensity: 0.25,
                        inverseColors: true,
                        opacityFrom: 0.8,
                        opacityTo: 1,
                        stops: [0, 100]
                    },
                },
                series: [{
                    data: [44, 55, 41, 64]
                }, {
                    data: [53, 32, 33, 52]
                }],
                xaxis: {
                    categories: ["Equipment1", "Equipment2", "Equipment3", "Equipment4"],
                },
            }
            var chart = new ApexCharts(
                document.querySelector("#bar-chart-3"),
                options
            );
            chart.render();
        });
        $(function() {
            var options = {
                chart: {
                    height: 250,
                    type: 'bar',
                },
                plotOptions: {
                    bar: {
                        horizontal: true,
                        dataLabels: {
                            position: 'top',
                        },
                    }
                },
                colors: ["#4099ff", "#0e9e4a"],
                dataLabels: {
                    enabled: true,
                    offsetX: -6,
                    style: {
                        fontSize: '12px',
                        colors: ['#fff']
                    }
                },
                stroke: {
                    show: true,
                    width: 1,
                    colors: ['#fff']
                },
                fill: {
                    type: 'gradient',
                    gradient: {
                        shade: 'light',
                        type: "horizontal",
                        shadeIntensity: 0.25,
                        inverseColors: true,
                        opacityFrom: 0.8,
                        opacityTo: 1,
                        stops: [0, 100]
                    },
                },
                series: [{
                    data: [44, 55, 41, 64]
                }, {
                    data: [53, 32, 33, 52]
                }],
                xaxis: {
                    categories: ["Equipment1", "Equipment2", "Equipment3", "Equipment4"],
                },
            }
            var chart = new ApexCharts(
                document.querySelector("#bar-chart-comp-equipment"),
                options
            );
            chart.render();
        });
        $(function() {
            var options = {
                chart: {
                    height: 300,
                    type: 'radialBar',
                },
                plotOptions: {
                    radialBar: {
                        offsetY: -30,
                        startAngle: 0,
                        endAngle: 270,
                        hollow: {
                            margin: 5,
                            size: '30%',
                            background: 'transparent',
                            image: undefined,
                        },
                        dataLabels: {
                            name: {
                                show: false,

                            },
                            value: {
                                show: false,
                            }
                        }
                    }
                },
                colors: ["#4099ff", "#0e9e4a", "#FFB64D", "#FF5370"],
                fill: {
                    type: 'gradient',
                    gradient: {
                        shade: 'light',
                        type: 'vertical',
                        shadeIntensity: 0.25,
                        inverseColors: true,
                        opacityFrom: 1,
                        opacityTo: 0.7,
                        stops: [40, 100]
                    }
                },
                series: [76, 67, 61, 90],
                labels: ['Vimeo', 'Messenger', 'Facebook', 'LinkedIn'],
                legend: {
                    show: true,
                    floating: true,
                    fontSize: '16px',
                    position: 'left',
                    offsetX: 0,
                    offsetY: 0,
                    labels: {
                        useSeriesColors: true,
                    },
                    markers: {
                        size: 0
                    },
                    formatter: function(seriesName, opts) {
                        return seriesName + ":  " + opts.w.globals.series[opts.seriesIndex]
                    },
                    itemMargin: {
                        horizontal: 1,
                    }
                },
                responsive: [{
                    breakpoint: 480,
                    options: {
                        legend: {
                            show: false
                        }
                    }
                }]
            }
            var chart = new ApexCharts(
                document.querySelector("#radialBar-tom-state"),
                options
            );
            chart.render();
        });
        $(function() {
            var options = {
                chart: {
                    height: 270,
                    type: 'pie',
                },
                labels: ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
                series: [44, 55, 13, 43, 22],
                colors: ["#4099ff", "#0e9e4a", "#00bcd4", "#FFB64D", "#FF5370"],
                legend: {
                    show: true,
                    position: 'bottom',
                },
                fill: {
                    type: 'gradient',
                    gradient: {
                        shade: 'light',
                        inverseColors: true,
                    }
                },
                dataLabels: {
                    enabled: true,
                    dropShadow: {
                        enabled: false,
                    }
                },
                responsive: [{
                    breakpoint: 480,
                    options: {
                        legend: {
                            position: 'bottom'
                        }
                    }
                }]
            }
            var chart = new ApexCharts(
                document.querySelector("#pie-chart-tom-equip"),
                options
            );
            chart.render();
        });
});
var chart1_equipment = {
                chart: {
                    height: 300,
                    type: 'line',
                    zoom: {
                        enabled: false
                    },
                },
                dataLabels: {
                    enabled: false
                },
                stroke: {
                    width: [5, 7, 5],
                    curve: 'straight',
                    dashArray: [0, 8, 5]
                },
                colors: ["#0e9e4a", "#FFB64D", "#FF5370"],
                fill: {
                    type: "gradient",
                    gradient: {
                        shade: 'light'
                    },
                },
                series: [{
                        name: "Session Duration",
                        data: [45, 52, 38, 24, 33, 26, 21, 20, 6, 8, 15, 10]
                    },
                    {
                        name: "Page Views",
                        data: [35, 41, 62, 42, 13, 18, 29, 37, 36, 51, 32, 35]
                    },
                    {
                        name: 'Total Visits',
                        data: [87, 57, 74, 99, 75, 38, 62, 47, 82, 56, 45, 47]
                    }
                ],
                title: {
                    text: 'Page Statistics',
                    align: 'left'
                },
                markers: {
                    size: 0,

                    hover: {
                        sizeOffset: 6
                    }
                },
                xaxis: {
                    categories: ['01 Jan', '02 Jan', '03 Jan', '04 Jan', '05 Jan', '06 Jan', '07 Jan', '08 Jan', '09 Jan',
                        '10 Jan', '11 Jan', '12 Jan'
                    ],
                },
                tooltip: {
                    y: [{
                        title: {
                            formatter: function(val) {
                                return val + " (mins)"
                            }
                        }
                    }, {
                        title: {
                            formatter: function(val) {
                                return val + " per session"
                            }
                        }
                    }, {
                        title: {
                            formatter: function(val) {
                                return val;
                            }
                        }
                    }]
                },
                grid: {
                    borderColor: '#f1f1f1',
                }
            }

function state(val){
            var values = [];
            $(".dash-main").hide();
            $(".predictor").show();
            console.log(values);
            $.ajax({
              url : "/", // the endpoint,commonly same url
              type : "POST", // http method
              data : { option: val},

                  // handle a successful response
              success : function(json) {
              console.log(json.values)
              }
            });
        }
function equip(){
    $(".dash-main").hide();
    $(".predictor").show();
}