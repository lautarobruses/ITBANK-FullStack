import path from '../../assets/construccion-page.gif'

import { styled } from 'styled-components'

const StyledDiv = styled.div`
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
   
    img{
        border-radius: 32px;
    }
    h1{
        color: #98DAD9;
    }
`

const ComingSoon = () => {
    return (
        <StyledDiv>
            <h1>¡Página en construcción!</h1>
            <img src={path} alt="Hombre construyendo una pagina web" />
        </StyledDiv>
    )
}

export default ComingSoon