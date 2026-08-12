// //Processo assíncrono
// setTimeout(() => {
//     console.log('Processo Assíncrono')
// }, 2000);

// //Processo síncrono
// console.log('1 - Inicio do processo');
// //Processo assíncrono
// setTimeout(() => {
//     console.log('2 - Meio do processo');
// },1000);
// console.log('3 - Fim do processo');

// const btn = document.getElementById('botao');
// const popup = document.getElementById('popup');

// btn.addEventListener('click', () => {
//     popup.classList.add('popup-active');

//     setTimeout(() => {
//         popup.classList.remove('popup-active')
//     }, 2000)
// })

// // setInterval(() => {
// //     console.log('Tic')
// // }, 1000)

// let counter = 0;
// const interval = setInterval(() => {
//     counter++
//     console.log('Counter: ', counter)

//     if (counter >= 5){
//         clearInterval(interval)
//         console.log('O intervalo foi removido')
//     }
// }, 1000);

const eventoFuturo = (res) => {
    return new Promise((resolve, reject) =>{
        // corpo da promessa
        // if(res === true){
        //     resolve('promessa resolvida')
        // }else{
        //     reject('promessa rejeitada')
        // }
        setTimeout(() =>{
        res ? resolve('promessa resolvida') : reject('promessa rejeitada')}, 2000)
    })
};
eventoFuturo(true).then((response) => {
    console.log(response)
});
eventoFuturo(false).catch((error) =>{
    console.log(error)
});