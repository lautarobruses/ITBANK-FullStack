import { createSlice } from '@reduxjs/toolkit'

import userService from '../../services/user'

const userSlice = createSlice({
    name: 'user',
    initialState: null,
    reducers: {
        setUserInfo(state, action) {
            const user = action.payload
            return user
        },
    },
})

export const initializeUserData = () => {
    return async dispatch => {
        const userInfo = await userService.getInfo()
        if (userInfo) {
            dispatch(setUserInfo(userInfo))
        }
    }
}

export const { setUserInfo } = userSlice.actions
export default userSlice.reducer