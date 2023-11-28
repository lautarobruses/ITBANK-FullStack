import { useState } from 'react'

import styles from '@/styles/Footer/ContactForm.module.css'

const ContactForm = () => {
    const [nombre, setNombre] = useState('')
    const [apellido, setApellido] = useState('')
    const [email, setEmail] = useState('')
    const [mensaje, setMensaje] = useState('')
    
    const handleSubmit = (event) => {
        event.preventDefault()

        const newMensage = {nombre, apellido, email, mensaje}
        
        console.log(newMensage)

        //Se envia la informacion al BACKEND

        setNombre('')
        setApellido('')
        setEmail('')
        setMensaje('')
    }

    return (
        <div className={`${styles.formContainer}`}>
            <form className={`${styles.form}`} onSubmit={handleSubmit}>
                <label htmlFor="nombre">Nombre:</label>
                <input 
                    type="text"
                    id="nombre"
                    name="nombre"
                    value={nombre}
                    onChange={({ target }) => setNombre(target.value)}
                    required
                />

                <label htmlFor="email">Correo Electrónico:</label>
                <input
                    type="email"
                    id="email"
                    name="email"
                    value={email}
                    onChange={({ target }) => setEmail(target.value)}
                    required
                />

                <label htmlFor="mensaje">Mensaje:</label>
                <textarea
                    id="mensaje"
                    name="mensaje"
                    value={mensaje}
                    rows="4"
                    onChange={({ target }) => setMensaje(target.value)}
                    required
                />

                <button 
                    type="submit"
                    value="enviar"
                    className={`${styles.submitButton}`}
                >
                    Enviar
                </button>
            </form>
        </div>
            
    )
}

export default ContactForm