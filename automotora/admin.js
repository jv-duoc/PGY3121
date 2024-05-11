const urlLogin = 'https://pgy-api.vercel.app/api/automotora/login';//POST


async function login(){
    const botonLogin = document.getElementById('btn-login');
    botonLogin.setAttribute('disabled',true);
    try {

        const usuario = document.getElementById('usuario').value;
        const password = document.getElementById('pass').value;



        const cuerpo = {
            usuario,
            password
        }

        const json = JSON.stringify(cuerpo);
        console.log(json);

        const solicitudLogin = await fetch(urlLogin,{
            method:'POST',
            headers:{
                'content-type':'application/json'
            },
            body:json
        })
    } catch (error) {
        console.log(error);
    }
}