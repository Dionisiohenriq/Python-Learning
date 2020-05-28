function escada(altura){
    let arrayEscada = [];

    for(let i = 0; i <= altura; i++){
        arrayEscada[i] = "#".repeat(i);
    }

    return arrayEscada;
    
}

console.log(escada(5))