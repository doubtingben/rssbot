function mark_as_read(divid) {
  $("#" + divid).children(".content").show();
  $("#" + divid).children(".content").html("<center><img src='/rssbot/ajax-loader.gif'><br /><b>Deleting selection!</b></center>");
  $.ajax({
          type: "POST",
          url: "/rssbot/rssbot.js",
          data: "{}",
          complete: function (xhr, textStatus) {
              if (textStatus == 'error') {
                $("#" + divid).children(".content").show();
                $("#" + divid).children(".content").html("Status: " + xhr.status + " - " + xhr.statusText);
              } else {
                $("#" + divid).hide();
              }
          },
        });
}

function loaddoc() {
  $(".log_button").click(function(){
    $(".loginform").toggle()
    }
  );
  $(".formsubmit").click(function(){
    $.ajax({
      type: "POST",
      data: "username=" + $("#username").attr('value') +
            "& password=" + $("#password").attr('value'),
      url: "/mysite/login/",
      complete: function (xhr, textStatus) {
        if (textStatus == 'error') {
          $(".loginform .error").show();
          $(".loginform .error").html("Status: " + xhr.status + " - " + xhr.statusText);
        } else {
          $(".loginform .error").html("Status: " + xhr.status + " - " + xhr.statusText);
        }
            },
                });
      }
              
  );
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
