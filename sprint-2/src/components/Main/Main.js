import {
    Outlet
} from 'react-router-dom'

import { styled } from 'styled-components'

const StyledMain = styled.main`
    margin-top: 100px;
    margin-left: 384px;
    min-height: 90vh;

    display: flex;
    align-items: center;
    justify-content: center;

    @media screen and (max-width: 1023px) {
        margin-left: 284px;
    }

    @media screen and (max-width: 640px) {
        margin-top: 80px;;
        margin-left: 0px;
        min-height: 90vh;
    }
`

const Main = () => {
    return (
        <StyledMain>
            <Outlet/>
        </StyledMain>
    )
}

export default Main