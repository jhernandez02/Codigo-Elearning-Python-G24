const readline = require('readline/promises');
const {stdin: input, stdout: output } = require('process');

async function saludar(){
    const lector = readline.createInterface({input, output});
    const nombre = await lector.question('Cual es tu nombre? ');
    console.log(`Hola ${nombre}`);
    lector.close();
}

saludar();