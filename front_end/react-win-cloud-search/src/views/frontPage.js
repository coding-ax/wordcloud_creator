import React, { useEffect, useState } from 'react'
import { Button, Progress, Spin, Alert } from 'antd';
import styled from 'styled-components'
import Highcharts from 'highcharts/highcharts'
import wordcloud from 'highcharts/modules/wordcloud'
import highcharts_zh from 'highcharts'
// 运行 
require('highcharts/modules/exporting')(Highcharts);
wordcloud(Highcharts)
// 样式设置
const Swiper = styled.div`
    background:url('https://xgpax.top/wp-content/uploads/2020/08/天气之子.jpg') 100%;
    margin:auto;
    padding:auto;
    width:100vw;
    height:100vh;
    text-align:center;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    .left-top{
        position: fixed;
        left:30px;
        top:50px;
    }
    color:#fff; 
    .pic-container{
        display:flex;
        flex-direction:row;
        justify-content:center;
        align-items:center;
        >*{
            margin:5px;
            border-radius:10px;
        }
    }
`
// 词云图设置
const drawWinCloud = (data) => {
    Highcharts.chart('container', {
        //highcharts logo
        credits: { enabled: true },
        //导出
        exporting: { enabled: true },
        //提示关闭
        tooltip: { enabled: false },
        //颜色配置
        colors: [
            '#ffffff', '#00c0d7', '#2594ce', '#de4c85',
            '#ff7f46', '#ffb310', '#e25c52'
        ],
        //图形配置
        chart: {
            spacingBottom: 15,
            spacingTop: 12,
            // spacingLeft: 5,
            // spacingRight: 5,
            backgroundColor: "rgba(0, 0, 0,0.5)",
        },

        series: [{
            type: "wordcloud",// 类型
            data: data,
            rotation: 0,//字体不旋转
            maxFontSize: 30,//最大字体
            minFontSize: 16,//最小字体
            style: {
                fontFamily: "微软雅黑",
                fontWeight: '500'
            }
        }
        ],
        //点击事件方法
        plotOptions: {
            series: {
                cursor: 'pointer',
                events: {
                    click: function (e) {
                        // 单条数据
                        console.log(e.point.options.itemData)
                    }
                }
            }
        },

        //标题配置
        title: {
            text: '词云图 ●',
            // x: 5,
            // y: 15,
            align: 'left',
            style: {
                color: 'white',
                fontSize: '16px',
                fontWeight: 'bold',
                lineHeight: '1.2',
            }
        }

    });
}
// 柱状图设置
const drawPic = (data) => {
    Highcharts.chart('container2', {
        chart: {
            type: 'column'
        },
        title: {
            text: '各词语TF-IDF值'
        },
        subtitle: {
            text: '统计前10位'
        },
        xAxis: {
            type: 'category',
            labels: {
                rotation: -45  // 设置轴标签旋转角度
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'TF-IDF值'
            }
        },
        legend: {
            enabled: false
        },
        tooltip: {
            pointFormat: 'TF-IDF: <b>{point.y:.3f}</b>'
        },
        series: [{
            name: 'TF-IDF值',
            data: data,
            dataLabels: {
                enabled: true,
                rotation: -90,
                color: '#FFFFFF',
                align: 'right',
                format: '{point.y:.3f}', // :.1f 为保留 1 位小数
                y: 1
            }
        }]
    });
}
const drawBing =(bing)=>{
    Highcharts.chart('container3', {
		chart: {
				plotBackgroundColor: null,
				plotBorderWidth: null,
				plotShadow: false,
				type: 'pie'
		},
		title: {
				text: '前十词汇比例'
		},
		tooltip: {
				pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
		},
		plotOptions: {
				pie: {
						allowPointSelect: true,
						cursor: 'pointer',
						dataLabels: {
								enabled: true,
								format: '<b>{point.name}</b>: {point.percentage:.1f} %',
								style: {
										color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
								}
						}
				}
		},
		series: [{
				name: 'Brands',
				colorByPoint: true,
				data:bing
		}]
});
}
function FrontPage(props) {
    const { keyword, dqs, salary } = JSON.parse(props.match.params.value)
    console.log(keyword, dqs, salary);
    // 提取关键词
    const [isLoad, setIsLoad] = useState(false)
    useEffect(() => {
        let data = [];
        fetch(`http://47.102.212.191:10010/getTF?keyword=${keyword}&dqs=${dqs}&salary=${salary}`).then(res => res.json()).then((res) => {
            console.log(res);
            res = Object(res.word)
            for (let key in res) {
                data.push({
                    key,
                    count: res[key]
                })
            }
            data.sort((a, b) => b.count - a.count);
            data = data.slice(0, 50)
            console.log(data);
            data = data.map((item) => {
                let obj = {
                    name: item.key || "错误",
                    itemData: item,
                    weight: Math.floor(Math.random() * 3 + 1)//控制加粗,随机数取1~3
                };
                return obj;
            });
            console.log(data);
            // 清除load
            setIsLoad(true);
            // 挂载词云图
            drawWinCloud(data);
            // 挂载柱状图
            let zhu = data.map(item => {
                console.log(item)
                return [
                    item.name,
                    item.itemData.count
                ]
            })
            zhu.sort((a, b) => a[1] > b[1]);
            console.log(zhu);
            drawPic(zhu.slice(0, 10));
            // 挂载饼状图
            zhu = zhu.slice(0, 10);
            zhu = zhu.map(item=>{
                return {
                    name:item[0],
                    y:item[1]
                }
            })
            drawBing(zhu);
        })
    }, [])
    return (<div>
        <Swiper>
            <Button type="primary" className="left-top" onClick={() => { props.history.push('/') }}>返回上层</Button>
            {!isLoad && <Spin tip="Loading...">
                <Alert
                    size="large"
                    message="正在加载中"
                    description="爬取中，请耐心等待"
                    type="info"
                />
            </Spin>}
            <div className="pic-container">
                {/**词云图 */}
                <div id="container" style={{ width: "500px", height: "400px" }}>

                </div>
                {/**柱状图 */}
                <div id="container2" style={{ width: "500px", height: "400px" }}>

                </div>
                {/**饼状图 */}
                <div id="container3" style={{ width: "500px", height: "400px" }}>4
                
                </div>
            </div>

        </Swiper>
    </div>)
}
export default React.memo(FrontPage)