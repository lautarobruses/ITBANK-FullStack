import styles from '@/styles/Footer/ContactForm.module.css'

const ContactForm = () => {

    const handleSubmit = (event) => {
        event.preventDefault()

    }

    return (
        <div className={`${styles.formContainer}`}>
            <form className={`${styles.form}`} onSubmit={handleSubmit}>
                <label for="nombre">Nombre:</label>
                <input type="text" id="nombre" name="nombre" required />
                
                <label for="apellido">Apellido:</label>
                <input type="text" id="apellido" name="apellido" required />

                <label for="email">Correo Electrónico:</label>
                <input type="email" id="email" name="email" required />

                <label for="mensaje">Mensaje:</label>
                <textarea id="mensaje" name="mensaje" rows="4" required></textarea>

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