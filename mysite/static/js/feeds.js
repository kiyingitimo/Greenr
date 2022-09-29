if ($.cookie("email") == undefined) {
    window.location = "/"
}
$("#logout").click(function(){
    $.removeCookie("email")
    $.removeCookie("password")
    window.location = "/"

})
$.post( "/getdata", {"email":$.cookie("email"),"password":$.cookie("password")}, function( data ) {
    $("#name").text(data.username)
    $("#estdate").text(data.estdate)

},"json");
function displayPost(post_data) {
    if (post_data.author == undefined) {
        return
    }
    var post = $( "#post_template" ).clone()
    var id = String(Date.now())
    post.attr("id",id)
    post.appendTo("body")
    $("#"+id).children(".post-cnt").html("<p>"+post_data.content+"</p>")
    var q = $("#"+id).children(".post-bts").children(".comment")
    q.attr("onclick","comment('"+post_data.id+"')")
    var o = $("#"+id).children(".post-bts").children(".save")
    o.attr("onclick","save('"+post_data.id+"')")
    $.get("/getname?email="+post_data.author,function(e) {
        $("#"+id).children(".post-header").children(".name").text(e)
    })
    $.get("/nolikes?post="+post_data.id+"&"+"group=default",function(e) {
        var g = $("#"+id).children(".post-bts").children(".like")
        g.attr("onclick","like('"+post_data.id+"'"+","+"'"+id+"')")
        $("#"+id).attr("post_id",post_data.id)
        g.html("<img src='/static/images/like icon.png' height='20px' ><br>Like <br>("+e+" like(s))")
    })
    $("#"+id).children(".post-header").children(".birthdate").text(post_data.birthdate)
}
function like(code,id) {
    $.post("/like",{"email":$.cookie("email"),"password":$.cookie("password"),"post":code,"group":"default"},function(e) {
        var g = $("div[post_id="+code+"]").children(".post-bts").children(".like")
        // console.log(e)
        g.html("Like <br>("+e+" like(s))")
    })
}
$("#submit_post").click(function () {
    var content = $("#post_text").val()
    // console.log(content)
    $("#post_text").val("")
    $.post( "/makepost",{"email":$.cookie("email"),"password":$.cookie("password"),"content":content},function (data) {
        // console.log(data)
        displayPost(data)
    } ,"json");
    post_modal.css("display","none")
})
$("#submit_croom").click(function() {
    var content = $("#croom_text").val()
    $("#croom_text").val("")
    $.post("/createroom",{"email":$.cookie("email"),"password":$.cookie("password"),"name":content},function (data) {
        console.log(data)
    },"json")
    croom_modal.css("display","none")
})
function download(file, text) {
    //creating an invisible element
    var element = document.createElement('a');
    element.setAttribute('href',
    'data:text/plain;charset=utf-8, '
    + encodeURIComponent(text));
    element.setAttribute('download', file);

    // Above code is equivalent to
    // <a href="path of file" download="file name">

    document.body.appendChild(element);

    //onClick property
    element.click();

    document.body.removeChild(element);
}
function save(code) {
    $.get("/save?post="+code,function(e) {
        download("POST-"+code+".txt",e)
    })
}
$("#qbt").click(function(){
    var txt = $("#q").val()
    $(':not(#post_template).post').remove()
    $(".loadingio-spinner-ball-3azh9u0yuyo").css("display","inline-block")
    $.getJSON("/search?q="+txt,function(e){
        var results = e.results
        $(".loadingio-spinner-ball-3azh9u0yuyo").css("display","none")
        for (i in results) {
            displayPost(results[i])
        }
    })
})

var post_modal = $("#postModal")
var post_btn = $("#post")
var post_span = $("#post_close")
post_btn.click(function() {
    post_modal.css("display","block")
})
post_span.click(function() {
    post_modal.css("display","none")
})
var spost_modal = $("#spostModal")
var spost_btn = $("#spost")
var spost_span = $("#spost_close")
spost_btn.click(function() {
    spost_modal.css("display","block")
})
spost_span.click(function() {
    spost_modal.css("display","none")
})
var comment_modal = $("#commentModal")
var comment_btn = $("#comment")
var comment_span = $("#comment_close")
function comment(code) {
    $.getJSON("/getcomments?post="+code,function(data){
        $("#comments").html(`<div class="room-s-bts" style="margin-bottom:50px;padding:10px;background:whitesmoke;" id="comment_template">
    			<img src="/static/dump/avatar.png" class="room-s-pic">
    			<h5 class="name">Michael Greener</h5><br>
    			<p class="content">Hello this is a Comment</p>
    		</div>`)
        for (i in data.posts){
            i = data.posts[i]
            var c = $("#comment_template").clone()
            var id = String(Date.now())
            c.attr("id",id)
            c.appendTo("#comments")
            $("#"+id).children(".name").text(i.user)
            $("#comment_text").val("")
            $("#"+id).children(".content").text(i.content)
        }
    })
    comment_modal.attr("cpost",code)
    comment_modal.css("display","block")
}
$("#submit_comment").click(function() {
    $.post("/comment",{"email":$.cookie("email"),"password":$.cookie("password"),"post":comment_modal.attr("cpost"),"content":$("#comment_text").val()},function(data){
        var c = $("#comment_template").clone()
        var id = String(Date.now())
        c.attr("id",id)
        c.appendTo("#comments")
        $("#"+id).css("display","block")
        $("#"+id).children(".name").text(data.user)
        $("#comment_text").val("")
        $("#"+id).children(".content").text(data.content)
    },"json")
})
comment_span.click(function() {
    comment_modal.css("display","none")
})

function fetchAndDisplayPost() {
    $.getJSON("/getpost",function(e) {
        displayPost(e)
    })
}
$(window).scroll(function(){

   var position = $(window).scrollTop();
   var bottom = $(document).height() - $(window).height();

   if( position == bottom ){
      fetchAndDisplayPost();
   }

});
var x = 0
while (x != 5) {
    fetchAndDisplayPost()
    x++
}