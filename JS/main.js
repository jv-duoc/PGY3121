console.log('Hola mundo!');

//asignacion
var nombre = 'Jorge';
let nombreLet = 'Jorge';
const nombreConst = 'JorgeConst';


//valor
let numero = 1;

let numero2 = numero;
numero2 +=10;
console.log(numero,numero2);

//referencia
let obj1 = {nombre:'duoc'};
let obj2 = obj1;
obj2.nombre = 'No soy duoc'
console.log(obj1,obj2)

hacerAlgo('Hola!')

let array = [1,5,3,4];

for (const i of array) {
    console.log(i)
}

console.log(hacerAlgo('Pruaba'));

//func
function hacerAlgo(parametro){
    console.log('Hago algo con el parametro',parametro);
    return parametro+', wena!';
}

let func = (parametro) =>{
    console.log('Fn anonima:',parametro);
}

func('Hola');