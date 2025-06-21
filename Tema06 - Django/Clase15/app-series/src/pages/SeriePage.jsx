import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { mostrarSerieService } from "../services/SerieService";
import Spinner from "react-bootstrap/Spinner";

const initData = {
    id: 0,
    nombre: "",
    fecha_lanzamiento: "",
    puntaje: 0,
    categoria: 0
}

function SeriePage(){
    const { id } = useParams();
    const [serie, setSerie] = useState(initData);
    const [cargando, setCargando] = useState(true);
    const mostrarSerie = async () => {
        const res = await mostrarSerieService(id);
        const datos = res.data;
        console.log(datos);
        setSerie({
            id: datos.id,
            nombre: datos.nombre,
            fecha_lanzamiento: datos.fecha_lanzamiento,
            puntaje: datos.puntaje,
            categoria: datos.categoria
        });
        setCargando(false);
    }
    
    useEffect(()=>{
        mostrarSerie();
    }, []);

    return(
        <section className="container py-5">
            {cargando ? (
                <p className="text-center">
                    <Spinner animation="border" variant="primary" />
                    <div>Cargando...</div>
                </p>
            ):(
                <div className="row">
                    <div className="col-md-6">
                        <img src="https://placehold.co/600x400" className="w-100" alt="imagen" />
                    </div>
                    <div className="col-md-6">
                        <h2>{serie.nombre}</h2>
                        <p>Fecha lanzamiento: {serie.fecha_lanzamiento}</p>
                        <p>Rating: {serie.puntaje}</p>
                        <p>Categoría: {serie.categoria}</p>
                        <button className="btn btn-primary mt-2 fs-4 w-100">Agregar a favoritos</button>
                    </div>
                </div>
            )}
        </section>
    );
}

export default SeriePage;