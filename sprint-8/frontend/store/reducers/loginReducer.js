import { createSlice } from '@reduxjs/toolkit'

const loginSlice = createSlice({
    name: 'login',
    initialState: null,
    reducers: {
        setUser(state, action) {
            return action.payload
        }
    },
})

export const initializeLoged = () => {
    return async dispatch => {
        const usersFromStorage = window.localStorage.getItem('loggedUser')
        if (usersFromStorage) {
            dispatch(setUser(usersFromStorage))
        }
    }
}

export const loginUser = (username, password ) => {
    return async dispatch => {
        const loggedUser = {
            username: username,
            password: password
        }
        dispatch(setUser(loggedUser))
    }
}

export const logoutUser = () => {
    return async dispatch => {
        dispatch(setUser(null))
        window.localStorage.clear()
    }
}

export const { setUser } = loginSlice.actions
export default loginSlice.reducer