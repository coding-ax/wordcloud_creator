import React, { useEffect, useState } from 'react'
import { Image, Spin, Alert, Button } from 'antd';
import styled from 'styled-components'
const Highcharts = require('highcharts')
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
`
let data = [];
function FrontPage(props) {
    const { keyword, dqs, salary } = JSON.parse(props.match.params.value)
    // 提取关键词

    const [word, setWord] = useState("")
    const [isLoad, setIsLoad] = useState(false)
    useEffect(() => {
        fetch(`http://127.0.0.1:5000/getDict?keyword=${keyword}&dqs=${dqs}&salary=${salary}`).then(res => res.json()).then((res) => {
            console.log(res.word);
            res = Object(res.word)
            for (let key in res) {
                data.push({
                    key,
                    count: res[key]
                })
            }
            console.log(data.sort((a, b) => b.count - a.count))
        })
        let text = `um erat ac justo sollicitudin, quis lacinia ligula fringilla. Pellentesque hendrerit, nisi vitae posuere condimentum, lectus urna accumsan libero, rutrum commodo mi lacus pretium erat. Phasellus pretium ultrices mi sed semper. Praesent ut tristique magna. Donec nisl tellus, sagittis ut tempus sit amet, consectetur eget erat. Sed ornare gravida lacinia. Curabitur iaculis metus purus, eget pretium est laoreet ut. Quisque tristique augue ac eros malesuada, vitae facilisis mauris sollicitudin. Mauris ac molestie nulla, vitae facilisis quam. Curabitur placerat ornare sem, in mattis purus posuere eget. Praesent non condimentum odio. Nunc aliquet, odio nec auctor congue, sapien justo dictum massa, nec fermentum massa sapien non tellus. Praesent luctus eros et nunc pretium hendrerit. In consequat et eros nec interdum. Ut neque dui, maximus id elit ac, consequat pretium tellus. Nullam vel accumsan lorem.`;
        // 注意：这里的代码只是对上面的句子进行分词并计算权重（重复次数）并构建词云图需要的数据，其中 arr.find 和 
        // 	reduce 函数可能在低版本 IE 中无法使用（属于ES6新增的函数），如果不能正常使用（对应的函数有报错），请自行加相应的 Polyfill
        //  array.find 的 ployfill 参见：https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/find#Polyfill
        // 	array.reduce 的 ployfill ：https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce#Polyfill
        var word = text.split(/[,\. ]+/g)
            .reduce(function (arr, word) {
                var obj = arr.find(function (obj) {
                    return obj.name === word;
                });
                if (obj) {
                    obj.weight += 1;
                } else {
                    obj = {
                        name: word,
                        weight: 1
                    };
                    arr.push(obj);
                }
                return arr;
            }, []);
        Highcharts.chart('container', {
            series: [{
                type: 'wordcloud',
                data: word
            }],
            title: {
                text: '词云图'
            }
        });

    }, [])
    return (<div>
        <Swiper>
            <Button type="primary" className="left-top" onClick={() => { props.history.push('/') }}>返回上层</Button>
            <div id="container">

            </div>
        </Swiper>
    </div >)
}
export default React.memo(FrontPage)