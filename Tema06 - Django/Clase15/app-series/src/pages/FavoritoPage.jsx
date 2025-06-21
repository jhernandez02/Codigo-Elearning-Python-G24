import { useState, useEffect } from "react";
import { listarFavoritoService, eliminarFavoritoService } from "../services/FavoritoService";
import Spinner from "react-bootstrap/Spinner";
import Card from "react-bootstrap/Card";
import Swal from "sweetalert2";

function FavofitoPage(){
    const [lista, setLista] = useState([]);
    const [cargando, setCargando] = useState(true);
    
    const listarFavoritos = async () => {
        const res = await listarFavoritoService();
        setLista(res.data);
        setCargando(false);
    }
    
    useEffect(()=>{
        listarFavoritos();
    }, []);

    const eliminarFavorito = async (id) => {
        const res = await eliminarFavoritoService(id);
        setCargando(true);
        listarFavoritos();
        Swal.fire({
            title: "Eliminado!",
            text: "La serie ha sido eliminada de tus favoritos",
            icon: "success",
            confirmButtonColor: "#6c757d",
            confirmButtonText: "Aceptar",
        });
    }

    const confirmarEliminarFavorito = (id) => {
        Swal.fire({
            title: "Esta seguro de eliminar?",
            text: "No podrás revertir esto esta acción!",
            icon: "warning",
            showCancelButton: true,
            confirmButtonColor: "#3085d6",
            cancelButtonColor: "#d33",
            confirmButtonText: "Sí, eliminar!",
            cancelButtonText: "Cancelar",
        }).then((result) => {
            if (result.isConfirmed) {
                eliminarFavorito(id);
            }
        });
    }

    return(
        <section className="container py-5">
            <h1>Favoritos</h1>
            {cargando ? (
                <p className="text-center">
                    <Spinner animation="border" variant="primary" />
                    <div>Cargando...</div>
                </p>
            ):(
                <div className="mt-4 row">
                    {lista.map(favorito=>(
                        <div key={favorito.id} className="col-md-3">
                            <Card className="mb-4 p-0">
                                <Card.Img variant="top" className="w-100" src="https://placehold.co/300x200" />
                                <Card.Body>
                                    <Card.Title>{favorito.nombre_serie}</Card.Title>
                                    <p>{favorito.nombre_categoria}</p>
                                    <button onClick={()=>confirmarEliminarFavorito(favorito.id)}  className="btn btn-danger w-100">
                                        <i className="bi bi-trash"></i> Eliminar
                                    </button>
                                </Card.Body>
                            </Card>
                        </div>
                    ))}
                </div>
            )}
        </section>
    );
}

export default FavofitoPage;