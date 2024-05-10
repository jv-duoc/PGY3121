document.getElementById('escanear').addEventListener('click',async ()=>{

    const inputArchivo = document.getElementById('foto');

    const foto = inputArchivo.files[0];

    if(foto){
        //
        const url = 'http://api.qrserver.com/v1/read-qr-code/';

        try {

            let formulario = new FormData();
            formulario.append('file',foto,foto.name);

            const solicitud = await fetch(url,{
                method:'POST',
                body:formulario
            });
            const datos = await solicitud.json();
            console.log(datos);
        } catch (error) {
            alert('Ocurrió un error!');
        }
    }

});