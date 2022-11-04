#  *
#  * Reto #20
#  * PARANDO EL TIEMPO
#  * Fecha publicación enunciado: 16/05/22
#  * Fecha publicación resolución: 23/05/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Crea una función que sume 2 números y retorne su resultado pasados unos segundos.
#  * - Recibirá por parámetros los 2 números a sumar y los segundos que debe tardar en finalizar su ejecución.
#  * - Si el lenguaje lo soporta, deberá retornar el resultado de forma asíncrona, es decir, sin detener la ejecución del programa principal. Se podría ejecutar varias veces al mismo tiempo.
#  *
#  *

import asyncio
import time


async def slep(delay, sec):
    for s in range(sec):
        await asyncio.sleep(delay)
        print(f"Waiting {str(s)} seconds...");
    
    

async def asyncSum(num1:int, num2:int, seconds:int):
    task1 = asyncio.create_task(slep(1,seconds))
   
    print(f"started at {time.strftime('%X')}");
    print("");       
    await task1;
    print("");
    print(f"finished at {time.strftime('%X')}");
    print(f"Resultado = {str(num1+num2)}");
    

asyncio.run(asyncSum(5,10,5));




# function sleep(ms) {
#     return new Promise(resolve => setTimeout(resolve, ms));
# }

# const asyncSum = async(n1, n2, seconds) =>{

#     // Usage!
#    for (let i = 1; i <= seconds; i++) {

#        await sleep(1000);
#        console.log(`Waiting ${i} seconds...`);

#     }
#             console.log('Done');
#             console.log(`Resultado = ${n1+n2}`);

# }


# asyncSum(10,5,5);