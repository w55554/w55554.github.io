---
layout: post
title:  "使用 Simple-Jekyll-Search 创建全文搜索"
date:   2020-05-19 16:30:54
categories: jekyll
tags: jekyll Simple-Jekyll-Search
author: 雨田
mathjax: true
---

* content
{:toc}

## 下载 `Simple-Jekyll-Search` 文件
百度搜索出来的一个有用的都没有，看来还是得找谷哥啊（在这里BS一下百度）。
```
git clone https://github.com/christian-fei/Simple-Jekyll-Search.git
```
克隆完成后，在目录下`Simple-Jekyll-Search/dest/`找到 `simple-jekyll-search.js`文件，把这个文件复制到我们的jekyll的js目录下，以下是我的目录结构
```
[root@aeas w55554.github.io]# ll js/
total 76
-rw-r--r-- 1 root root 1623 May 18 13:46 main.js
-rw-r--r-- 1 root root 22946 May 18 13:46 masonry.pkgd.min.js
-rw-r--r-- 1 root root 5371 May 18 13:46 pageContent.js
-rw-r--r-- 1 root root 9618 May 18 17:26 simple-jekyll-search.js
-rw-r--r-- 1 root root 5014 May 18 13:46 smooth-scroll.min.js
-rw-r--r-- 1 root root 10737 May 18 13:46 waterfall.js
```






## 在网站根目录下添加`search.json`，内容如下
```
---
layout: null
---
[
  {% for post in site.posts %}
    {
      "title" : "{{ post.title | escape }}",
      "category" : "{{ post.category }}",
      "tags" : "{{ post.tags | join: ', ' }}",
      "url" : "{{ site.baseurl }}{{ post.url }}",
      "date" : "{{ post.date }}"
    } {% unless forloop.last %},{% endunless %}
  {% endfor %}
]
```


## 在`_sass`目录下修改`_index.css`文件，在文件末尾添加以下内容
```
#search-input {
    width: 90%;
    height: 35px;
    color: #333;
    background-color: rgba(227,231,236,.2);
    line-height: 35px;
    padding:0px 16px;
    border: 1px solid #c0c0c0;
    font-size: 16px;
    font-weight: bold;
    border-radius: 17px;
    outline: none;
    box-sizing: border-box;
    box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102,175,233,.6);
}
#search-input:focus {
    outline: none;
    border-color: rgb(102, 175, 233);
    background-color: #fff;
    box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px #007fff;
}
```

## 修改`_layout/default.html`文件，添加一下内容：
```
<script src="{{ " /js/simple-jekyll-search.js " | prepend: site.baseurl }}" charset="utf-8"></script>

<script type="text/javascript">
SimpleJekyllSearch({
    searchInput: document.getElementById('search-input'),
    resultsContainer: document.getElementById('results-container'),
    json: '/search.json',
    searchResultTemplate: '<li><a href="{url}" title="{desc}">{title}</a></li>',
    noResultsText: '没有搜索到文章',
    limit: 20,
    fuzzy: false
  })
</script>
```

## 修改`index.html` 文件
修改根目录下的`index.html`文件，在`Recent Posts`上面添加一下段
```
 <div class="side">
                <div id="search-container">
                    <input type="text" id="search-input" placeholder="search...">
                    <ul id="results-container"></ul>
                </div>
            </div>
```
