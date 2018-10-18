var pass1 = document.querySelector("#Password");
var pass2 = document.querySelector("#Password2");
registerBtn = document.querySelector("#register");


pass2.addEventListener("input" , ()=>{
  if (pass1.value === pass2.value){
    registerBtn.disabled= false;
  }else {
    registerBtn.disabled= true;
  }
});
