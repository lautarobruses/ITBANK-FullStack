import { styled } from 'styled-components'

import HeaderForm from './HeaderForm'
import RegisterForm from './RegisterForm'

const StyledBackgroundCustom = styled.div`

    @media screen and (max-width: 1023px) {
        #background-container {
            height: 150%;
        }
    }

    @media screen and (max-width: 640px) {
        #background-container {
            height: 139%;
        }
    }
`

const StyledRegister = styled.div`

    /* Estilos personalizados para el Header*/
    header{
        height: 84px;
        width: auto;
    }
    
    header img{
        height: 60px;
        width: auto;
    }
`

export default function Register() {

    return (
        <StyledBackgroundCustom>
            <div id='background-container'>
                <StyledRegister>
                    <HeaderForm/>
                    <RegisterForm/>
                </StyledRegister>
            </div>
        </StyledBackgroundCustom>
    )
}