
var pokamios = [

];

const CLAVE_POKAMIOS = 'pokamios'

$(document).ready(()=>{
    
    try {
        const pokamiosGuardados = localStorage.getItem(CLAVE_POKAMIOS);
    
        if(pokamiosGuardados){
            pokamios = JSON.parse(pokamiosGuardados);
            if(pokamios.length < 1){
                throw 'No hay pokamios guardados!';
            }
        }else{
            alert('No hay pokamios');
        }  
    } catch (error) {
        if(error.constructor.name === 'SyntaxError'){
            alert('Hay un error de sintaxis');
        }else{
            alert('Otro error:'+error);
        }
        
    }
    
    

    cargarPokamios();
    
});

function cargarPokamios(){
    const contenedor = $('#lista');
    contenedor.html('');
    pokamios.forEach((e) => {

        /* Modo vanilla JS
            const div = document.createElement('div');
            const nombreP = document.createElement('p');
            nombreP.innerText = e.nombre;
            div.appendChild(nombreP);
            contenedor.append(div);
        */

        //Usando JQuery
        const element = $('<div class="pokamio"><img class="sprite"><p class="nombre"></p><button class="btn btn-warning">❌</button></div>');
        $(element).children('.nombre').text(e.nombre);
        $(element).children('.sprite').attr('src',obtenerUrlImagen(e.id));
        $(element).children('.btn').on('click',()=>{
            const nuevosPokamios = pokamios.filter((p)=>{
                if(p.id != e.id){
                    return true;
                }
                return false;
            });
            console.log(nuevosPokamios);
            pokamios = nuevosPokamios;
            guardarPokamios();
            cargarPokamios();
        });
        element.hide();
        contenedor.append(element);
        element.show(500);

    });
}

function obtenerUrlImagen(numero){
    const imagesUrl = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/showdown/'
    return imagesUrl+numero+'.gif';
}

function agregar(){
    const numero = $('#input-numero').val();
    const nombre = $('#input-nombre').val();

    if(numero && nombre){
        const nuevo = {
            id:numero,
            nombre:nombre
        };
        pokamios.push(nuevo);
        guardarPokamios()
        cargarPokamios();

    }
}

function guardarPokamios(){
    const serializado = JSON.stringify(pokamios);
    localStorage.setItem(CLAVE_POKAMIOS,serializado);
}