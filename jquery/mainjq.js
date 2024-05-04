
$(document).ready(()=>{
    const contenedorSaludo = $('#contenedor-saludo');
    contenedorSaludo.hide();
    const btnSaludar = $('#btn-saludar');

    btnSaludar.on('click',()=>{
        const inputNombre = $('#input-nombre');
        const nombre = inputNombre.val();

        contenedorSaludo.empty();
        

        const element = $('<div role="alert" class="alert"></div>');

        if(nombre && nombre.length > 2){
            element.addClass('alert-primary');
            element.text('Hola '+nombre+'👋🏼 !');
            contenedorSaludo.append(element);
        }else{
            element.addClass('alert-danger');
            element.text('❌ Debes escribir tu nombre!');
            contenedorSaludo.append(element);
        }
        contenedorSaludo.show(1000);
    })
});