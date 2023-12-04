import styles from '@/styles/Login/RegisterForm.module.css'

import { useRouter } from 'next/router'
import Link from 'next/link'

import TextBox from '@/components/Login-Register/TextBox'
import Checkbox from '@/components/Login-Register/Checkbox'

import registerService from '@/services/register'

import ArrowIcon from '@/public/svg/arrow.svg'

const RegisterForm = () => {
    const router = useRouter();

    const handleRegister  = (event) => {
        event.preventDefault()

        const name_surname = event.target[0].value
        const password = event.target[1].value
        const dni = event.target[3].value
        const mail = event.target[4].value
        const confirm_password = event.target[5].value
        const phone = event.target[7].value

        const userRegister = { name_surname, password, dni, mail, confirm_password, phone }
            registerService.register(userRegister)
                .then((response) => {
                    console.log(response);
                    router.replace('/cuenta/login');
                })
                .catch((error) => {
                    window.alert(`${error.response.data.error} Vuelva a intentarlo nuevamente.`);
                });  
    }

    return (
        <div className={`${styles.container}`}>
            <form className={`${styles.form}`} onSubmit={handleRegister}>
                <section className={`${styles.rightFormContainer}`}>
                    <TextBox type='text' id='name'>Nombre y Apellido:</TextBox>
                    <TextBox type='password' id='password'>Contraseña:</TextBox>
                    <TextBox type='number' id='dni'>DNI:</TextBox>
                </section>
                <section className={`${styles.leftFormContainer}`}>
                    <TextBox type='email' id='email'>Correo electronico:</TextBox>
                    <TextBox type='password' id='confirm-password'>Confirmar contraseña:</TextBox>
                    <TextBox type='number' id='phone'>Telefono:</TextBox>
                </section>
                <section className={`${styles.sendFormContainer}`}>
                    <Checkbox>Acepto los <Link href="/coming-soon">Términos y Condiciones</Link></Checkbox>
                    <div className={`${styles.buttonsContainer}`}>
                        <button
                            className={`${styles.interactiveButton}`}
                            type="button"
                            value="Volver"
                        >
                            <Link href="/cuenta/login">
                                <ArrowIcon />
                                Atrás
                            </Link>
                        </button>
                        <button
                            className={`${styles.submitButton}`}
                            type='submit'
                            id='submit'
                            value='submit'
                        >
                            Crear cuenta
                        </button>
                    </div>
                </section>
            </form>
        </div>
    )
}

export default RegisterForm