import axios from 'axios'

const STORAGE_KEY = 'loggedUser'

const baseUrl = 'http://localhost:8000/usuario/self/cliente/'

const setUser = (user) => {
    window.localStorage.setItem(STORAGE_KEY, JSON.stringify(user))
}

const getUser = () => {
    const loggedUserJSON = window.localStorage.getItem(STORAGE_KEY)
    return loggedUserJSON
}

const clearUser = () => {
    window.localStorage.clear()
    axios.defaults.auth = null;
}

const getInfo = async () => {
    const response = await axios.get(baseUrl)
        .catch(error => {
            return error.response.data.error
        });

    return response.data
}

const userServices = {
    setUser,
    getUser,
    clearUser,
    getInfo,
}

export default userServices