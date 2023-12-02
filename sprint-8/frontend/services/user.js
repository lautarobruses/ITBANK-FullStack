// import axios from 'axios'

const STORAGE_KEY = 'loggedUser'

const baseUrl = '/api/user/info'

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
    const response = await axios.get(baseUrl)
    return response.data
}

const userServices = {
    setUser,
    getUser,
    clearUser,
    getInfo,
}

export default userServices
