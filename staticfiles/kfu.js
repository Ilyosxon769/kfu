
let id = (id) => document.getElementById(id);

let classes = (classes) => document.getElementsByClassName(classes);

let username = id("username"),
  firstname=id("firstname"),
  lastname = id("lastname"),
  tel = id("tel"),
  tamomlagan_joy = id("tamomlagan_joy"),
  diplom = id("diplom"),
  pasport = id("pasport"),
  pasport_rasm = id("pasport_rasm"),
  rasm = id("rasm"),
  diplom_rasm = id("diplom_rasm"),
  form = id("form"),
  sel=id("sel"),
  errorMsg = classes("error"),
  successIcon = classes("success-icon"),
  failureIcon = classes("failure-icon");

form.addEventListener("submit", (e) => {
  if(username.value&& firstname.value && lastname.value &&
    tel.value && tamomlagan_joy.value &&
    diplom.value && pasport.value && pasport_rasm.value &&
    rasm.value && diplom_rasm.value&& sel.value!=='' ){}else{e.preventDefault();}

console.log('salom');
console.log(sel.value)
  engine(username, 0, "Ma'lumot kiritilmadi!");
  engine(firstname, 1, "Ma'lumot kiritilmadi!");
  engine(lastname, 2, "Ma'lumot kiritilmadi!");
  engine(tel, 3, "Ma'lumot kiritilmadi!");
  engine(tamomlagan_joy, 4, "Ma'lumot kiritilmadi!");
  engine(sel,5, "Ma'lumot kiritilmadi!");
  engine(diplom, 6  , "Ma'lumot kiritilmadi!");
  engine(pasport, 7  , "Ma'lumot kiritilmadi!");
  engine(pasport_rasm, 8  , "Ma'lumot kiritilmadi!");
  engine(rasm, 9  , "Ma'lumot kiritilmadi!");
  engine(diplom_rasm, 10  , "Ma'lumot kiritilmadi!");
  
},false);

let engine = (id, serial, message) => {
  if (id.value.trim() === "") {
    errorMsg[serial].innerHTML = message;
    id.style.border = "1px solid red";

    failureIcon[serial].style.opacity = "1";
    successIcon[serial].style.opacity = "0";
  } else {
    errorMsg[serial].innerHTML = "";
    id.style.border = "2px solid green";
    
    failureIcon[serial].style.opacity = "1";
    successIcon[serial].style.opacity = "0";
    
}
};

function dipfun(){
  dipval=document.getElementById('diplom').value;
  console.log(dipval);
  fetch(`/api?dip=${dipval}`)
  .then(res=> res.json())
  .then(data=>{
    if(data.diplom==='yes'){
      diplom.style.border = "1px solid red";
      errorMsg[6].innerHTML = 'Bunday seriya mavjud!';
    }else{
      errorMsg[6].innerHTML = "";
      diplom.style.border = "2px solid green";
    }
  })
  .catch(err=>console.log(err));
}
function pasfun(){
  pasval=document.getElementById('pasport').value;
  console.log(pasval);
  fetch(`/api?pas=${pasval}`)
  .then(res=> res.json())
  .then(data=>{
    console.log(data)
    if(data.pasport==='yes'){
      pasport.style.border = "1px solid red";
      errorMsg[7].innerHTML = 'Bunday seriya mavjud!';
    }else{
      errorMsg[7].innerHTML = "";
      pasport.style.border = "2px solid green";
    }
  })
  .catch(err=>console.log(err));
}