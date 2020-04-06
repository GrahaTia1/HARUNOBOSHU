        function postSignup(argName, argSex, argAge, argCollege, argDorm, argTel, argFirst, argSecond, argTime, argAdjust, argIntro) {
            //创建一个XMLHttpRequest 对象
            var xhr = new XMLHttpRequest();
            //准备发送请求的数据：url
            var url = "##";
            //使用HTTP POST请求与服务器交互数据
            xhr.open("POST", url, true);
            //设置发送数据的请求格式
            xhr.setRequestHeader('content-type', 'application/json');
            xhr.onreadystatechange = function() {
                if (xhr.readyState == 3) {
                    // loading();
                } else if (xhr.readyState == 4) {
                    // closeLoading();
                    //根据服务器的响应内容格式处理响应结果
                    if (xhr.getResponseHeader('content-type') === 'application/json') {
                        console.log(xhr.responseText);
                        var resultJSON = JSON.parse(xhr.responseText);
                        if (resultJSON.errcode === 0) {
                            alert("报名成功!");
                            reload();
                        }
                    } else {
                        console.log(xhr.responseText);
                        alert("发生错误");
                    }
                }
            }

            var sendData = {
                "Name": argName,
                "SEX": argSex,
                "AGE": argAge,
                "College": argCollege,
                "DIC": argDorm,
                "Tel": argTel,
                "FIRST": argFirst,
                "SECOND": argSecond,
                "timing": argTime,
                "FUCONG": argAdjust,
                "SELFPRO": argIntro,
            };
            //将用户输入值序列化成字符串
            console.log(JSON.stringify(sendData));
            xhr.send(JSON.stringify(sendData));
        }

        function postInfo() {
            var Name = $("#name").val();
            var SEX = $("input[name='sex']:checked").val();
            var AGE = $("input[name='grade']:checked").val();
            var College = $('select#college option:selected').val();
            var DIC = $("#dorm").val();
            var Tel = $("#tel").val();
            var FIRST = $('select#first option:selected').val();
            var SECOND = $('select#second option:selected').val();
            var timing = $('select#time option:selected').val();
            var FUCONG = $("input[name='adjust']:checked").val();
            var SELFPRO = $("#intro").val();
            console.log(Name, SEX, AGE, College, DIC, Tel, FIRST, SECOND, timing, FUCONG, SELFPRO)

            if (Name == '' || Name == undefined || Name == null) {
                //alert("请输入姓名");
                $("#label1").css('color', 'red'); //添加css样式
            } else {
                $("#label1").css('color', ''); //取消css样式
            }
            if (SEX == '' || SEX == undefined || SEX == null) {
                //alert("请输入姓名");
                $("#label2").css('color', 'red'); //添加css样式
            } else {
                $("#label2").css('color', ''); //取消css样式
            }
            if (AGE == '' || AGE == undefined || AGE == null) {
                //alert("请输入姓名");
                $("#label3").css('color', 'red'); //添加css样式
            } else {
                $("#label3").css('color', ''); //取消css样式
            }
            if (College == '' || College == undefined || College == null) {
                //alert("请输入姓名");
                $("#label4").css('color', 'red'); //添加css样式
            } else {
                $("#label4").css('color', ''); //取消css样式
            }
            if (DIC == '' || DIC == undefined || DIC == null) {
                //alert("请输入姓名");
                $("#label5").css('color', 'red'); //添加css样式
            } else {
                $("#label5").css('color', ''); //取消css样式
            }
            if (Tel == '' || Tel == undefined || Tel == null) {
                //alert("请输入姓名");
                $("#label6").css('color', 'red'); //添加css样式
            } else {
                $("#label6").css('color', ''); //取消css样式
            }
            if (FIRST == '' || FIRST == undefined || FIRST == null) {
                //alert("请输入姓名");
                $("#label7").css('color', 'red'); //添加css样式
            } else {
                $("#label7").css('color', ''); //取消css样式
            }
            if (timing == '' || timing == undefined || timing == null) {
                //alert("请输入姓名");
                $("#label9").css('color', 'red'); //添加css样式
            } else {
                $("#label9").css('color', ''); //取消css样式
            }
            if (FUCONG == '' || FUCONG == undefined || FUCONG == null) {
                //alert("请输入姓名");
                $("#label10").css('color', 'red'); //添加css样式
            } else {
                $("#label10").css('color', ''); //取消css样式
            }
            if (Name == '' || Name == undefined || Name == null || SEX == '' || SEX == undefined || SEX == null || AGE == '' || AGE == undefined || AGE == null || College == '' || College == undefined || College == null || DIC == '' || DIC == undefined || DIC == null || Tel == '' || Tel == undefined || Tel == null || FIRST == '' || FIRST == undefined || FIRST == null || timing == '' || timing == undefined || timing == null || FUCONG == '' || FUCONG == undefined || FUCONG == null) {
                alert("请填写相应的选项！");
                return;
            } else {
                postSignup(Name, SEX, AGE, College, DIC, Tel, FIRST, SECOND, timing, FUCONG, SELFPRO)
            }

        }