$(document).ready(jqueryCargado);

function jqueryCargado(){

    const mascotas =[
        'Perro',
        'Gato',
        'Hamster',
        'Delfin'
    ];

    const principal = $('#principal');

    principal.css('background','red');
    principal.css('width','100vw')
    principal.css('height','100vh');
    principal.css('color','white');

    const encabezado = $('<h1></h1>');
    encabezado.text('Bienvenido via Jquery');

    principal.append(encabezado);

    const parrafo = $('<p></p>');
    parrafo.text('loremadsanmdjksdasjk adkja skasjd dksasdjkads skd adsjkads ');
    parrafo.hide();
    principal.append(parrafo);
    parrafo.show(2000);

    for (const i of mascotas) {
        const nuevaMascota = $('<div><p>🐕</p><p class="mascota"></p></div>');
        const parrafo = nuevaMascota.children('.mascota').first();
        parrafo.text(i);
        principal.append(nuevaMascota);
    }
}