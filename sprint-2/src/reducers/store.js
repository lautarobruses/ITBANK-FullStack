import { configureStore } from '@reduxjs/toolkit'

import menuReducer from './menuReducer'
import loginReducer from './loginReducer'

const store = configureStore({
    reducer: {
        buttonMenu: menuReducer,
        loggedUser: loginReducer
    }
})

export default store