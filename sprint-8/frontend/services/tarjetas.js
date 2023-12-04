import axios from 'axios'

const baseUrl = 'http://localhost:8000/cuenta/api'

const getAll = async (id) => {
    const response = await axios.get(`${baseUrl}/tarjetas/${id}`);
    return [response.data]
}

const create = async (newTarjeta) => {
    const response = await axios.post(baseUrl, newTarjeta)
    return response.data
}

const update = async (id, newTarjeta) => {
    const response = await axios.put(`${baseUrl}/${id}`, newTarjeta)
    return response.data
}

const remove = (id) => {
    return axios.delete(`${baseUrl}/${id}`)
}

const tarjetaService = { getAll, create, update, remove }

export default tarjetaService