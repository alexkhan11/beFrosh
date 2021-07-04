const product_btn = document.getElementById("add-product");
const product_form = document.getElementById("product-form");
console.log(product_form);
product_form.addEventListener("submit", (e) => {
  e.preventDefault();
  add_product();
});
function add_product() {
  const data = form_data(product_form);
  const url = "";
  fetch(url, { body: data, method: "POST" })
    .then((jresp) => jresp.json())
    .then((resp) => console.log(resp))
    .catch((error) => console.log(error));
}

function form_data(form) {
  let data = {};
  for (const inp of form) {
    data[inp.id] = inp.value;
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
