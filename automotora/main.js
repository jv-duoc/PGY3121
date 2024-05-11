const urlAutos = 'https://pgy-api.vercel.app/api/automotora/autos';//GET,POST,DELETE
const urlLogin = 'https://pgy-api.vercel.app/api/automotora/login';//POST
const urlDolar = 'https://mindicador.cl/api';
const contenedorAutos = document.getElementById('lista');

var autosEnCarrito = []

main();


document.getElementById('carrito').addEventListener('show.bs.offcanvas',()=>{
    cargarOffCanvas();
});

function cargarOffCanvas(){
    const carritoContenedor = document.getElementById('carrito-contenedor');
    carritoContenedor.innerHTML = '';

    for (const auto of autosEnCarrito) {
        const itemAuto = document.createElement('div');
        itemAuto.classList.add('auto-en-carrito');
        const nombreP = document.createElement('p');
        nombreP.innerText = auto.modelo+' $'+auto.precio.toLocaleString('es-CL');
        itemAuto.append(nombreP);

        const botonBorrar = document.createElement('button');
        botonBorrar.classList.add('btn','btn-danger');
        botonBorrar.innerText = 'Quitar';

        itemAuto.append(botonBorrar);
        botonBorrar.addEventListener('click',()=>{
            quitarDelCarrito(auto)
        })

        carritoContenedor.append(itemAuto);
    }

}

function quitarDelCarrito(auto){
    var nuevoCarrito = [];
    for (const i of autosEnCarrito) {
        if(i.id != auto.id){
            nuevoCarrito.push(i)
        }
    }
    autosEnCarrito = nuevoCarrito;
    guardarCarrito();
    cargarOffCanvas();
}

async function main(){

    cargarCarrito();

    const plantilla = document.getElementById('auto-plantilla');
    plantilla.remove();

    try {

        const solicitudIndicadores = await fetch(urlDolar);
        const datosIndicadores = await solicitudIndicadores.json();
        const valorDolar = datosIndicadores.dolar.valor;

        const solicitudAutos = await fetch(urlAutos);
        const autos = await solicitudAutos.json();
        for (const auto of autos) {
            const nuevoAuto = plantilla.cloneNode(true);
            nuevoAuto.querySelector('.nombre').innerText = auto.marca+' '+auto.modelo;
            nuevoAuto.querySelector('.año').innerText = auto.año ?? 'Desconocido';
            nuevoAuto.querySelector('.precio').innerText = '$'+auto.precio.toLocaleString('es-CL') +' / $USD '+Math.round(auto.precio/valorDolar);
            nuevoAuto.querySelector('.tiempo').innerText = tiempoDiferencia(auto.fecha);

            cargarImagen(auto,nuevoAuto);

            nuevoAuto.addEventListener('click',()=> agregarCarrito(auto));

            contenedorAutos.append(nuevoAuto);
        }
    } catch (error) {
        console.log(error);
    }
    
}


async function cargarImagen(auto,elemento){
    try {
        const solicitudDetallada = await fetch(urlAutos+'?id='+auto.id);
        const datos = await solicitudDetallada.json();
        elemento.querySelector('.imagen').setAttribute('src',datos.image)
        return true;
    } catch (error) {
        return false;
    }
}

function agregarCarrito(auto){
    const autoEncontrado = autosEnCarrito.find(i => auto.id == i.id);
    if(!autoEncontrado){
        autosEnCarrito.push(auto);
        guardarCarrito();
        alert('Auto agregado!');
    }
    
}

function guardarCarrito(){
    localStorage.setItem('carrito',JSON.stringify(autosEnCarrito));
}

function cargarCarrito(){
    try {
        const autos = localStorage.getItem('carrito');
        if(autos){
            autosEnCarrito = JSON.parse(autos);
            console.log(autosEnCarrito);
        }
    } catch (error) {
        alert(error);
    }
}

function tiempoDiferencia(fecha){
    const fechaObj = new Date(fecha).getTime()/1000;
    const fechaActual = new Date().getTime()/1000;
    const dif = fechaActual - fechaObj;
    const horas = Math.round(dif/3600);
    return 'Hace '+horas+' horas';
}