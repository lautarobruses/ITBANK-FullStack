import { configureStore } from '@reduxjs/toolkit'
import menuReducer from './menuReducer'

const store = configureStore({
    reducer: {
        buttonMenu: menuReducer
    }
})

export default store