import { createSlice } from '@reduxjs/toolkit'

import userService from '../../services/user'

const userSlice = createSlice({
    name: 'user',
    initialState: null,
    reducers: {
        setInfo(state, action) {
            const byBlogsCreated = (b1, b2) => b2.blogs.length>b1.blogs.length ? 1 : -1
            const users = action.payload.sort(byBlogsCreated)
            return users
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