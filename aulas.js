function alturaArvoreUtopica(ciclos) {

    let tamanhoArvore = 1;
   
    for(let i = 0; i < ciclos; i++){
   
        if(i & 1){
            tamanhoArvore += 1;
        }else{
            tamanhoArvore *= 2;
        }
    }
    return tamanhoArvore;
   
   }
   