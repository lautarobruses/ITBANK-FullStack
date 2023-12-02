import axios from 'axios'

const STORAGE_KEY = 'loggedUser'

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

const userServices = {
    setUser,
    getUser,
    clearUser,
}

export default userServices
