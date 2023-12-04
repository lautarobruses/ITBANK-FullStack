import axios from 'axios'

const baseUrl = 'http://localhost:8000/usuario/register/'

const register = async (info) => {
    const response = await axios.post(baseUrl, info)
    return response.data
}

const registerService = { register }

export default registerService