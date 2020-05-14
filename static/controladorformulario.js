const nombre=document.getElementById("name");
const numero=document.getElementById("numero");
const email=document.getElementById("email");
const date=document.getElementById("date");
const poss=document.getElementById("contrasena");
const poss1=document.getElementById("contrasena1");
const form=document.getElementById("form");
const parrafo=document.getElementById("warnings");


form.addEventListener("submit",e=>{
    e.preventDefault();
    let warnings="";
    let entrar= false;
    let regexEmail=/^\w+([\.-]?\w{)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/
   parrafo.innerHTML="";
    if(nombre.value.length<6){
        warnings+="El nombre no es válido. <br>";
        entrar=true;
    }
    if(!regexEmail.test(email.value)){
        warnings+="Correo no es válido. <br>";
        entrar=true;
    }
    if(poss.value!=poss1.value){
        warnings+="Las contraeñas no coinciden. <br>"
        entrar=true;
    }
    if(poss.value.length<8){
        warnings+="Las contraeñas es muy corta. <br>"
        entrar=true;
    }
    if(numero.value.length!=10){
        warnings+="El número no es válido <br>"
        entrar=true;
    }
    if(entrar){
        parrafo.innerHTML=warnings;
    }
})
