// let num = 5;

// if (num == 5) {
//   console.log("Variável é igual à cinco");
// }
// if (num == 6) {
//   console.log("A variável não tem esse valor");
// }

// let umaCor = prompt('Digite uma cor:')

// if (umaCor == "vermelho"){
//     alert('A cor é vermelho')
// }
// else {
//     alert('A cor não é vermelho')
// }
// let = veri = false;

// do {
//   let nomeUsuario = prompt("Digite seu nome");

//   if (nomeUsuario == "" || nomeUsuario == null) {
//     alert("Nome não inserido");
//   } else {
//     alert(`Nome inserido: ${nomeUsuario}`);
//   }
// } while (veri == false);

// let combustivel = prompt('Digite o tipo de combustível');

// if (combustivel == 'gnv'){
//     alert('O veículo se move à gás');
// }
// else if(combustivel == 'gasolina'){
//     alert('O veículo se move à alcool')
// }else {
//     alert('O veículo só pode ser elétrico')
// }

// let numero = prompt('Digite um número')

// if (numero == 1){
//     alert("UM")
// }else if(numero == 2){
//     alert("DOIS")
// }else if(numero == 3){
//     alert("TRÊS")
// }else if(numero == 4){
//     alert("QUATRO")
// }else if(numero == 5){
//     alert("CINCO")
// } else {
//     alert("Ou vc digitou um número além de 1 a 5, ou você digitou texto")
// }

let numInserido = parseInt(prompt('Digite um número entre 1 e 20'))

if (numInserido <= 10){
    alert(`O número inserido: ${numInserido} está entre 1 a 10`)
}else if (numInserido <= 20){
    alert(`O número inserido: ${numInserido} está entre 11 a 20`)
}
else {
    alert(`O número inserido: ${numInserido} é maior que 20`)
}