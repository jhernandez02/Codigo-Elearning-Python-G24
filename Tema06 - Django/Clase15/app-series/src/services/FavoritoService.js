import { Api } from "../utils/Api";
import { API_URL } from "../utils/Config";

const URL = `${API_URL}/favoritos`;

export const listarFavoritoService = async () => {
    const res = await Api().get(URL);
    return res;
}

export const guardarFavoritoService = async (data) => {
    const res = await Api().post(`${URL}/crear/`, data);
    return res;
}

export const eliminarFavoritoService = async (id) => {
    const res = await Api().delete(`${URL}/${id}/eliminar/`);
    return res;
}