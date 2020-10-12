import React, { useEffect, useState } from 'react'
import { Image, Spin, Alert, Button } from 'antd';
import styled from 'styled-components'
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
function ResPage(props) {
    const { keyword, dqs, salary } = JSON.parse(props.match.params.value)
    console.log(props)
    const [pic, setPic] = useState("")
    const [isLoad, setIsLoad] = useState(false)
    useEffect(() => {
        // eslint-disable-next-line
        fetch(`http://47.102.212.191:10010/getPic?keyword=${keyword}&dqs=${dqs}&salary=${salary}`).then(res => res.json()).then(res => {
            console.log(res)
            setPic(res.url)
            setIsLoad(true)
        })
    }, [])
    return (<div>
        <Swiper>
            <Button type="primary" className="left-top" onClick={() => { props.history.push('/') }}>返回上层</Button>
            {!isLoad && <Spin tip="Loading...">
                <Alert
                    message="正在请求中"
                    description="正在为您生成专业技能词云图"
                    type="info"
                />
            </Spin>}
            {isLoad && <Image
                width={500}
                src={`http://47.102.212.191:10010/${pic}`}
            />}
        </Swiper>
    </div >)
}
export default React.memo(ResPage)