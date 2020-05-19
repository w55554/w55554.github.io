---
layout: post
title: "使用 jekyll + Github 创建自己的博客站点"
date: 2020-05-18 16:30:54
categories: jekyll
tags: jekyll github pages
author: 雨田
mathjax: true
---

* content
{:toc}

## 使用 jekyll + Github Pages 创建自己的博客站点
原来一直用的WP，后来没有精力去管理了，干脆就转到github上吧，只需要commit提交就行了，省事简单，主要是我懒（看我的网站图标就知道了，图标是一头驴），所以我这里使用了Github Pages + Jekyll 来搞，主题大家可以官网[http://jekyllthemes.org/](http://jekyllthemes.org/)去选择，不要挑花眼了。我这里选用了的是[HYG](https://github.com/Gaohaoyang/gaohaoyang.github.io)大神的，Fork（不知道什么意思的，自行搜索吧。）一份到自己的仓库中，自行修改吧。


## 安装 rvm

```
gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
curl -sSL https://get.rvm.io | bash -s stable
//如果上面的连接失败，可以尝试:
curl -L https://raw.githubusercontent.com/wayneeseguin/rvm/master/binscripts/rvm-installer | bash -s stable
source /etc/profile.d/rvm.sh
rvm -v 
## 出现了RVM的版本号，代表安装成功了
```











## 安装ruby

```
rvm install ruby
## 因为从国外的网站的下载，可能会很慢
## 你可以通过 export ALL_PROXY 来使用代理
## 漫长的等待过后提示安装成功的话
rvm list
## 显示已经安装的ruby版本
rvm use 2.7.0 --default
## 这里我使用最新的2.7.0 并设置为默认
```
## 变更 `gem`镜像源
因为 `gem` 原有的很慢（你懂的），所以这里改成国内的源
```
gem sources --add https://gems.ruby-china.com/ --remove https://rubygems.org
gem sources --add https://mirrors.aliyun.com/rubygems/ --remove https://rubygems.org
gem sources -l //查看在用的 gem 源
```

## 安装 `jekyll`

```
gem install jekyll
## 会自动安装依赖包
```

## 安装 `jekyll-paginate` 

```
gem install jekyll-paginate
```

## 修改`_config.xml` 添加以下内容

```
# paginate
gems: [jekyll-paginate]
paginate: 6

plugins: [jekyll-paginate]

```

## 执行`jekyll server`来查看效果
进入 git clone 下来的目录 ，执行`jekyll server -w -H 0.0.0.0` 启动服务，然后就可以通过`http://ip:4000`（ip换成自己的）端口来访问了。

```
[root@aeas gaohaoyang.github.io]# jekyll server -w -H 0.0.0.0
Configuration file: none
            Source: /root/gaohaoyang.github.io
       Destination: /root/gaohaoyang.github.io/_site
 Incremental build: disabled. Enable with --incremental
      Generating... 
                    done in 0.01 seconds.
 Auto-regeneration: enabled for '/root/gaohaoyang.github.io'
    Server address: http://0.0.0.0:4000
  Server running... press ctrl-c to stop.
```

