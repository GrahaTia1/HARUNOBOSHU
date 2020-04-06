function postSearch(argTel) {
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
            //loading();
        } else if (xhr.readyState == 4) {
            closeLoading();
            //根据服务器的响应内容格式处理响应结果
            if (xhr.getResponseHeader('content-type') === 'application/json') {
                console.log(xhr.responseText);
                var resultJSON = JSON.parse(xhr.responseText);
                if (resultJSON.errcode === 0) {
                    var newData = eval("(" + data + ")");
                    var newName = data.Name;
                    var newSEX = data.SEX;
                    var newAGE = data.AGE;
                    var newCollege = data.College;
                    var newDIC = data.DIC;
                    var newTel = data.Tel;
                    var newFIRST = data.FIRST;
                    var newSECOND = data.SECOND;
                    var newtiming = data.timing;
                    var newFUCONG = data.FUCONG;
                    var newSELFPRO = data.SELFPRO;
                    localStorage.setItem("name", newName);
                    localStorage.setItem("sex", newSEX);
                    localStorage.setItem("age", newAGE);
                    localStorage.setItem("college", newCollege);
                    localStorage.setItem("dic", newDIC);
                    localStorage.setItem("tel", newTel);
                    localStorage.setItem("first", newFIRST);
                    localStorage.setItem("second", newSECOND);
                    localStorage.setItem("name", newtiming);
                    localStorage.setItem("fucong", newFUCONG);
                    localStorage.setItem("selfpro", newSELFPRO);
                    window.location.href = "page6.html";
                } else {
                    alert(resultJSON.errmsg);
                }
            } else {
                console.log(xhr.responseText);
                alert("发生错误");
            }
        }
    }

    var sendData = {
        "Tel": argTel,
    };
    //将用户输入值序列化成字符串
    console.log(JSON.stringify(sendData));
    xhr.send(JSON.stringify(sendData));

}

function search() {
    var Tel = document.getElementById("tel").value;
    console.log("用户输入:", Tel)
    postSearch(Tel)
}