import { createSlice } from '@reduxjs/toolkit'

import cuentaService from '@/services/cuentas'

const cuentaSlice = createSlice({
    name: 'cuentas',
    initialState: [],
    reducers: {
        appendCuenta(state, action) {
            state.push(action.payload)
        },
        setCuentas(state, action) {
            const cuentas = action.payload
            return cuentas
        }
    },
})

export const initializeCuentas = (id) => {
    return async dispatch => {
        const cuentas = await cuentaService.getAll(id)
        dispatch(setCuentas(cuentas))
    }
}

export const createCuenta = (newCuenta) => {
    return async dispatch => {
        const createdCuenta = await cuentaService.create(newCuenta)
        dispatch(appendCuenta(createdCuenta))
    }
}

export const { appendCuenta, setCuentas } = cuentaSlice.actions
export default cuentaSlice.reducer