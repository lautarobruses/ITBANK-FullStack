import { createSlice } from '@reduxjs/toolkit'

import userService from '../../services/user'

const userSlice = createSlice({
    name: 'user',
    initialState: null,
    reducers: {
        setInfo(state, action) {
            const user = action.payload
            return user
        },
    },
})

export const initializeUser = () => {
    return async dispatch => {
        const userInfo = await userService.getInfo()
        if (userInfo) {
            dispatch(setInfo(userInfo))
        }
    }
}

export const { setInfo } = userSlice.actions
export default userSlice.reducer