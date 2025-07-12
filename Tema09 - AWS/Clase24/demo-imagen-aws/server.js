import 'dotenv/config';
import { S3Client, PutObjectCommand, DeleteObjectCommand } from "@aws-sdk/client-s3";
import express from "express";
import multer from "multer";

const upload = multer();
const app = express();
const PORT = 3000;

const s3Client = new S3Client({
    region: process.env.AWS_REGION,
    credentials: {
        accessKeyId: process.env.AWS_ACCESS_KEY_ID,
        secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY
    }
});

app.get("/", (req, res) => res.json(res.send("Demo AWS")));

app.post("/upload", upload.single('archivo'), async(req, res)=>{
    try {
        if(!req.file){
            return res.status(400).json({error:"No se ha seleccionado ningún archivo."});
        }
        const uploadParams = {
            Bucket: process.env.S3_BUCKET_NAME,
            Key: req.file.originalname,
            Body: req.file.buffer,
            ContentType: req.file.mimetype,
            ContentLength: req.file.size
        }

        const command = new PutObjectCommand(uploadParams);
        const result = await s3Client.send(command);

        res.json({
            success: true,
            message: "Archivo subido exitosamente",
            result
        });
    } catch (error) {
        console.log("Error al subir archivo a S3", error);
        res.json({
             success: false,
            message: "Error al subir archivo a S3",
        });
    }
});

app.delete("/delete/:key", async (req, res) => {
    const { key } = req.params;
    const deleteParams = {
        Bucket: process.env.S3_BUCKET_NAME,
        Key: key
    }

    try {
        const command = new DeleteObjectCommand(deleteParams);
        const result = await s3Client.send(command);

        res.json({
            success: true,
            message: "Archivo eliminado exitosamente",
            result
        });
    } catch (error) {
        console.log("Error al eliminar archivo en S3", error);
        res.json({
            success: false,
            message: "Error al eliminar archivo en S3",
        });
    }
});

app.listen(PORT, ()=>{ console.log(`Servidor iniciado en el puerto ${PORT}`); })