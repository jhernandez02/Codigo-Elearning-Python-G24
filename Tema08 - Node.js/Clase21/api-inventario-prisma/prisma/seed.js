import { PrismaClient } from '../generated/prisma/client.js';
const prisma = new PrismaClient();

async function main() {
    const categorias = await prisma.categoria.createMany({
        data: [
            {nombre: "Electronica"},
            {nombre: "Ropa"},
            {nombre: "Alimentos"}
        ]
    });
    const productos = await prisma.producto.createMany({
        data: [
            {
                categoriaId: 1, 
                codigo: "ELEC0001",
                nombre: "Laptop Lenovo",
                precio: 1500.00,
                cantidad: 5,
                fecha_compra: new Date('2023-01-18')
            },
            {
                categoriaId: 2, 
                codigo: "ROPA0001",
                nombre: "Casaca de invierno",
                precio: 120.00,
                cantidad: 8,
                fecha_compra: new Date('2023-01-18')
            }
        ]
    });
}

main().then(()=>{
    console.log("Datos de prueba insertados correctamente");
}).catch((e)=>{
    console.log(e);
    process.exit(1);
}).finally(()=>{
    prisma.$disconnect();
});