function mark_as_read(divid) {
  $("#" + divid).children(".content").show();
  $("#" + divid).children(".content").html("<center><img src='/rssbot/ajax-loader.gif'><br /><b>Deleting selection!</b></center>");
  $.ajax({
          type: "POST",
          url: "/rssbot/rssbot.js",
          data: "{}",
              //          success: alert("Marked as read : " + divid),
              //          error: function(XMLHttpRequest, textStatus, errorThrown) {
              //alert("Status: " + XMLHttpRequest.status + " - " + XMLHttpRequest.statusText);
              //},
          complete: function (xhr, textStatus) {
              if (textStatus == 'error') {
                alert("Status: " + xhr.status + " - " + xhr.statusText);
              } else {
                $("#" + divid).hide();
              }
          },
        });
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
