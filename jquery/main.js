const btnSaludar = document.getElementById('btn-saludar');

btnSaludar.addEventListener('click',()=>{
    const inputNombre = document.getElementById('input-nombre');
    const nombre = inputNombre.value;
    const contenedorSaludo = document.getElementById('contenedor-saludo');
    

    contenedorSaludo.innerHTML = '';

    let element = document.createElement('div');
    element.setAttribute('role','alert');
    element.classList.add('alert');

    if(inputNombre.reportValidity() && nombre){
        element.classList.add('alert-primary');
        element.innerText = 'Hola '+nombre+'👋🏼 !';
        contenedorSaludo.appendChild(element);
    }else{
        element.classList.add('alert-danger');
        element.innerText = '❌ Debes escribir tu nombre!';
        contenedorSaludo.appendChild(element);
    }

    contenedorSaludo.style = 'display:block';
});

