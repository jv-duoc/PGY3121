
//main
escribir('Hola');
setTimeout(()=>{
    escribir('Hola desde handler ')
},1000);
escribir('Esto saldra primero que handler');

const myPromise = new Promise((exito, error) => {
    //operaciones
    let valorDeAlgo = 100;
    valorDeAlgo+=Math.random();

    if(valorDeAlgo > 100.5){
        error('Errors');
    }else{
        setTimeout(() => {
            exito({valor:valorDeAlgo,nombre:'Resultado de random'});
          }, 2000);
    }
    

    
  });

myPromise.then( (resultado) => {
    escribir(resultado.nombre+':'+resultado.valor);
}, (error) => {
    escribir('Error en la promesa:'+error);
});


var otraPromesa = new Promise((exito,error)=>{
    error();

    setTimeout(() => {
        exito('Promesa exitosa async!');
      }, 3500);
})

ejecutarTareasAsync();
camara();


async function ejecutarTareasAsync(){
    try {
        const saludoDePromesa = await otraPromesa;
        escribir(saludoDePromesa);
    } catch (error) {
        escribir('Error en await')
    }
    
}

async function camara(){
    const camara = await navigator.mediaDevices.getUserMedia({video: true})
    const contenedor = document.getElementById('contenedor');
    const video = document.createElement('video');
    video.srcObject = camara;
    contenedor.appendChild(video);
    video.play();
}

//funciones


function escribir(texto){
    const consola = document.querySelector('#consola-impostor');
    const nuevoP = document.createElement('p');
    nuevoP.classList.add('linea-consola');
    nuevoP.innerText = texto;

    consola.appendChild(nuevoP);
}

function limpiarConsola(){
    const consola = document.querySelector('#consola-impostor');
    consola.innerHTML = '';
}
