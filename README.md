# WeChat_AES_Encrypt

微信AES端对端自动加密脚本，实现自动加解密聊天

**原理**

使用AES-256位加密微信聊天消息，通过sha256（或者RSA）生成AES密钥!

先在客户端加密后传送。

多线程操作，自动加解密！


**使用方法**


安装好相应的库

可以自行修改源码设计密钥生成方式（例如利用RSA生成密钥）

扫码登陆，输入需要加密聊天的对象的昵称即可开始自动加密聊天模式。

windows64位操作系统可以直接到releases主页https://github.com/kay-cottage/WeChat_AES_Encode/releases 下载即可使用！



**补充**

由于itchat项目已经停止维护更新，与微信方面有逐渐取消用户程序接入微信的意向，再加之小编非专业IT人员水平有限！

因此，本程序仅简单与大家分享思路，并没有良好的布局！

不喜勿喷,谢谢支持！

