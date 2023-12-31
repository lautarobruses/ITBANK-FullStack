import { Link, useNavigate } from 'react-router-dom'

import TextBox from './TextBox'
import SubmitButton from './SubmitButton'
import InteractiveButton from './InteractiveButton'
import Checkbox from './Checkbox'
import { styled } from 'styled-components'
import StyledBackgroundForm from './styles/StyledBackgroundForm'

const StyledForm = styled.form `
    display: grid;
    align-items: center;
    justify-items: center;

    section {
        display: grid;
        gap: 24px;
        margin-bottom: 24px;
    }

    #send-form-container {
        margin-top:12px;
        grid-column: 1 / 3;

        display: flex;
        flex-direction: column;
        align-items: center;
    }

    #buttons-container{
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 24px;
    }

    /*Tamaño personalizado del textbox*/
    input { 
        width: 433px;
        height: 55px
    }

    /*Tamaño personalizado del boton*/

    .register {
        padding: 16px 60px;
    }

    @media screen and (max-width: 1023px) {
        grid-template-columns: 1fr;
        // grid-template-rows: 380px 380px 160px;

        section {
            display: grid;
        }

        #left-form-container{
            grid-row: 1;
        }
    
        #right-form-container{
            grid-row: 2;
        }

        /*Tamaño personalizado del textbox*/
        input{
            width: 500px;
            height: 60px;
        }
    }

    @media screen and (max-width: 640px) {
        // grid-template-rows: 370px 370px 160px;

        #interactive-button {
            font-size: 20px;
        }
    
        #interactive-button svg {
            width: 23px;
            height: auto;
        }

        /*Tamaño personalizado del textbox*/
        input{
            width: 300px;
            height: 48px;
        }

        .register {
            padding: 16px 60px;
        }
    }
`

export default function RegisterForm() {
    const navigate = useNavigate()

    const handleRegister  = (event) => {
        event.preventDefault()

        console.log(event)

        const username = event.target[0].value
        const password = event.target[1].value
        const dni = event.target[3].value
        const email = event.target[4].value
        const confirmPassword = event.target[5].value
        const phone = event.target[7].value

        const userRegister = { username, password, dni, email, confirmPassword, phone }

        window.localStorage.setItem( //Aca en un futuro se debera guardar en la base de datos
            'registedUser', JSON.stringify(userRegister)
        )

        navigate('/')
    }

    return (
        <StyledBackgroundForm>
            <StyledForm onSubmit={handleRegister}>
                <section id='left-form-container'>
                    <TextBox type='text' id='name'>Nombre y Apellido:</TextBox>
                    <TextBox type='password' id='password'>Contraseña:</TextBox>
                    <TextBox type='number' id='dni'>DNI:</TextBox>
                </section>
                <section id='right-form-container'>
                    <TextBox type='email' id='email'>Correo electronico:</TextBox>
                    <TextBox type='password' id='confirm-password'>Confirmar contraseña:</TextBox>
                    <TextBox type='number' id='phone'>Telefono:</TextBox>
                </section>
                <section id='send-form-container'>
                    <Checkbox>Acepto los <a href='#'>Términos y Condiciones</a></Checkbox>
                    <div id='buttons-container'>
                        <InteractiveButton>
                            <Link to="/login">
                                <svg xmlns="http://www.w3.org/2000/svg" id="Outline" stroke="currentColor" fill="currentColor" viewBox="0 0 24 24" width="1em" height="1em"><path d="M19,11H9l3.29-3.29a1,1,0,0,0,0-1.42,1,1,0,0,0-1.41,0l-4.29,4.3A2,2,0,0,0,6,12H6a2,2,0,0,0,.59,1.4l4.29,4.3a1,1,0,1,0,1.41-1.42L9,13H19a1,1,0,0,0,0-2Z"/></svg>
                                Atrás
                            </Link>
                        </InteractiveButton>
                        <SubmitButton className="register">Crear cuenta</SubmitButton>
                    </div>
                </section>
            </StyledForm>
        </StyledBackgroundForm>
    )
}