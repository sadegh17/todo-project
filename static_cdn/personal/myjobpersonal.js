var newjob = document.querySelector(".newjob");
var form = document.querySelector(".form");
var arrow = document.querySelectorAll(".arrow");



newjob.addEventListener("click" , ()=>{
  form.classList.toggle("d-none");
});
arrow.forEach(function(element) {
  element.addEventListener("mouseenter" , ()=>{
    element.style.backgroundColor='#87DBDB';
  });
  element.addEventListener("mouseleave" , ()=>{
    element.style.backgroundColor='white';
  });
});
