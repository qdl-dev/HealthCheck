# <img src="https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=69948112,3892466283&fm=26&gp=0.jpg" alt="hnu" width = "80" height = "77" /> HNU 自动打卡 HealthCheck

#### 更新日志 Log :bulb:

- :100: :新建`auto`分支，增加`GitHub Action`自动部署功能，录制Bilibili教程，请访问：——`2021/10/30`

- :1st_place_medal: 增加了用户信息加密功能，新建`dev`默认分支（该分支包含加密功能，如不在意用户信息，请用master分支部署） ——`2021/10/29`

- :2nd_place_medal: 完善了`master`分支管理，优化了程序环境部署，增加了ascii艺术字。 					——`2021/3/3`

- :3rd_place_medal:新建`version1-outdate`分支，完成核心功能，`version1-outdate`分支现已过时 ——`2021/3/3`



## 简介 :bulb:

> HealthCheck基于**python**搭建，它每天尝试三次打卡，成功后会**邮箱提醒**你打卡成功; 如果3次尝试仍未成功，HealthCheck会邮件提醒您手动打卡，并将**错误日志**发送给开发者（yourself）.
>
> HealthCheck分离代码和配置文件，你可以很方便地通过修改配置文件来达到**切换运行**环境的目的。同时你也可以通过向用户列表文件中添加新的打卡用户信息来进行**批量打卡**。mapper文件夹下的接口与主程序分离，可以随时**测试接口**。
>
> HealthCheck通过ASP定时框架来实现定点打卡，一旦你将HealthCheck部署到服务器，即可解放双手，高效生活。
>
> 现已添加`auto`分支，无需手动部署，使用`GitHub Action`即可完成自动打卡。

- **声明** :triangular_flag_on_post:
> **使用此项目完成打卡的同学有义务保证信息的准确性！如若出现身体异常，请务必配合疫情防控工作，完成异常信息上报！**



## 分支介绍

- :100: `auto`分支：`GitHub Action`自动部署分支+默认分支，Bilibili教程。（自动部署推荐）.
- :1st_place_medal: `dev`分支：包含用户信息`加密功能`的`手动部署`分支，如不在意用户信息，请用master分支部署.
- :2nd_place_medal: `master`分支：手动部署主分支，相较`dev` 手动部署更加简便。（手动部署推荐）.
- :3rd_place_medal:`version1-outdate`：已过时的分支。（不推荐）.

**目录结构 :trident:**

>  目录结构
```zsh
.
├── config						
│   └── appConfig.py            	# 配置文件
├── data
│   ├── .img                    	# 验证码图片缓存
├── main.py                      	# 程序入口
├── mapper                       	# 方法接口
│   ├── commit.py               	# 提交打卡信息表单
│   ├── getImage.py             	# 下载保存验证码图片
│   ├── ksdemo.py               	# 验证码图像识别
│   ├── login.py                	# 登陆
│   └── sendEmail.py            	# 邮件发送
├── README.md                    	# README
└── requirements.txt             	# 安装依赖		
```



## Quick Start For `auto` branch

>  本README文件对应`auto`分支（手动部署请参考相应分支的README），使用此程序需要简单3步：

### 1. 注册帐号 (Please skip it if you have one)

- [Github](https://github.com)

![image-20211030224537969](https://i.loli.net/2021/10/30/BaYtk3RJwVP2DGT.png)

### 2. pull 到自己的仓库



### 3. 开放Github Action权限并填写账户信息



