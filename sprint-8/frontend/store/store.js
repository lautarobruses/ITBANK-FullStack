import { configureStore } from '@reduxjs/toolkit'

import loginReducer from './reducers/loginReducer'
import userReducer from './reducers/userReducer'
import cuentasReducer from './reducers/cuentasReducer'
import tarjetasReducer from './reducers/tarjetasReducer'

const store = configureStore({
    reducer: {
        loggedUser: loginReducer,
        user: userReducer,
        cuentas: cuentasReducer,
        tarjetas: tarjetasReducer,
    }
})

export default store