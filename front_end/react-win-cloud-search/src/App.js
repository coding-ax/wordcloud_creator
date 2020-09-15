import React from 'react';
import { HashRouter as Router } from 'react-router-dom'
import { renderRoutes } from 'react-router-config'
import config from './routes/index'
// 由于 antd 组件的默认文案是英文，所以需要修改为中文
import zhCN from 'antd/es/locale/zh_CN';
import moment from 'moment';
import 'moment/locale/zh-cn';
import 'antd/dist/antd.css';
import './index.css';
import { ConfigProvider } from 'antd';
moment.locale('zh-cn');
function App() {
  return (
    <div className="App">
      <Router>
        <ConfigProvider locale={zhCN}>
          {renderRoutes(config)}
        </ConfigProvider>
      </Router>
    </div>
  );
}

export default App;
