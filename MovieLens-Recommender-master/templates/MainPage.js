$(function(){
    $("#OptionInputContainer").hide();
    $("#UserInput").focus(function(){
    if($(this).prop("value")=="请输入要推荐的用户ID")
        {
            $(this).prop("value","");
            $(this).css("color","white");
        }
      $("#OptionInputContainer").fadeIn();
    });
    $("#UserInput").blur(function(){
    	if($(this).prop("value")=="")
	    {
            $(this).prop("value","请输入要推荐的用户ID");
            $(this).css("color","#CCCCCC");
        }
    });
    $("#OptionConfirm").click(function(){
        var Content=$("#UserInput").val();
        var LeftOption=$("#LeftOptionContainer option:checked").val()
        var RightOption=$("#RightOptionContainer option:checked").val()
        $.post("http://127.0.0.1:2020/submit",
        {
            Content:Content,
            LeftOption:LeftOption,
            RightOption:RightOption
        },
        function(data,status){
            alert("推荐成功")
            $("#BottomContainer").empty()
            $("#BottomContainer").prepend(data)
//            alert(data["res"])
        }).fail(function(){alert("推荐失败，用户ID不存在")
        });
//        $.ajax({
//            url: "http://127.0.0.1:2020/submit",
//            type: "post",  // 或 get， 大小写都可以
//            data: {Content:Content},
//            async: false,
//            // contentType:"application/json", //指定内容格式,一般发送字典可省略
//            // dataType: "json",  // 服务器响应的数据类型,python flask 返回jsonify 字典数据时可以省略,如果后端上传文件，则不能是json类型
//            error:function(error){
//                alert(error)},
//            success:function(data){
//            alert(data);}
//            });
    });
    $("#OptionCancel").click(function(){
        $("#OptionInputContainer").fadeOut();
    });
});
