import Link from 'next/link'

import styles from '@/styles/Footer/Terms.module.css'


const Terms = () => {
    return (
        <div className={`${styles.terms}`}>
            <p>© 2023 NexusBank. Todos los derechos reservados.</p>
            <p>
                Consulta nuestros
                <Link href='/coming-soon'> términos y condiciones</Link>
            </p>
            <p>
                Consulta nuestra
                <Link href='/coming-soon'> política de privacidad</Link>
            </p>
        </div>
    )
}

export default Terms