const search = document.querySelector(".main-search");
const products_box = document.querySelector(".products-box");
const catagory_btns = document.querySelectorAll(".catagory-btn");

catagory_btns.forEach((btn) => {
  btn.addEventListener("click", (e) => {
    const data = { catagory: e.target.getAttribute("catagory") };
    search_products(data);
  });
});

search.addEventListener("keyup", (e) => {
  const data = { search_text: search.value };
  search_products(data);
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

function search_products(data) {
  const csrftoken = getCookie("csrftoken");
  const url = "http://127.0.0.1:8000/search/";
  fetch(url, {
    method: "POST",
    body: JSON.stringify(data),
    headers: {
      "X-CSRFToken": csrftoken,
      Accept: "application/json",
    },
  })
    .then((jresp) => jresp.json())
    .then((resp) => render_products(resp));
}

function render_products(resp) {
  const ul = products_box.querySelector("ul");
  ul.innerHTML = "";

  for (const product of resp) {
    ul.appendChild(product_el(product));
  }
}

function product_el(product) {
  let li = document.createElement("li");
  const img_url = "http://127.0.0.1:8000/media/" + product["fields"]["image"];
  li.innerHTML = ` 
  <div class="col-md-6 col-lg-4">
    <div class="card mb-3 custom-card-style">
        <div class="card-img">
        <img
            src="${img_url}"
            class="img-fluid card-img-top custom-img"
            alt="${product.fields.title}"
        />
    </div>
    <div class="card-body">
        <a href="" class="custom-link1">
            <h4 class="card-text">${product.fields.title}</h4>
            <small class="mb-4"> ${product.fields.desc}</small>
        </a>
        <h5 class="mt-4 custom-link1">${product.fields.address}</h5>
        <h1>fdssd</h1>
        <a href="" class="h6 custom-link">
            Sale by: ${product.fields.seller}    
        </a>
    <div>
      <button
        class="check-it-later fa fa-download mr-2 mt-3 float-left custom-link"
        id="${product.pk}"
        >Check it later</button>

      <h5 class="float-right mt-3 card-text" style="color: black">
        ${product.fields.price} $
      </h5>
    </div>
  </div>
</div>
</div>`;

  return li;
}
