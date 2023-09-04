import {
    Routes, Route
} from 'react-router-dom'

import { styled } from 'styled-components'

const StyledMain = styled.main`
    margin-top: 100px;
    margin-left: 384px;
    min-height: 100vh;

    @media screen and (max-width: 1023px) {
        margin-left: 284px;
    }
`

const Main = () => {
    return (
        <StyledMain>
            <Routes>
                {/* DENTRO DE ELEMENT VA EL COMPONENTE CORRESPONDIENTE A CADA RUTA */}
                <Route path="/" element={null} />
                <Route path="/cuenta" element={null} />
                <Route path="/transferencias" element={null} />
                <Route path="/pagos" element={null} />
                <Route path="/prestamos" element={null} />
            </Routes>
        </StyledMain>
    )
}

export default Main