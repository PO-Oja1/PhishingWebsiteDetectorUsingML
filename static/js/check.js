$(document).ready(function () {

  $("#loading").hide();

  $("#chk-btn").click(() => {
    $("#loading").show();
    $("#result").html("<p><p>");
    $("#remedy-list").html("<p><p>");
    let url = $("#ip-domain").val();
    console.log(url);

    $.ajax({
      type: "POST",
      url: "/predict",
      data: JSON.stringify(url),
      contentType: "application/json",
      success: function (data) {
        $("#loading").hide();
        let btn = "<button class='btn btn-success'>Good</button>";
        if (data["op"] == "bad") {
          btn = `<button class='btn btn-danger'>Bad</button><h4>IP:${data['ip']}</h4><h4>Location:${data['location']}</h4>`;
        }
        let ip;
        console.log(data);
        $("#result").append(btn);
        let links = data["links"];

      
        if (data["op"] == "bad") {
          for (let i = 0; i < links.length; i++) {
            $("#remedy-list").append(
              " <li class='list-group-item'>" + links[i] + "</li>"
            );
            console.log(links[i]);
            if (i > 10) {
              break;
            }
          }
         
        }
      },
    });
  });
});
