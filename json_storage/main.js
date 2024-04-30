
const pokamios = [
    {
        id:25,
        nombre:'Pikachu'
    },
    {
        id:1,
        nombre:'Bulbasaur'
    },
    {
        id:6,
        nombre:'Charizard'
    },
    {
        id:151,
        nombre:'Mew'
    }
];


$(document).ready(()=>{
    cargarPokamios();
});

function cargarPokamios(){
    const contenedor = $('#lista');
    contenedor.html('');
    pokamios.forEach(e => {

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

}