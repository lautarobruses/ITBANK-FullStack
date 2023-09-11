const menuReducer = (state = false, action) => {
    switch(action.type) {
    case 'TOGGLE_VISIBILITY': {
        return !state
    }
    default:
        return state
    }
}

export const toggleVisibility = () => {
    return {
        type: 'TOGGLE_VISIBILITY',
        payload: {}
    }
}

export default menuReducer

