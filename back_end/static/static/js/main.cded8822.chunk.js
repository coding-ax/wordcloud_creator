(this["webpackJsonpreact-win-cloud-search"]=this["webpackJsonpreact-win-cloud-search"]||[]).push([[0],{127:function(e,n,t){e.exports=t(199)},199:function(e,n,t){"use strict";t.r(n);var a=t(0),c=t.n(a),o=t(9),r=t.n(o),i=(t(92),t(119)),l=t(122),u=t(60),s=t(65),p=t(202),m=t(88),h=t(126);function d(){var e=Object(u.a)(["\n    background:url('https://xgpax.top/wp-content/uploads/2020/08/\u5929\u6c14\u4e4b\u5b50.jpg') 100%;   \n    margin:auto;\n    padding:auto;\n    width:100vw;\n    height:100vh;\n    text-align:center;\n    display:flex;\n    flex-direction:column;\n    justify-content:center;\n    align-items:center;\n    .search-box{\n        width:700px;\n    }\n"]);return d=function(){return e},e}var f=p.a.Search,g=s.a.div(d());var v=c.a.memo((function(e){return console.log(e),c.a.createElement(g,null,c.a.createElement("div",{className:"search-box"},c.a.createElement(f,{placeholder:"\u8bf7\u8f93\u5165\u8981\u67e5\u627e\u7684\u5c97\u4f4d",onSearch:function(n){""!==n?e.history.push("/res/".concat(n)):function(){var e="open".concat(Date.now()),n=c.a.createElement(m.a,{type:"primary",size:"small",onClick:function(){return h.a.close(e)}},"\u786e\u8ba4");h.a.open({message:"\u63d0\u793a",description:"\u8bf7\u8f93\u5165\u8981\u641c\u7d22\u7684\u5185\u5bb9",btn:n,key:e})}()},enterButton:!0})))})),w=t(78),x=t(200),b=t(203),E=t(201);function j(){var e=Object(u.a)(["\n    background:url('https://xgpax.top/wp-content/uploads/2020/08/\u5929\u6c14\u4e4b\u5b50.jpg') 100%;\n    margin:auto;\n    padding:auto;\n    width:100vw;\n    height:100vh;\n    text-align:center;\n    display:flex;\n    flex-direction:column;\n    justify-content:center;\n    align-items:center;\n    .left-top{\n        position: fixed;\n        left:30px;\n        top:50px;\n    }\n"]);return j=function(){return e},e}var y=s.a.div(j());var k=[{path:"/",exact:!0,component:v},{path:"/res/:value",exact:!0,component:c.a.memo((function(e){var n=Object(a.useState)(e.match.params.value),t=Object(w.a)(n,2),o=t[0],r=(t[1],Object(a.useState)("")),i=Object(w.a)(r,2),l=i[0],u=i[1],s=Object(a.useState)(!1),p=Object(w.a)(s,2),h=p[0],d=p[1];return Object(a.useEffect)((function(){fetch("http://47.102.212.191:10010/getPic?keyword=".concat(o)).then((function(e){return e.json()})).then((function(e){console.log(e.url),u(e.url),d(!0)}))}),[]),c.a.createElement("div",null,c.a.createElement(y,null,c.a.createElement(m.a,{type:"primary",className:"left-top",onClick:function(){e.history.push("/")}},"\u8fd4\u56de\u4e0a\u5c42"),!h&&c.a.createElement(x.a,{tip:"Loading..."},c.a.createElement(b.a,{message:"\u6b63\u5728\u8bf7\u6c42\u4e2d",description:"\u6b63\u5728\u4e3a\u60a8\u751f\u6210\u4e13\u4e1a\u6280\u80fd\u8bcd\u4e91\u56fe",type:"info"})),h&&c.a.createElement(E.a,{width:500,src:"http://47.102.212.191:10010/".concat(l)})))}))}],O=t(123),S=t(82),B=t.n(S),N=(t(193),t(194),t(21));B.a.locale("zh-cn");var z=function(){return c.a.createElement("div",{className:"App"},c.a.createElement(i.a,null,c.a.createElement(N.a,{locale:O.a},Object(l.a)(k))))};Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));r.a.render(c.a.createElement(z,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()})).catch((function(e){console.error(e.message)}))},92:function(e,n,t){}},[[127,1,2]]]);
//# sourceMappingURL=main.cded8822.chunk.js.map