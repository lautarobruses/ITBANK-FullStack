import axios from 'axios'

import { useSelector } from 'react-redux'

const STORAGE_KEY = 'loggedUser'

const baseUrl = 'http://localhost:8000/usuario/self/'

const setUser = (user) => {
    window.localStorage.setItem(STORAGE_KEY, JSON.stringify(user))
}

const getUser = () => {
    const loggedUserJSON = window.localStorage.getItem(STORAGE_KEY)
    return loggedUserJSON
}

const clearUser = () => {
    window.localStorage.clear()
}

const getInfo = async () => {
    const { username, password } = window.localStorage.getItem(STORAGE_KEY)

    return await axios.get(baseUrl, {
        auth: {
            username: username,
            password: password
        }
    })
        .then(response => {
            console.log(response.data);
        })
        .catch(error => {
            return error.data.error.message
        });
}

const userServices = {
    setUser,
    getUser,
    clearUser,
    getInfo,
}

export default userServices