import { configureStore } from '@reduxjs/toolkit'

import menuReducer from './reducers/menuReducer'
import loginReducer from './reducers/loginReducer'

const store = configureStore({
    reducer: {
        buttonMenu: menuReducer,
        loggedUser: loginReducer
    }
})

export default store