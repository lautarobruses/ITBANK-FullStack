import axios from 'axios'

const baseUrl = '/api/cuentas'

const getAll = async () => {
    const response = await axios.get(baseUrl)
    return response.data
}

const create = async (newAccount) => {
    const response = await axios.post(baseUrl, newAccount)
    return response.data
}

const update = async (id, newAccount) => {
    const response = await axios.put(`${baseUrl}/${id}`, newAccount)
    return response.data
}

const remove = (id) => {
    return axios.delete(`${baseUrl}/${id}`)
}

const cuentaService = { getAll, create, update, remove }

export default cuentaService