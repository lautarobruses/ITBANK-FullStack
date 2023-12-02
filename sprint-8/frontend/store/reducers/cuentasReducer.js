import { createSlice } from '@reduxjs/toolkit'

import cuentaService from '@/services/cuentas'

const cuentaSlice = createSlice({
    name: 'cuentas',
    initialState: [],
    reducers: {
        appendCuenta(state, action) {
            state.push(action.payload)
        },
        deleteCuenta(state, action) {
            const byLikes = (b1, b2) => b2.likes>b1.likes ? 1 : -1
            const removedBlog = action.payload
            const blogs = state.filter((b) => b.id !== removedBlog.id).sort(byLikes)
            return blogs
        },
        setCuentas(state, action) {
            const cuentas = action.payload
            return cuentas
        }
    },
})

export const initializeCuentas = () => {
    return async dispatch => {
        const cuentas = await cuentaService.getAll()
        dispatch(setCuentas(cuentas))
    }
}

export const createCuenta = (newCuenta) => {
    return async dispatch => {
        const createdBlog = await cuentaService.create(newCuenta)
        dispatch(appendCuenta(createdBlog))
    }
}

export const removeCuenta = (cuenta) => {
    return dispatch => {
        cuentaService
            .remove(cuenta.id)
            .then(() =>
                dispatch(deleteCuenta(cuenta))
            )
    }
}

export const { appendCuenta, deleteCuenta, setCuentas } = cuentaSlice.actions
export default cuentaSlice.reducer