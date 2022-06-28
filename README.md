介绍：
准时预定最新可订lab（医工院），后期可能加入预定当前退订的lab功能。

软件架构
软件架构说明：调用selenium库，主要使用find_by_selector函数定位元素，通过时间判断实现准时lab预定

安装教程：
1、安装谷歌浏览器及其对应驱动。（驱动下载地址：https://chromedriver.storage.googleapis.com/index.html）

使用说明：
1、将驱动地址填入代码区
	version1: 手动提取预定时间第一个位置selector，并填写相应预定信息即可运行。（速度最快）
	version2：全自动判断，只需填写预定信息即可运行。
	shell_version：可终端运行 python -u name.py 按照提示输入信息即可运行。
		      1、手动输入第一个预定时间点selector及对应column（可以中途续订）
		      2、自动判断（若当前时间点的前几天未被订，可能从前面时间点开始预定,不可中途续订）
		      3、可登入任意账号，从头预定，中途续订
2、注意事项：1）默认预定时间为3h，version2和shell_version2运行至结束即可，中途停止不可续订。其它version可以中途续订，中途续订colum位置需要与第一个预定时间点对应。
	     2）由于测试次数有限，可能存在未知bug。

参与贡献
Fork 本仓库
新建 Feat_xxx 分支
提交代码
新建 Pull Request
特技
使用 Readme_XXX.md 来支持不同的语言，例如 Readme_en.md, Readme_zh.md
Gitee 官方博客 blog.gitee.com
你可以 https://gitee.com/explore 这个地址来了解 Gitee 上的优秀开源项目
GVP 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
Gitee 官方提供的使用手册 https://gitee.com/help
Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 https://gitee.com/gitee-stars/