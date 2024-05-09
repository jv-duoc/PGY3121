function mostrarMensaje(mensaje){
    const textP = document.querySelector('#modal-mensaje p');
    textP.innerText = mensaje;

    const bModal = new bootstrap.Modal('#modal-mensaje',{});
    bModal.show();
}


function verificar(){
    
    const datePicker = document.getElementById('fecha');
    if(datePicker.reportValidity() && datePicker.value){

    }else{
        mostrarMensaje('Selecciona una fecha!')
    }
}