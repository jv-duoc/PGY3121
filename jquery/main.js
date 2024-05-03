const btnSaludar = document.getElementById('btn-saludar');

btnSaludar.addEventListener('click',()=>{
    const inputNombre = document.getElementById('input-nombre');
    const nombre = inputNombre.value;
    const contenedorSaludo = document.getElementById('contenedor-saludo');
    const parrafo = document.getElementById('texto-saludo');
    
    if(inputNombre.reportValidity()){
        removerClases(parrafo);
        parrafo.classList.add('alert-primary');
        parrafo.innerText = 'Hola '+nombre+'!';
        
    }else{
        removerClases(parrafo);
        parrafo.classList.add('alert-danger');
        parrafo.innerText = 'Debes escribir tu nombre en el input!';
    }

    contenedorSaludo.style = 'display:block';
});

function removerClases(elemento){
    elemento.classList.remove('alert-primary','alert-danger');
}