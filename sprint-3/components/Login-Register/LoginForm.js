import styles from '@/styles/Login/LoginForm.module.css'

import Link from 'next/link'

import { useDispatch } from 'react-redux'

import TextBox from './TextBox'

import { loginUser } from '@/store/reducers/loginReducer'

const LoginForm =() => {
    const dispatch = useDispatch()

    const handleLogin  = (event) => {
        event.preventDefault()

        const username = event.target[0].value
        const password = event.target[1].value

        const user = { username, password }

        window.localStorage.setItem(
            'loggedUser', JSON.stringify(user)
        )

        dispatch(loginUser(username, password))
    }

    return (
        <div className={`${styles.formContainer}`}>
            <form className={`${styles.form}`} onSubmit={handleLogin}>
                <TextBox type='text' id='user'>Correo electronico o usuario:</TextBox>
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