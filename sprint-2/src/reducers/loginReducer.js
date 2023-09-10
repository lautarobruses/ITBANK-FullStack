
const loginReducer = (state = null, action) => {
    switch(action.type) {
    case 'INITIALIZE_LOGED': {
        //PENDIENTE
        // const usersFromStorage = await userService.getUser()
        const usersFromStorage = null
        return usersFromStorage
    }
    case 'LOGIN_USER': {
        console.log(action)
        const logedUser = null
        return logedUser
        //Meter parte Backend
    }
    case 'LOGOUT_USER': {
        return null
        //Meter parte Backend
    }
    default:
        return state
    }
}

export const initializeLoged = () => {
    return {
        type: 'INITIALIZE_LOGED',
        payload: {}
    }
}

export const loginUser = (username, password ) => {
    return {
        type: 'LOGIN_USER',
        payload: {
            username: username,
            password: password
        }
    }
}

export const logoutUser = () => {
    return {
        type: 'LOGOUT_USER',
        payload: {}
    }
}

export default loginReducer

