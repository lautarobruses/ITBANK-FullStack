import styles from '@/styles/Footer/Terms.module.css'

const Terms = () => {
    return (
        <div className={`${styles.terms}`}>
            <p>© 2023 NexusBank. Todos los derechos reservados.</p>
            <p>
                Consulta nuestros
                <a href="enlace"> términos y condiciones</a>
            </p>
            <p>
                Consulta nuestra
                <a href="enlace"> política de privacidad</a>
            </p>
        </div>
    )
}

export default Terms