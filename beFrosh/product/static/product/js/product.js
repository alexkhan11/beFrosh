const product_btn = document.getElementById("add-product");
const product_form = document.getElementById("product-form");
const checkitlater_btns = document.querySelectorAll(".check-it-later");
const my_listings_btn = document.getElementById("my-listings-btn");
const favorites_btn = document.getElementById("favorites-btn");
const favorites_box = document.querySelector(".favorites");
const my_listings_box = document.querySelector(".my-listings");
const seller_update_box = document.getElementById("update-form-container");

function hide_display(el) {
  el.style.display = "none";
}
function show_display(el) {
  el.style.display = "block";
}

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

if (product_form) {
  product_form.addEventListener("submit", (e) => {
    e.preventDefault();
    add_product();
  });
}

if (favorites_btn) {
  favorites_btn.addEventListener("click", favorites);
}

if (my_listings_btn) {
  my_listings_btn.addEventListener("click", my_listings);
}

if (checkitlater_btns) {
  for (const btn of checkitlater_btns) {
    btn.addEventListener("click", checkitlater.bind(null, btn.id));
  }
}

function my_listings() {
  const url = "http://127.0.0.1:8000/product/my-listings/";
  const csrftoken = getCookie("csrftoken");
  fetch(url, {
    method: "POST",
    headers: {
      "X-CSRFToken": csrftoken,
    },
  })
    .then((jresp) => jresp.json())
    .then((resp) => render_listings(resp))
    .catch((error) => {
      console.log(error);
    });
}

function render_listings(resp) {
  const products = JSON.parse(resp["products"]);
  const ul = my_listings_box.querySelector("ul");

  for (const product of products) {
    ul.appendChild(product_element(product));
  }
  hide_display(favorites_box);
  hide_display(seller_update_box);
  show_display(my_listings_box);
}

function favorites() {
  const url = "http://127.0.0.1:8000/product/favorites/";
  const csrftoken = getCookie("csrftoken");
  fetch(url, {
    method: "POST",
    headers: {
      "X-CSRFToken": csrftoken,
    },
  })
    .then((jresp) => jresp.json())
    .then((resp) => render_favorites(resp));
}

function render_favorites(resp) {
  hide_display(my_listings_box);
  hide_display(seller_update_box);
  show_display(favorites_box);
  const ul = favorites_box.querySelector("ul");

  for (const product of resp) {
    ul.appendChild(product_element(product));
  }
}

function product_element(product) {
  let li = document.createElement("li");
  const img_url = "http://127.0.0.1:8000/media/" + product["fields"]["image"];

  li.innerHTML = ` 
    <div class="col-md-6 col-lg-4">
      <div class="card mb-3 custom-card-style">
        <div class="card-img">
          <img
          src=${img_url}
          class="img-fluid card-img-top custom-img"
          />
        </div>
      <div class="card-body">
        <a href="" class="custom-link1">
          <h4 class="card-text">${product["fields"]["title"]}</h4>
          <small class="mb-4"> ${product["fields"]["desc"]}</small>
        </a>
        <h5 class="mt-4 custom-link1">${product["fields"]["address"]}</h5>
        <div>
          <h5 class="float-right mt-3 card-text" style="color: black">
          ${product["fields"]["price"]} $
          </h5>
        </div>
      </div>
    </div>
  </div>`;

  return li;
}

function checkitlater(product_id) {
  const url = "http://127.0.0.1:8000/product/check-it-later/";
  const csrftoken = getCookie("csrftoken");
  const data = JSON.stringify({ product_id: product_id });
  fetch(url, {
    body: data,
    headers: {
      "X-CSRFToken": csrftoken,
    },
    method: "POST",
  })
    .then((jresp) => jresp.json())
    .then((resp) => {
      if (resp["message"]) {
        alert(resp["message"]);
      }
    });
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
    .then((resp) => show_message(resp, "add-product-msg"))
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
