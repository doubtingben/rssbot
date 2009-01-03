function mark_as_read(divid) {
  $("#" + divid).children(".content").show();
  $("#" + divid).children(".content").html("<center><img src='/rssbot/ajax-loader.gif'><br /><b>Deleting selection!</b></center>");
  $.post("/rssbot/mark_as_read/" + divid, function(data) {
          alert("data loaded: " + data);});
}

function loaddoc() {
  $(".accordion .content").hide();
  $(".accordion .footer .window").hide();
  $(".accordion .title").click(function(){
    $(this.parentNode.parentNode).children(".content").toggle();
    $(this).toggleClass("active");
    $(this).siblings(".title").removeClass("active");
    }
  );
  $(".accordion .header .controls").click(function() {
    mark_as_read($(this.parentNode.parentNode).attr("id"));
    }
  );
  $(".accordion .footer .controls").click(function() {
    mark_as_read($(this.parentNode.parentNode.parentNode).attr("id"));
    }
  );
  $(".accordion .footer .send_link").click(function() {
    $(this.parentNode).children(".window").show();
    $(this.parentNode).children(".window").html("Sending selection!");
    }
  );
  $(".accordion .footer .follow_link").click(function() {
    $(this.parentNode).children(".window").show();
    $(this.parentNode).children(".window").html("Following link!");
    }
  );
}
