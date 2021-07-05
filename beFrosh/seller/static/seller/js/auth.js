const login_btn = document.getElementById("login-btn");
const register_btn = document.getElementById("register");
const register_form = document.getElementById("register-form");
const seller_update_btn = document.getElementById("update-account-btn");
const seller_form = document.getElementById("seller-form");

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

const csrftoken = getCookie('csrftoken');

if (login_btn) {
  login_btn.addEventListener("click", login);
}

if (register_form) {
  register_form.addEventListener("submit", (e) => {
    e.preventDefault();
    register();
  });
}
//CHECKING FOR IF FILE CONTAINS THIS FORM OTHERWISE WILL BE ERROR
if (seller_form) {
  seller_form.addEventListener("submit", (e) => {
    e.preventDefault();
    seller_update();
  });
}

function register() {
  const url = "http://127.0.0.1:8000/seller/register/";
  const csrftoken = getCookie('csrftoken');
  //GIVE FORM NODE IT RETURNS OBJECTS CONTAINING VALUE AS VALUE AND INPUT ID AS PROPERTY
  const data = JSON.stringify(form_data(register_form));
  fetch(url, {
    method: "POST",
    headers:{
      'X-CSRFToken': csrftoken,
      'Accept': 'application/json',
      },
    body: data,
  })
    .then((jresp) => jresp.json())
    .then((resp) => {
      show_message(resp, "reg-error-msg");
    });
}

function login() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;
  const csrftoken = getCookie('csrftoken');

  console.log("clicked");
  console.log(csrftoken);
  const data = JSON.stringify({ password: password, username: username });
  const url = "http://127.0.0.1:8000/seller/login/";
  fetch(url, {
    headers:{
      'X-CSRFToken': csrftoken,
      'Accept': 'application/json',
      },
    body: data,
    method: "POST",
  })
    .then((jresp) => jresp.json())
    .then((resp) => {
      show_message(resp, "login-error");
    })
    .catch((error) => {
      console.log(error);
    });
}

function seller_update() {
  const url = "http://127.0.0.1:8000/seller/become-seller/";

  const csrftoken = getCookie('csrftoken');

  console.log("clicked");
  console.log(csrftoken);

  const data = JSON.stringify(form_data(seller_form));

  fetch(url, {
    headers:{
      'X-CSRFToken': csrftoken,
      'Accept': 'application/json',
      },
    method: "POST",
    body: data,
  })
    .then((jresp) => jresp.json())
    .then((resp) => {
      show_message(resp, "update-error-msg");
    });
}

function form_data(form) {
  let data = {};
  for (const inp of form) {
    if (inp.tagName == "INPUT") {
      data[inp.id] = inp.value;
    }
  }
  return data;
}

function show_message(resp, id) {
  if (resp["error"]) {
    document.getElementById(id).textContent = resp["message"];
  } else {
    window.location = resp["success_url"];
  }
}
