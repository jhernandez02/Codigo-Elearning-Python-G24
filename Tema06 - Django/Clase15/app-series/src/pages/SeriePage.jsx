import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { mostrarSerieService } from "../services/SerieService";
import { guardarFavoritoService } from "../services/FavoritoService";
import Spinner from "react-bootstrap/Spinner";
import Swal from "sweetalert2";

const initData = {
    id: 0,
    nombre: "",
    nombre_categoria: "",
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
        setSerie({
            id: datos.id,
            nombre: datos.nombre,
            nombre_categoria: datos.nombre_categoria,
            fecha_lanzamiento: datos.fecha_lanzamiento,
            puntaje: datos.puntaje,
            categoria: datos.categoria
        });
        setCargando(false);
    };
    
    useEffect(()=>{
        mostrarSerie();
    }, []);

    const agregarSerie = async (serieId) => {
        try {
            const res = await guardarFavoritoService({serie: serieId});
            Swal.fire({
                icon: "success",
                title: "Serie agregada",
                text: "La serie se agregó a tus favoritos!",
                confirmButtonColor: "#3085d6",
                confirmButtonText: "Aceptar"
            });
        } catch (error) {
            Swal.fire({
                icon: "error",
                title: "Oops...",
                text: "Ocurrió un error!",
            });
        }
        
    };

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
                        <p><strong>Fecha lanzamiento:</strong> {serie.fecha_lanzamiento}</p>
                        <p><strong>Rating:</strong> {serie.puntaje}</p>
                        <p><strong>Categoría:</strong> {serie.nombre_categoria}</p>
                        <button onClick={()=>agregarSerie(serie.id)} className="btn btn-success mt-2 fs-4 w-100">
                            <i className="bi bi-plus-circle"></i> Agregar a favoritos
                        </button>
                    </div>
                </div>
            )}
        </section>
    );
}

export default SeriePage;