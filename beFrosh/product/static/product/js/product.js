const product_btn = document.getElementById("add-product");
const product_form = document.getElementById("product-form");

product_form.addEventListener("submit", (e) => {
  e.preventDefault();
  add_product();
});

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function add_product() {
  const csrftoken = getCookie("csrftoken");
  const data = form_data(product_form);
  const url = "http://127.0.0.1:8000/product/add-listing/";
  fetch(url, {
    body: data,
    headers: {
      "X-CSRFToken": csrftoken,
    },
    method: "POST",
  })
    .then((jresp) => jresp.json())
    .then((resp) => {
      show_message(resp, "add-product-msg");
    })
    .catch((error) => console.log(error));
}

function show_message(resp, id) {
  if (resp["error-key"]) {
    document.getElementById(resp["error-key"]).classList.add("input-error");
  }
  if (resp["error"]) {
    document.getElementById(id).textContent = resp["message"];
  } else {
    window.location = resp["success_url"];
  }
}

function form_data(form) {
  let data = new FormData();
  for (const inp of form) {
    inp.classList.remove("input-error");

    if (inp.type == "file") {
      data.append(inp.id, inp.files[0]);
    } else {
      if (inp.tagName == "BUTTON") {
        continue;
      }
      data.append(inp.id, inp.value);
    }
  }
  return data;
}
