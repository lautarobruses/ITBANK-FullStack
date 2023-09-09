import TextBox from './TextBox'
import SubmitButton from './SubmitButton'
import InteractiveButton from './InteractiveButton'
import Checkbox from './Checkbox'
import { styled } from 'styled-components'
import StyledBackgroundForm from './styles/StyledBackgroundForm'

const StyledForm = styled.form `
    width: 1000px;
    height: 560px;

    display: grid;
    grid-template-columns: 50% 50% ;
    grid-template-rows: 74% 26%;
    align-items: center;
    justify-items: center;

    section {
        display: grid;
        gap: 32px;
    }

    #send-form-container{
        grid-column: 1 / span2;

        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 32px;
    }

    #buttons-container{
        display: flex;
        align-items: center;
        gap: 24px;
    }

    /*Tamaño personalizado del textbox*/
    input{ 
        width: 433px;
        height: 55px
    }

    /*Tamaño personalizado del boton*/

    #register{
        padding: 16px 60px;
    }

    @media screen and (max-width: 1023px) {
        width: 600px;
        height: 1000px;

        grid-template-columns: 1fr;
        grid-template-rows: 420px 420px 160px;

        #left-form-container{
            padding-top: 25px;
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
        width: 360px;
        height: 890px;

        grid-template-rows: 370px 370px 160px;

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
    }
`

export default function RegisterForm() {
    return (
        <StyledBackgroundForm >
            <StyledForm>
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
                        <InteractiveButton><svg xmlns="http://www.w3.org/2000/svg" id="Outline" stroke="currentColor" fill="currentColor" viewBox="0 0 24 24" width="1em" height="1em"><path d="M19,11H9l3.29-3.29a1,1,0,0,0,0-1.42,1,1,0,0,0-1.41,0l-4.29,4.3A2,2,0,0,0,6,12H6a2,2,0,0,0,.59,1.4l4.29,4.3a1,1,0,1,0,1.41-1.42L9,13H19a1,1,0,0,0,0-2Z"/></svg>Atrás</InteractiveButton>
                        <SubmitButton id="register">Crear cuenta</SubmitButton>
                    </div>
                </section>
            </StyledForm>
        </StyledBackgroundForm>
    )
}