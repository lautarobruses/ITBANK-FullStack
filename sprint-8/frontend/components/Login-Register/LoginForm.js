import styles from '@/styles/Login/LoginForm.module.css'

import Link from 'next/link'

import { useRouter } from 'next/router'

import { useDispatch } from 'react-redux'

import { loginUser } from '@/store/reducers/loginReducer'

import TextBox from './TextBox'

const LoginForm =() => {
    const dispatch = useDispatch()
    const router = useRouter();

    const handleLogin  = (event) => {
        event.preventDefault()

        const username = event.target[0].value
        const password = event.target[1].value

        // ====== ELIMINAR:
        // const user = { username, password }

        // window.localStorage.setItem(
        //     'loggedUser', JSON.stringify(user)
        // )
        // =====

        dispatch(loginUser(username, password))
        .catch(() => {
            window.alert("Email o contraseña incorrecto!");
        })
        router.replace('/');
    }

    return (
        <div className={`${styles.formContainer}`}>
            <form className={`${styles.form}`} onSubmit={handleLogin}>
                <TextBox type='text' id='user'>Correo electronico:</TextBox>
                <div id='passwordContainer'>
                    <TextBox type='password' id='password'>Contraseña:</TextBox>
                    <br/>
                    <Link href='/coming-soon'>Olvide mi contraseña</Link>
                </div>
                <button 
                    type="submit"
                    id="login"
                    value="login"
                    className={`${styles.submitButton}`}
                >
                    Iniciar sesion
                </button>
            </form>
        </div>
    )
}

export default LoginForm