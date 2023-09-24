import styles from '@/styles/Footer/Contact.module.css'

const Contact = () => {
    return (
        <div className={`${styles.contact}`}>
            <p>Atención al Cliente:</p>
            <a>+54 9 11 1234-5678</a>
            <a href="mailto:soporte@nexusbank.com">soporte@nexusbank.com</a>
        </div>
    )
}

export default Contact