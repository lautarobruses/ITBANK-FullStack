import axios from 'axios'

import { useSelector } from 'react-redux'

const STORAGE_KEY = 'loggedUser'

const baseUrl = 'http://localhost:8000/usuario/self/'

const userInfo = useSelector((state) => state.user)

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
    const { username, password } = getUser()
    console.log(username);
    console.log(password);
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
            // Maneja el error
            console.error(error);
        });
}

const userServices = {
    setUser,
    getUser,
    clearUser,
    getInfo,
}

export default userServices