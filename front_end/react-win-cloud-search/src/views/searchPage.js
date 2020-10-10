import React, { useEffect, useState } from 'react'
import styled from 'styled-components'
import { Input, Button, notification, Tabs, Cascader } from 'antd';
const { Search } = Input;
const { TabPane } = Tabs;

const SearchCSSDiv = styled.div`
    background:url('https://xgpax.top/wp-content/uploads/2020/10/188ebc2a7772036b536b948a46c55782.jpg') 100%;   
    margin:auto;
    padding:auto;
    width:100vw;
    height:100vh;
    text-align:center;
    display:flex;
    color:#ffffff;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    .search-box{
        width:700px;
        display:flex;
        flex-direction:row;
        text-align:center;
        justify-content:center;
        align-items:center;
    }
    .description{
        margin-top:100px;
        font-size: 18px;
        transition:1s all;
    }
`
const openNotification = () => {
    const key = `open${Date.now()}`;
    const btn = (
        <Button type="primary" size="small" onClick={() => notification.close(key)}>
            确认
        </Button>
    );
    notification.open({
        message: '提示',
        description: "请输入要搜索的内容",
        btn,
        key,
    });
};
const fontColors = ["#e74c3c", "#3498db", "#2ecc71", "#f1c40f", "#9b59b6"]
let i = 0;
function SearchPage(props) {
    const callback = (key) => {
        console.log(key)
    }
    // 展示option
    const options = [
        {
            value: '010',
            label: '北京',
        },
        {
            value: '020',
            label: '上海',
        },
        {
            value: '050020',
            label: '广州',
        },
        {
            value: '050090',
            label: '深圳',
        }
    ];
    function onChange(value) {
        console.log(value);
    }

    const [fontColor, setFontColor] = useState(fontColors[i])
    // 颜色变化效果
    useEffect(() => {
        let count = setInterval(() => {
            setFontColor(fontColors[i++])
            if (i === fontColors.length - 1) {
                i = 0;
            }

        }, 1000);
        return () => {
            clearInterval(count)
        }
    }, [])
    return (
        <SearchCSSDiv>
            <div className="search-container">
                <Tabs defaultActiveKey="1" onChange={callback} style={{ "color": "#fff" }}>
                    <TabPane tab="通过前端生成词云图和分析图" key="1">
                        <div className='search-box'>
                            <Cascader options={options} placeholder="请选择地区" onChange={onChange} style={{ margin: "3px" }} />
                            <Search placeholder="请输入要查找的岗位"
                                onSearch={value => {
                                    if (value !== "") {
                                        props.history.push(`/res/${value}`)
                                    } else {
                                        openNotification()
                                    }

                                }}
                                enterButton />
                        </div>
                    </TabPane>
                    <TabPane tab="通过后端生成词云图（仅词云图）（较慢）" key="2">
                        <div className='search-box'>

                            <Search placeholder="请输入要查找的岗位"
                                onSearch={value => {
                                    if (value !== "") {
                                        props.history.push(`/res/${value}`)
                                    } else {
                                        openNotification()
                                    }

                                }}
                                enterButton />
                        </div>
                    </TabPane>
                </Tabs>
                <div className="description" style={{ color: fontColor }}>
                    本网站基于猎聘进行相关爬取，服务器配置较低，后端生成图片较慢，请尽量使用前端生成图片。
                </div>
            </div>
        </SearchCSSDiv>
    )
}
export default React.memo(SearchPage)
