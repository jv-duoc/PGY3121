function mostrarMensaje(mensaje){
    const textP = document.querySelector('#modal-mensaje p');
    textP.innerText = mensaje;

    const bModal = new bootstrap.Modal('#modal-mensaje',{});
    bModal.show();
}


async function verificar(){

    const btn = document.getElementById('btn-verificar');
    btn.setAttribute('disabled',true);

    const url = 'https://api.boostr.cl/holidays.json';
    
    const datePicker = document.getElementById('fecha');
    if(datePicker.reportValidity() && datePicker.value){
        try {

            const solicitud = await fetch(url);
            
            const datosFeriados = await solicitud.json();

            const feriados = datosFeriados.data;

            let esFeriado = undefined;
            const fechaSeleccionada = datePicker.value;

            for (const fecha of feriados) {
                if(fecha.date == fechaSeleccionada){
                    esFeriado = fecha;
                    break;
                }
            }

            if(esFeriado){

                console.log(esFeriado);

                mostrarMensaje('La fecha es feriado por que:'+esFeriado.title)
            }else{
                mostrarMensaje('No es feriado');
            }


        } catch (error) {
            mostrarMensaje('Ocurrió un error al recoger los datos.')
        }
    }else{
        mostrarMensaje('Selecciona una fecha!')
    }

    btn.removeAttribute('disabled');
}