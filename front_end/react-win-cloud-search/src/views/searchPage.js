import React from 'react'
import styled from 'styled-components'
import { Input, Button, notification } from 'antd';
const { Search } = Input;
const SearchCSSDiv = styled.div`
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
    .search-box{
        width:700px;
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
        // onClose: close,
    });
};
function SearchPage(props) {
    console.log(props)
    return (
        <SearchCSSDiv>
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

        </SearchCSSDiv>
    )
}
export default React.memo(SearchPage)
