const sidebar = document.querySelector(".sidebar");
const menu = document.querySelector(".menu");
if(menu){
  menu.addEventListener("click", function () {
    sidebar.classList.toggle("sidebar-width-max");
  });
}


