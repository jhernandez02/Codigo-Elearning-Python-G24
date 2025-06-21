import { Api } from "../utils/Api";
import { API_URL } from "../utils/Config";

const URL = `${API_URL}/series`;

export const listarSerieService = async () => {
    const res = await Api().get(URL);
    return res;
}

export const mostrarSerieService = async (id) => {
    const res = await Api().get(`${URL}/${id}`);
    return res;
}