# BBT报名表学习

### 1.设计

【风格】

&emsp;1、bbt风格不一定是绿的，也不一定要梯仔。可以是插画，水彩，手绘等等。探索自己喜欢的风格（浏览设计网站，或者收藏自己喜欢的图片。xnview）

&emsp;2、去看看别人的作品找灵感。可以看看排版，或者是颜色搭配，元素之类

&emsp;3、顺序：逻辑——排版——动效等效果

【设计图】

&emsp;1、色彩搭配，不要过多，注意突出主体。

&emsp;2、按钮：

&emsp;&emsp;可以用背景图某一元素当按钮的图案，不一定要是方的，也不一定是有突出效果。

&emsp;&emsp;与背景的颜色区别开来。

&emsp;&emsp;按钮的文字指示要清晰。

&emsp;&emsp;考虑优先级，排版注意。

&emsp;3、可用性,可读性

&emsp;&emsp;可点击区域要大一点，字要清晰

&emsp;&emsp;与背景颜色区分

&emsp;&emsp;标点不能在一行的开头。检查一下。

&emsp;&emsp;特殊情况：如显示院名称，要考虑很长名字的框里塞不塞的下。填错时。

&emsp;&emsp;主体内容放在视觉中心，不要太高。

&emsp;4、对齐，不仅好看，前端也可以方便些。

&emsp;5、不要语文作图。从视觉上直观地展示一张图。


【与前端对接】

&emsp;1、字体：少部分字体给图片，如果某种字体应用很多的话最好用系统字体，不然加载很慢。可以不用给字体包。

&emsp;2、标注：标字体，大小，颜色，距离，

&emsp;3、线框图不能改动

&emsp;4、图片的命名用英文

***
### 2.前端

&emsp;&emsp;1.文件命名尽量以功能性命名，方便看懂。

&emsp;&emsp;2.强调html、css、js分装的重要性，注意js文件与网页的代码顺序，是否优先网页加载（可节省网页全部加载的时间）

&emsp;&emsp;3.与后端预先做好对接，与设计事先确定设计稿，防止写废代码

&emsp;【css】

&emsp;&emsp;4.排版时避免使用</br>或空格来进行排版，应尽量多用 text-indent 或盒子模型来进行排版

&emsp;&emsp;5.如果要把css封装在一个文件里要注意对h5内的类名与id的命名

&emsp;&emsp;6.按钮的制作尽量避免以图片为按钮，按钮的样式可以参考网上不同风格的按钮代码

&emsp;【js】

&emsp;&emsp;7.js部分可以使用循环来避免冗长的代码。（可以用一个数组存变量名，另一个数组存属性名。进行for循环直接遍历取值）

&emsp;&emsp;8.通过jQuery及循环添加div可减少大量重复代码

&emsp;&emsp;9.用console.log()来判断js代码是否有错误

&emsp;&emsp;10.swiper插件的使用

***
### 3.后端

#第一次合锅后端总结

​	希望能把自己在这几周学到的东西都能总结一下。因为真的非常容易忘记，很多时候要用到的时候都要去再查一遍，不过可能再用多几次就能熟练一些了。

​	所有POST请求的content-type都使用application/json, 即使用json作为请求的消息的数据格式.

​	@app.route('', methods=['POST'])我们定义了decorators_demo, 并且用它来修饰test函数, 此时test函数作为参数传入到了decorate的f形参, 此时执行的是decorators_demo函数, 并且在打印出kwds之后, 返回执行test

​	 使用flask的session时, 不可将敏感数据存入其中, 因为前端是可以直接获取到的。 如果要在其中存入用户状态或用户的相关信息, 最好如上面一样存入id, 后端通过id去查询用户具体信息.

​	data=request.get_json()在这里（不只是这里）要和前端建立好接口文档，注意数据的类型，然后在POSTMAN上看看有没有bugx

​	然后进行数据库的增删查改 并返回各种信息（除了敏感数据）在执行语句之后要返回是否成功这样的结果这里用的是

try:    

except pymysql.Error as e:

https://www.runoob.com/mysql/mysql-insert-query.html

https://www.runoob.com/mysql/mysql-where-clause.html

 这里要注意的是SQL的注入 这里用的方法是把数据先封装在一并发送，能避免因为%导致的注入（这是第一种解决方法参数化查询第二种orm看起来比较难就没有怎么了解x）

self.cur.execute('Insert into `stud`values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")',args)

​	正则表达式的验证手机号：

```pyhton
phone_pat = re.compile('^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$')
phone=11451419191
res = re.search(phone_pat, phone)
 if res:
        print('正常手机号')
    else:
        print('不是手机号')
```

另外还需要导出数据库https://www.cnblogs.com/yuwensong/p/3955834.html	

从JA那里拿了一份关于状态码的flask，这几天再看看实现

​	之前的FLASK学的并不好，大概是只知道怎么用而不了解为什么这么用，部长给了我多看看底层代码及其实现的建议以及多使用postman尝试的建议。在做了一些学习和尝试后，我对底层的实现也有了一些理解，但最近作业还有社团的锅也比较多看的不够深入，希望闲下来之后能静下心来继续学习。感觉还是时间分配的问题，以后会继续加油。