import { createSlice } from '@reduxjs/toolkit'

import tarjetaService from '@/services/tarjetas'

const tarjetaSlice = createSlice({
    name: 'tarjetas',
    initialState: [],
    reducers: {
        appendTarjeta(state, action) {
            state.push(action.payload)
        },
        setTarjetas(state, action) {
            const tarjetas = action.payload
            return tarjetas
        }
    },
})

export const initializeTarjetas = (id) => {
    return async dispatch => {
        const cuentas = await tarjetaService.getAll(id)
        dispatch(setTarjetas(cuentas))
    }
}

export const createTarjeta = (newTarjeta) => {
    return async dispatch => {
        const createdTarjeta = await tarjetaService.create(newTarjeta)
        dispatch(appendTarjeta(createdTarjeta))
    }
}

export const { appendTarjeta, setTarjetas } = tarjetaSlice.actions
export default tarjetaSlice.reducer