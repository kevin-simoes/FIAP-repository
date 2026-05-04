var nome = "Lucas";

function obterNome() {
  var nome = "Jonas";
  console.log(this.nome); //Lucas
}

obterNome();
console.log(this.none); //Lucas

var nome = "Lucas";

function obterNome() {
  this.nome = "Jonas";
  console.log(this.nome); // Jonas
}
new obterNome();
console.log(this.nome); //Lucas

//Laço de repetição for
for (let i = 0; i < 10; i++) {
  console.log(i);
}

// Solicitamos o valor ao usuário
let numero = parseInt(prompt("Inserir um número"));

// A Cada repetição, calculamos o número inserido vezes o número da repetição (i)
for (let i = 1; i <= 10; i++) {
  let resultado = numero * i;
  console.log(numero + "X" + i + "=" + resultado);
}

for (let i = 1; i <= 5; i++) {
    //Se a varíavel i for iual à 3
    if(i == 3){
        break;
    }
    console.log(i);
}

let entrada = prompt("Inserir um dado");
//Repetimos com while até que o usuário digite

while (entrada != "sair"){
    alert("O usuário inseriu"+entrada);
    //Solicitamos novamente um dado
    //Na próxima interação, será verificado
    entrada = prompt("Inserir outro dado");
}

let numer = 0;
do {
    //repetimos com do... while enquanto o usuário
    numer = prompt("Inserir um número");
    console.log(numer);
} while (!parseInt(numer))



let entrad = promt("Inserir um nome");
//Repetimos até que "sair" seja inserido.
while (entrad != "sair") {
    switch (entrad) {
        case "ANA":
            alert("OlÁ, ANA");
            break;
        case "JOÃO":
            alert("OLÁ, JOÃO");
            break;
        default:
            alert("QUEM É VOCÊ?")
            beak;
    }
    entrada = prompt("Inserir um nome");
}

